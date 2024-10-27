import librosa
import scipy.io.wavfile as wavfile
import os
from datetime import datetime

def mp3_to_wav(path: str) -> str:
    """
    Converts an MP3 file to WAV format without using ffmpeg.
    
    Parameters:
        path (str): The file path of the MP3 file to convert.
        
    Returns:
        str: The file path of the newly created WAV file.
    """
    # Define the output folder and create it if necessary
    output_folder = "dummy"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate a unique output filename
    output_filename = os.path.join(
        output_folder, "converted_{:%Y%m%d%H%M%S}.wav".format(datetime.now())
    )

    # Load MP3 file with librosa
    audio_data, sample_rate = librosa.load(path, sr=None)

    # Write to WAV format using scipy
    wavfile.write(output_filename, sample_rate, (audio_data * 32767).astype("int16"))

    return output_filename
