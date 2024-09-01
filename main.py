import os

from fastapi import FastAPI, File, UploadFile
import json

from api import answer_questions

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/question_answering")
async def question_answering(QuestionsFile: UploadFile, PDFFile: UploadFile ):
    json_data = json.loads(QuestionsFile.file.read())
    file_location = f"uploads/{PDFFile.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await PDFFile.read())
    res = answer_questions(file_location, json_data)
    return res