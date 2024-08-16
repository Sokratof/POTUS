from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/ping/")
async def read_root():
    return JSONResponse({"message": "pong"})
