# Extract Text from Audio File
It's a set of python scripts that working together, gives you a transcribed text file. Pretty much useful for students, or anyone who wants to extract text from an mp3 or wav file.

## Requirements
This code runs on `python 3.x`. So, please first consider[ installing python](https://www.python.org/downloads/) on your local machine before continuing. Otherwise, go on and read the rest of this documentation.
- ‍‍`ffmpeg`
- `pydub`
- `speech_recognition`

You have to have `ffmpeg` installed for `pydub` to work. To do so, go to their [website](https://ffmpeg.org/download.html). Or use `homebrew` to install it on your machine. Open your terminal and call brew:

```bash
brew install ffmpeg
```

## Instructions
Download the code to your local machine. Unpack the file. Open your terminal/shell. Navigate to the folder by typing the following in your terminal:

`cd /example/AudioToText`

Then install the required packages using `pip` as follow:

```bash
pip install SpeechRecognition pydub
```

And finally, run the `audio_text.py` file in your terminal like below:

```bash
python audio_text.py
```

It will ask for the audio file path. Copy and paste it in your terminal. Bingo, now you have a file on your desktop named `Extracted Text.txt` that contains the text you were looking for. Enjoy!

## Notes
- Given that `SpeechRecognition` uses Google's speech recognition API, you need an active Internet connection to succeed.
- You can manipulate the code and use other speech recognition engines available in `SpeechRecognition` package.

## Future Developments
- Adding support for more audio files
- Adding video to text conversion

## Current Issues
- File conversion works just fine. But, when converted to `wav`, the file size becomes really large.
