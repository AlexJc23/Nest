from pydantic import BaseModel, ConfigDict

class ErrorDetail(BaseModel):
    code: str
    message: str

class ErrorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    error: ErrorDetail
