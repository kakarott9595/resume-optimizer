from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Resume Optimizer App is running!"}

@app.get("/upload", response_class=HTMLResponse)
def upload_form():
    return """
    <form action="/upload-resume" method="post" enctype="multipart/form-data">
        <input type="file" name="file"/>
        <input type="submit"/>
    </form>
    """

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
