from fastapi import FastAPI
import math
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Allow CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/sqrt/{x}")
def square_root(x: float):
    if(x<0): return {"result":"Enter valid number"}
    return {"result": math.sqrt(x)}

@app.get("/factorial/{x}")
def factorial(x: int):
    if(x<0): return {"result": "Enter valid number"}
    return {"result": math.factorial(x)}

@app.get("/ln/{x}")
def natural_log(x: float):
    if(x<0): return {"result":"Enter valid number"}
    return {"result": math.log(x)}

@app.get("/power/{x}/{b}")
def power(x: float, b: float):
    return {"result": math.pow(x, b)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
