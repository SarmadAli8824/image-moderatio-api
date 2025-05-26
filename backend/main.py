from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class ImageRequest(BaseModel):
    image_url: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Moderation API"}

@app.post("/moderate")
def moderate_image(request: ImageRequest):
    try:
        # Download the image
        response = requests.get(request.image_url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Unable to fetch image from URL")

        image_bytes = response.content

        
        # Dummy moderation logic
        if len(image_bytes) % 2 == 0:
            status = "safe"
            message = "The image appears to be safe."
        else:
            status = "unsafe"
            message = "The image may contain unsafe content."

        return {
            "status": status,
            "message": message,
            "image_url": request.image_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Predefined image URL for your testing convenience
@app.get("/test-moderate")
def test_moderate():
    test_image_url = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"
    try:
        response = requests.get(test_image_url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Test image fetch failed")

        image_bytes = response.content
        status = "safe" if len(image_bytes) % 2 == 0 else "unsafe"

        return {
            "status": status,
            "message": "Moderation result of test image",
            "image_url": test_image_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Test failed: {str(e)}")
