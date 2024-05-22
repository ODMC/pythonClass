import librosa
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo de música MP3
archivo_mp3 = "cancion_procesada.mp3"
audio, sr = librosa.load(archivo_mp3, sr=None, mono=True)

# Calcular el espectrograma
n_fft = 2048
hop_length = 512
spectrogram = np.abs(librosa.stft(audio, n_fft=n_fft, hop_length=hop_length))

# Convertir a decibeles
spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)

# Visualizar el espectrograma
plt.figure(figsize=(10, 6))
librosa.display.specshow(spectrogram_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la música')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia (Hz)')
plt.show()
