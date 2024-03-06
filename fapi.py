from fastapi import FastAPI
import os
from datetime import datetime
import uvicorn
app = FastAPI()


@app.get("/time")
def time():
    return {"current_time": datetime.now()}


@app.get("/path")
def path():
    return os.path.abspath("fapi.py")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
