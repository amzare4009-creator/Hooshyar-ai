from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return{
        "project": "Hooshyar AI",
        "status": "running"
    }

@router.get("/health")
def health():
    return{
        "status": "healthy"
    }
    