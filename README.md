# 🧠 Sistema de Detección de Lengua de Señas (LSA) con YOLOv8

Este proyecto implementa un **sistema de detección de letras del alfabeto de la Lengua de Señas Americana (LSA)** utilizando **YOLOv8**, entrenado con un **dataset propio** y desplegado mediante un **backend en Python (FastAPI)**, preparado para ser consumido por una **aplicación móvil (.NET MAUI)** en tiempo casi real.

---

## 🎯 Objetivo del proyecto

Desarrollar un sistema funcional de **detección de objetos** capaz de:

- Detectar letras del alfabeto LSA a partir de imágenes.
- Utilizar un modelo entrenado con datos propios.
- Exponer el modelo mediante una API REST.
- Permitir su integración con una aplicación móvil usando imágenes o frames de cámara.

---

## 🧩 Arquitectura general

App móvil (.NET MAUI)

        │
        │  (envío de imágenes / frames)
        ▼
Backend FastAPI (Python + YOLOv8)

        │
        ▼
Modelo entrenado (best.pt)

---

## 📁 Estructura del proyecto

backendYoloLSA/

├── best.pt

├── main.py

├── requirements.txt

├── README.md

└── runs/

---

## 🗂 Dataset

- Dataset propio recolectado manualmente.
- Etiquetado con Roboflow.
- Formato YOLO (.jpg + .txt).
- Mínimo 80 - 90 imágenes por clase.
link del DataSet
https://drive.google.com/drive/folders/1dz0fM5kLfVIK8mcz5TBbyh8ZMujQkTD0?usp=sharing


Link de api funcional:



---

## 🧠 Modelo y entrenamiento

Versión seleccionada: YOLOv8

Ejemplo:

from ultralytics import YOLO
uso de 2361 imagenes de etiquetado para el entrenamiento
uso de 100 epoch 

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=100,
    imgsz=416,
    batch=4,
    device="cpu"
)

---

## 📊 Métricas

- Precision ≈ 0.80
- Recall ≈ 0.79
- mAP@50 ≈ 0.91
- mAP@50-95 ≈ 0.90

---

## 🚀 Backend

FastAPI + YOLOv8
Endpoint principal:
POST /predict

---

## 🌐 Despliegue

- Ubuntu 22.04 (VPS)
- Gunicorn + Uvicorn
- Nginx
- systemd

---

## 📱 App móvil

La app captura frames, los envía al backend y muestra la letra detectada en tiempo casi real.

---

## 🧪 Pruebas

curl -X POST http://IP_SERVIDOR/predict -F "file=@imagen.jpg"

---

## 🔧 Mejoras futuras

- Dataset más grande
- GPU
- Letras dinámicas
- Optimización móvil

---

## 👨‍💻 Autor

Proyecto académico de detección de objetos aplicado a accesibilidad.


