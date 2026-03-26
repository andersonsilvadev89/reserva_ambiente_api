from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ola_mundo():
    return {"mensagem": "Meu primeiro projeto FastAPI está rodando!"}