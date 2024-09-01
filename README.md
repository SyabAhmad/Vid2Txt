# Video Audio Extractor and Text Classifier

This project provides a Python script that extracts audio from a video file, transcribes the audio using Google Speech-to-Text, and classifies the transcription into a predefined category using the Anthropic API.

## Features

- Extracts audio from video files.
- Transcribes audio to text using Google Speech-to-Text.
- Classifies transcribed text using Anthropic's AI model.

## Requirements

To run this project, you'll need:

- Python 3.6+
- `moviepy` for video processing
- `SpeechRecognition` for audio transcription
- `Anthropic` API for text classification
- `pyaudio` (required by `SpeechRecognition`)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SyabAhmad/Vid2txt.git
   cd video-audio-extractor
   ```
2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Add pyaudio**:

   On Linux:

   ```bash
   sudo apt-get install portaudio19-dev python3-pyaudio
   ```

   On Windows:

   Download the appropriate `.whl` file from [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:

   ```bash
   pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
   ```

## Usage

1. **Prepare your environment**: Make sure all dependencies are installed and your Anthropic API key is correctly set up.
2. **Run the script**:

   Place your video file in the project directory or provide the full path to your video file. Then run:

   ```bash
   python main.py
   ```
3. **Transcription and Classification**:

   The script will extract audio from the specified video file, transcribe the audio using Google Speech-to-Text, and classify the transcription using the Anthropic API. The classification result will be printed to the console.

## Code Overview

### `extract_audio_and_transcribe(video_filepath)`

This function:

- Extracts audio from the given video file using `moviepy`.
- Transcribes the audio to text using Google Speech-to-Text.
- Calls the `textClassification` function to classify the transcribed text.

### `textClassification(text)`

This function:

- Uses the Anthropic API to classify the given text into a specific category.
- Returns the classification result.

## Example

Here’s how to use the script:

```python
if __name__ == "__main__":
    videoFilePath = "talksmall.mp4"  # Replace with your video file path
    transcription = extract_audio_and_transcribe(videoFilePath)

    if transcription is None:
        print("Transcription failed. Please check for errors above.")
```

## Troubleshooting

- **Google Speech Recognition could not understand audio**: Ensure the audio quality is good and clear.
- **Could not request results from Google Speech Recognition service**: Check your internet connection and ensure Google API services are accessible.
- **Anthropic API errors**: Make sure your Anthropic API key is correct and that you are using the correct model and parameters.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find a bug.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
