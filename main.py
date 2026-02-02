from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import numpy as np
import cv2
import uvicorn

app = FastAPI(title="YOLOV8 LSA BACKEND", version="1.0")

model = YOLO("best.pt")

@app.get("/")
def root():
    return {"status": "YOLOV8 LSA BACKEND is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try: 
        #leer la imagen subida
        image_bytes = await file.read()
        np_img = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # inferencia
        results = model.predict(img, conf=0.25, verbose=False)

        if len(results[0].boxes) == 0:
            return {"detected": False}
        
        # tomar la deteccion con mayor confianza
        boxes = results[0].boxes
        best_idx = int(boxes.conf.argmax())

        cls_id = int(boxes.cls[best_idx])
        confidence = float(boxes.conf[best_idx])
        label = results[0].names[cls_id]

        return {
            "detected": True,
            "label": label,
            "confidence": round(confidence, 3)
        }
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)


