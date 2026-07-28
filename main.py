from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Biathlon Expert API",
    description="API for the Biathlon Expert GPT",
    version="1.0.0",
    servers=[
        {
            "url": "https://biathlon-expert-api.onrender.com"
        }
    ]
)
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Biathlon Expert API работает!"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
