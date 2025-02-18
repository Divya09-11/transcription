from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import services

app = FastAPI(title="Sales Conversation Analysis System")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    """
    Upload and process audio file
    """
    try:
        result = await services.process_audio_file(file)
        return {"message": "File processed successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/transcripts/")
def get_transcripts():
    """
    Get all transcripts
    """
    return services.get_all_transcripts()

@app.get("/transcripts/{transcript_id}")
def get_transcript(transcript_id: int):
    """
    Get specific transcript by ID
    """
    transcript = services.get_transcript(transcript_id)
    if transcript is None:
        raise HTTPException(status_code=404, detail="Transcript not found")
    return transcript

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sales Conversation Analysis System!"}

@app.post("/export/{transcript_id}")
async def export_single_transcript(transcript_id: int):
    """
    Export a specific transcript as a text file
    """
    transcript = services.get_transcript(transcript_id)
    if transcript is None:
        raise HTTPException(status_code=404, detail="Transcript not found")
    
    try:
        export_path = services.export_transcript(transcript)
        return {
            "message": "Export successful", 
            "transcript_id": transcript_id,
            "file_path": export_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))