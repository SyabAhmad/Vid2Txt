import speech_recognition as sr
from moviepy.editor import VideoFileClip
import tempfile
import os
import anthropic

def extract_audio_and_transcribe(video_filepath):
    """
    Extracts audio from a video file, transcribes it using Google Speech-to-Text,
    and returns the transcription or handles potential errors.

    Args:
        video_filepath (str): Path to the video file.

    Returns:
        str: Transcription of the audio content (if successful), or None.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_audio_file = os.path.join(temp_dir, "extracted_audio.wav")

        # Extract audio using moviepy
        try:
            video_clip = VideoFileClip(video_filepath)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(temp_audio_file)
        except Exception as e:
            print(f"Error extracting audio: {str(e)}")
            return None

        # Perform speech recognition using Google Speech-to-Text
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_audio_file) as source:
            try:
                audio_data = recognizer.record(source)
                transcription = recognizer.recognize_google(audio_data)
                print("Asking AI for Classification...")
                result = textClassification(transcription)
                print(f"Response: {result.content[0].text}\n")
                return transcription
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Unexpected error during speech recognition: {str(e)}")

        return None

def textClassification(text):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-opus-20240229",
        temperature=0.5,
        max_tokens=10,
        messages=[
            {
                "role": "user",
                "content": f'"{text}"\nClassify the above text into a category (e.g., educational, abuse, musical, etc.). Provide just one word.'
            }
        ]
    )

    return message

if __name__ == "__main__":
    videoFilePath = r"I:\Code\video to text\vid2txt\smalltalk2.mp4"
    transcription = extract_audio_and_transcribe(videoFilePath)

    if transcription is None:
        print("Transcription failed. Please check for errors above.")
