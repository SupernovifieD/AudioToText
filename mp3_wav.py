# found the below piece form this article:
# https://pythonbasics.org/convert-mp3-to-wav/
# then modified it and turned into a working function

from pydub import AudioSegment
from datetime import datetime
import os


def mp3_wav(path):
    # source file
    source = path

    # create a directory to store the converted audio file
    folder_name = "dummy"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    temp_file = os.path.join(folder_name, "temp{:-%Y%m%d%H%M%S}.wav".format(datetime.now()))

    # convert wav to mp3
    sound = AudioSegment.from_mp3(source)
    sound.export(temp_file, format="wav")

    return temp_file
