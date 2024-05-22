import librosa
import numpy as np

# Cargar el archivo de música MP3
archivo_mp3 = "music.mp3"
audio, sr = librosa.load(archivo_mp3, sr=None, mono=True)

# Calcular el espectrograma
n_fft = 2048
hop_length = 512
spectrogram = np.abs(librosa.stft(audio, n_fft=n_fft, hop_length=hop_length))

# Obtener las frecuencias correspondientes a las filas del espectrograma
frequencies = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

# Calcular el rango de frecuencia
rango_frecuencia = (np.min(frequencies), np.max(frequencies))

# Calcular la frecuencia promedio
frecuencia_promedio = np.mean(frequencies)

print("Rango de frecuencia:", rango_frecuencia)
print("Frecuencia promedio:", frecuencia_promedio)
