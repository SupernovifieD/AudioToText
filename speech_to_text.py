import speech_recognition as sr
import os
import shutil
from mp3_wav import mp3_to_wav  # Assuming your conversion function is defined as mp3_to_wav_librosa
import librosa
import numpy as np
import tempfile


# Initialize the speech recognition object
r = sr.Recognizer()


def extract_text(path: str) -> str:
    """
    Converts speech in an audio file to text by splitting the audio based on silence.
    
    Parameters:
        path (str): File path to the audio file to be processed.
        
    Returns:
        str: The transcribed text from the audio file.
        
    Notes:
        This function splits audio where silence is detected, processes each chunk
        for speech recognition, and removes temporary files after processing.
    """
    # Convert MP3 to WAV if needed
    file_name = mp3_to_wav(path)
    
    # Load the audio with librosa
    audio_data, sample_rate = librosa.load(file_name, sr=None)

    # Define silence threshold and chunking parameters
    silence_threshold = np.mean(np.abs(audio_data)) * 0.02  # adjust based on audio
    chunk_duration = 0.5  # seconds of silence that defines a split, adjustable

    # Split based on silence
    non_silent_intervals = librosa.effects.split(audio_data, top_db=14)

    # Prepare to store all recognized text
    whole_text = []

    # Process each chunk
    with tempfile.TemporaryDirectory() as folder_name:
        for i, (start, end) in enumerate(non_silent_intervals):
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            
            # Export each audio chunk using librosa's write_wav
            librosa.output.write_wav(chunk_filename, audio_data[start:end], sample_rate)

            # Recognize the audio chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                
                # Try converting it to text
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError:
                    continue
                else:
                    text = f"{text.capitalize()}."
                    whole_text.append(text)

    # Return the transcribed text
    return " ".join(whole_text)


def txt_file(file_path: str):
    """
    Extracts text from an audio file and saves it as a text file on the user's desktop.
    
    Parameters:
        file_path (str): Path to the audio file for transcription.
        
    Returns:
        None
    """
    # Define output path on the Desktop
    output = os.path.join(os.path.expanduser('~'), 'Desktop', "Extracted Text.txt")

    # Extract text from the audio file
    text = extract_text(file_path)

    # Write to the text file
    with open(output, "w") as file:
        file.write(text)

    print("\033[1;31m==>", "\033[1;39mCheck out your Desktop!", "\033[1;31m<==")


# Prompt the user for a file path and start the transcription process
path = input("Give me the file path: ")
txt_file(path)
