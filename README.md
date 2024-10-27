# Free Speech to Text Transcription Tool
This tool provides a set of Python scripts that convert audio files (MP3 or WAV) to text, creating a transcribed `.txt` file. This is particularly useful for students, researchers, or anyone needing to extract text from an audio recording efficiently, and for free!

## Requirements
The scripts are compatible with **Python 3.x**. Please [install Python](https://www.python.org/downloads/) before proceeding.

### Dependencies
Install the required Python packages:
- `librosa`
- `numpy`
- `scipy`
- `speech_recognition`

To install these packages, navigate to the project directory in your terminal and run:
```bash
pip install librosa numpy scipy SpeechRecognition
```

### Why No `ffmpeg`?
This version is optimized to remove `ffmpeg` as a dependency. By using `librosa` and `scipy`, we achieve audio processing and silence detection with minimal dependencies and improved efficiency, without needing external tools.

## Instructions
1. Download or clone this repository.
2. Open your terminal, navigate to the downloaded folder:
   ```bash
   cd /path/to/AudioToText
   ```
3. Install the required packages using `pip` as described above.

### Running the Tool
1. Run the `speech_to_text.py` script:
   ```bash
   python speech_to_text.py
   ```
2. Enter the path of the audio file you want to transcribe when prompted.
3. The program will process the audio file, split it based on silence, and perform speech recognition on each chunk.

### Output
A `.txt` file named `Extracted Text.txt` will be saved on your desktop, containing the transcribed text.

## Notes
- **Internet Connection**: The tool uses Google’s speech recognition API, so an active Internet connection is required.
- **Customizable Silence Detection**: Silence detection parameters can be fine-tuned in the code, allowing you to adapt the tool for various audio environments and noise levels.

## Future Developments
- Expand compatibility with more audio formats.
- Add support for direct video-to-text conversion.

## Known Issues
- Large audio files may result in slower processing times.
- Output accuracy is dependent on audio quality and Google’s speech recognition accuracy.

