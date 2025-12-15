from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from ..services.iban_registry_service import IBANRegistryService
from ..model.upload_iban_registry_result import UploadIBANRegistryResult
from ..model.iban_registry import IBANRegistry
from ..core.error_response import ErrorResponse

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload IBAN Registry file",
    description="""Upload a **txt file** containing the IBAN Registry in the format provided by **SWIFT (ISO 13616 standard)**.  
            The file is processed, validated, and stored .""",
    response_model=UploadIBANRegistryResult,
    responses={
        400: {"model": ErrorResponse},
    },
)
async def upload_registry(
    file: UploadFile = File(...), service: IBANRegistryService = Depends()
) -> UploadIBANRegistryResult:

    return service.upload_registry(file)


@router.get(
    "/",
    summary="Get records from IBAN Registry",
    description="Get records from IBAN Registry",
    response_model=list[IBANRegistry],
    responses={
        400: {"model": ErrorResponse},
    },
)
async def find_all(service: IBANRegistryService = Depends()):
    return service.find_all()
