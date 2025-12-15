from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from datetime import datetime

from .routers import iban_registry_router, main_router
from .core.domain_exception import DomainException
from .core.settings import settings

app = FastAPI(
    title="Open IBAN Registry API",
    description="Api for loading and retrieving the IBAN registry according to ISO 13616.",
    version=settings.app_version,
    contact={"name": "Juan Renato Noh"},
    license_info={
        "name": "MIT",
    },
)

app.include_router(main_router.router)
app.include_router(iban_registry_router.router, tags=["registry"], prefix="/registry")


@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):

    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            timestamp=datetime.utcnow().isoformat(),
            message=exc.message,
            path=str(request.url),
        ),
    )
