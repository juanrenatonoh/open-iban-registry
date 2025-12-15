from pydantic import BaseModel
from datetime import datetime


class ErrorResponse(BaseModel):
    timestamp: datetime = datetime.utcnow().isoformat()
    message: str
    path: str
