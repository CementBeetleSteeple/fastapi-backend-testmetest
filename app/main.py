from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Testmetest API", version="2.1.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "2.1.0"}

@app.get("/api/v1/items")
async def list_items(token: str = Depends(oauth2_scheme)):
    return {"items": [], "total": 0}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
