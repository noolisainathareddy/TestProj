import fastapi as fastapi

app = fastapi.FastAPI()

@app.get("/health")
def health():
    return "app is up and running"


