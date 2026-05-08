from fastapi import FastAPI

app = FastAPI(title="SysVen API")


@app.get("/")
def home():
    return {"message": "SysVen funcionando correctamente"}