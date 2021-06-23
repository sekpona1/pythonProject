
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')

async def api(hello: "world"):

    return {"hello":hello}
