from fastapi import APIRouter, HTTPException, Depends, Header
from backend.database import tokens_collection
from backend.models import TokenRequest
from datetime import datetime
from fastapi import HTTPException

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

def require_admin_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Header")
    token = authorization.split(" ")[1]
    record = tokens_collection.find_one({"token": token})
    if not record or not record["isAdmin"]:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return token

@auth_router.post("/tokens")
def create_token(data: TokenRequest, _: str = Depends(require_admin_token)):
    if tokens_collection.find_one({"token": data.token}):
        raise HTTPException(status_code=400, detail="Token already exists")
    tokens_collection.insert_one({
        "token": data.token,
        "isAdmin": data.isAdmin,
        "createdAt": datetime.utcnow()
    })
    return {"message": "Token created"}

@auth_router.get("/tokens")
def list_tokens(_: str = Depends(require_admin_token)):
    return list(tokens_collection.find({}, {"_id": 0}))

@auth_router.delete("/tokens/{token}")
def delete_token(token: str, _: str = Depends(require_admin_token)):
    result = tokens_collection.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"message": "Token deleted"}
