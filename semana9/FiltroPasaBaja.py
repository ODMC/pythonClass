import librosa # Analisis de audio
import soundfile as sf # Lee y escribe archivos de audio
import numpy as np # Para trabajar con matrices y el procesamiento de señales
import scipy.signal # Para el procesamiento de señales, filtros, y Transformada de fourier
import matplotlib.pyplot as plt # Para visualizar datos graficamente
import librosa.display

# Frecuencia de corte del filtro pasa baja
cutoff_frequency = 1000  # Hz

# Tasa de muestreo
sample_rate = 44100  # Hz

# Coeficientes del filtro pasa baja (Butterworth)
# ORDEN DEL FILTRO, controla que pronunciada es la atenuacion de las frecuencias
# por encima de la frecuencia de corte
order = 4
# Define la frecuencia maxima que puede ser representada
nyquist = 0.5 * sample_rate
# Frecuencia de corte normalizada
normal_cutoff = cutoff_frequency / nyquist
# Coeficientes de filtro pasa baja
b, a = scipy.signal.butter(order, normal_cutoff, btype='low', analog=False)

# Función generadora para procesamiento de audio en tiempo real
def procesar_audio(audio_data):
    # Se usa para almacenar muestras anteriores del audio
    buffer = np.zeros(order)
    # Se itera sobre cada bloque de audio, que representa una parte del audio que se procesara por separada
    for block in audio_data:
        # Aplicar el filtro pasa baja
        # Se realiza la filtracion lineal con los coeficientes (a,b)
        # Se concatena el buffer, con el bloque actual (block) y se aplica el filtro al resultado
        # zi=buffer se usa para especificar la condicion inicial del filtro
        filtered_block, buffer = scipy.signal.lfilter(b, a, np.concatenate((buffer, block)), zi=buffer)
        yield filtered_block

# Cargar el archivo de música MP3
archivo_mp3 = "music.mp3"
audio, sr = librosa.load(archivo_mp3, sr=sample_rate, mono=True)

# Generar los bloques de audio procesados
audio_procesado = procesar_audio(librosa.util.frame(audio, frame_length=1024, hop_length=512))

# Escribir el archivo de audio procesado
archivo_procesado = "music_filtrada.mp3"
sf.write(archivo_procesado, np.concatenate(list(audio_procesado)), sample_rate)

# Cargar el archivo de música MP3 filtrado
audio_filtrado, sr_filtrado = librosa.load(archivo_procesado, sr=None, mono=True)

# Calcular el espectrograma de la música original
n_fft = 2048
hop_length = 512
spectrogram_original = np.abs(librosa.stft(audio, n_fft=n_fft, hop_length=hop_length))
spectrogram_db_original = librosa.amplitude_to_db(spectrogram_original, ref=np.max)

# Calcular el espectrograma de la música filtrada
spectrogram_filtrado = np.abs(librosa.stft(audio_filtrado, n_fft=n_fft, hop_length=hop_length))
spectrogram_db_filtrado = librosa.amplitude_to_db(spectrogram_filtrado, ref=np.max)

# Visualizar los espectrogramas
plt.figure(figsize=(15, 8))

plt.subplot(2, 1, 1)
librosa.display.specshow(spectrogram_db_original, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la música original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')

plt.subplot(2, 1, 2)
librosa.display.specshow(spectrogram_db_filtrado, sr=sr_filtrado, hop_length=hop_length, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la música filtrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')

plt.tight_layout()
plt.show()
