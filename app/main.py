from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://tufrontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # 👈 Orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],            # 👈 GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],            # 👈 Content-Type, Authorization, etc.
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}