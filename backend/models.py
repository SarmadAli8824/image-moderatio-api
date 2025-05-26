from pydantic import BaseModel
from datetime import datetime

class TokenRequest(BaseModel):
    token: str
    isAdmin: bool = False

class UsageRecord(BaseModel):
    token: str
    endpoint: str
    timestamp: datetime
