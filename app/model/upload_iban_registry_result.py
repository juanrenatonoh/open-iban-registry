from pydantic import BaseModel


class UploadIBANRegistryResult(BaseModel):

    total_records: int
