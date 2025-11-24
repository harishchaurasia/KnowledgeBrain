# app/stt.py

from faster_whisper import WhisperModel

# Loading the model once at startup (important for speed)
stt_model = WhisperModel("base")

def transcribe_audio(audio_path: str) -> str:
    """
    Take an audio file and return the text using the Faster Whisper model.
    """
    
    # segments is a generator of small transcript pieces
    segments, _ = stt_model.transcribe(audio_path)

    text = " ".join([segment.text for segment in segments])
    
    return text.strip()