# Extract Text from Audio File
It's a set of python scripts that working together, gives you a transcribed text file. Pretty much useful for students, or anyone who wants to extract text from an mp3 or wav file.

## Requirements
- `pydub`
- `speech_recognition`

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
