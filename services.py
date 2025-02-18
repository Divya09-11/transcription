import whisper
from fastapi import UploadFile
import os
import tempfile
from pathlib import Path
import uuid

# Initialize Whisper model
model = whisper.load_model("medium")

# Add export directory configuration
EXPORT_DIR = os.environ.get('EXPORT_DIR', 'exports')
os.makedirs(EXPORT_DIR, exist_ok=True)

async def process_audio_file(file: UploadFile):
    """
    Process uploaded audio file using Whisper
    """
    # Validate file
    if not file.filename.endswith(('.wav', '.mp3', '.m4a')):
        raise ValueError("Unsupported file format")

    # Create temp file to store upload
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file.flush()
        
        # Transcribe audio
        result = model.transcribe(temp_file.name)

        transcript_id = str(uuid.uuid4())
        
        transcript = {
            "transcript_id": transcript_id,
            "filename": file.filename,
            "content": result["text"],
            "duration": result.get("duration", 0),
            "file_path": temp_file.name,
        }
        export_transcript(transcript)
        return transcript

def get_all_transcripts():
    """
    Retrieve all transcripts (Mock implementation)
    """
    return []

def get_transcript(transcript_id: int):
    """
    Retrieve specific transcript by ID (Mock implementation)
    """
    return None

def export_transcript(transcript: dict) -> str:
    """
    Export transcript to a text file
    Returns the path to the exported file
    """
    base_filename = os.path.splitext(transcript["filename"])[0]
    export_path = Path(EXPORT_DIR)
    output_path = export_path / f"{base_filename}_transcript.txt"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Transcript ID: {transcript['transcript_id']}\n")
        f.write(f"Filename: {transcript['filename']}\n")
        f.write(f"Duration: {transcript['duration']} seconds\n")
        f.write(f"Content:\n{transcript['content']}\n")
            
    return str(output_path)

def export_all_transcripts() -> list:
    """
    Export all transcripts as text files
    Returns a list of exported file paths
    """
    transcripts = get_all_transcripts()
    exported_files = []
    
    for transcript in transcripts:
        exported_files.append(export_transcript(transcript))
    
    return exported_files
