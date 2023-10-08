from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    # json_data = json.load(open("teas.json", "r", encoding="utf-8"))
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
