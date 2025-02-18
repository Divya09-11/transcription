# Local Whisper Usage

Your project is already configured to use Whisper locally! Here's what's already set up:

1. The `openai-whisper` package is listed in your requirements.txt, which is the official package for running Whisper locally.

2. In services.py, the model is initialized locally using:
```python
model = whisper.load_model("medium")
```

3. The transcription is performed locally using:
```python
result = model.transcribe(temp_file.name)
```

To run this project locally, simply:

1. Ensure you have all dependencies installed:
```bash
pip install -r requirements.txt
```

2. Make sure you have ffmpeg installed on your system (required by whisper for audio processing)

3. Run your FastAPI application as normal - all Whisper operations will be performed locally on your PC.

The "base" model is currently being used, but you can modify the model size in services.py by changing the model name to any of:
- "tiny"
- "base"
- "small"
- "medium"
- "large"

Larger models will provide better accuracy but require more computational resources and memory.