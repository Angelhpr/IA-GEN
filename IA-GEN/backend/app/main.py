from fastapi import FastAPI

app = FastAPI(
    title="IA-GEN API",
    description="Backend oficial del Instituto IA-GEN",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenido a IA-GEN API"
    }