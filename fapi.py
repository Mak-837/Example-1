from fastapi import FastAPI
from datetime import datetime
import os
app = FastAPI()


@app.get("/time")
def date_time():
    return {"current_time": datetime.now()}


@app.get("/path")
def path():
    return os.path.abspath('fapi.py')
