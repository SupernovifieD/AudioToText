# came along this code in below:
# https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# modified it and made it more usable


import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from mp3_wav import mp3_wav
import shutil

# create a speech recognition object
r = sr.Recognizer()


def extract_text(path):
    """
    splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    then delete the chunks and only return the text
    """

    file_name = mp3_wav(path)
    # open the audio file using pydub
    sound = AudioSegment.from_wav(file_name)

    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )

    # create a directory to store the audio chunks
    folder_name = "/Users/yasin/Desktop/temp_for_test"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    whole_text = []

    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError:
                continue
            else:
                text = f"{text.capitalize()}."
                whole_text += text

    # deleting the temp folder
    shutil.rmtree("/Users/yasin/Desktop/temp_for_test")

    # return the text for all chunks detected
    return whole_text


def txt_file(file_path):
    """
    this function returns a text file containing
    extracted text string from 'extract_text' function
    """

    folder_name = "/Users/yasin/Desktop/"
    output = os.path.join(folder_name, "Extracted Text.txt")

    # creating a .txt file
    file = open(output, "w")
    # extracting text from the desired file
    text = extract_text(path=file_path)
    # writing to the file
    file.writelines(text)
    # closing the file
    file.close()


path = input("Give me the file path. ")
txt_file(path)
