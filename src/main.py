from fastapi import FastAPI
from api.absences import router

app = FastAPI()

@app.route('/')
async def main():
    return "Hi"

app.include_router(router)
