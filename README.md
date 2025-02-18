<<<<<<< HEAD
# whisper-model-i
=======
# Sales Conversation Analysis System

A system to transcribe and analyze sales conversations using locally hosted Whisper model.

## Features
- Audio file upload (WAV, MP3, M4A)
- Speech-to-text transcription using local Whisper model
- Basic transcript storage and retrieval
- RESTful API endpoints

## Setup
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Install FFmpeg (required for Whisper):
- On Ubuntu: `sudo apt-get install ffmpeg`
- On macOS: `brew install ffmpeg`
- On Windows: Download from FFmpeg website

3. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints
- POST /upload/ - Upload and transcribe audio file
- GET /transcripts/ - Get all transcripts
- GET /transcripts/{transcript_id} - Get specific transcript

## Future Enhancements
- Speaker identification
- Conversation phase classification
- Sentiment analysis
- User authentication
- Advanced analytics
>>>>>>> 51971e4 (Initial version)
