from fastapi import APIRouter

router = APIRouter()


@router.get("/", include_in_schema=False)
def root():
    return {
        "name": "Open IBAN Registry API",
        "status": "running",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }


@router.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}
