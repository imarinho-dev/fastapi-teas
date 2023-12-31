from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    expose_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    with open("teas.json", "r", encoding="utf-8") as teas_file:
        json_data = json.load(teas_file)
        return {"teas": json_data}


@app.get("/teas")
async def teas():
    with open("teas.json", "r", encoding="utf-8") as teas_file:
        json_data = json.load(teas_file)
        return json_data

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
