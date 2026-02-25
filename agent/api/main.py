from fastapi import FastAPI

app = FastAPI(title="Agente Conversacional Técnico Local")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Agente técnico local operativo (modo demo)."}