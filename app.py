from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import base64
import numpy as np

app = Flask(__name__)

# MODELS:
# yolov8n-seg.pt = fastest
# yolov8s-seg.pt = balanced
# yolov8m-seg.pt = more accurate
# yolov8l-seg.pt = very accurate

model = YOLO("yolov8s-seg.pt")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():

    file = request.files["image"]

    image = Image.open(file).convert("RGB")

    image_np = np.array(image)

    results = model(
        image_np,
        conf=0.12,
        imgsz=1280
    )

    result = results[0]

    detections = []

    if result.masks is not None:

        for i, mask in enumerate(result.masks.xy):

            cls_id = int(result.boxes.cls[i])

            label = result.names[cls_id]

            conf = float(result.boxes.conf[i])

            polygon = []

            for point in mask:

                polygon.append([
                    int(point[0]),
                    int(point[1])
                ])

            detections.append({
                "label": label,
                "confidence": round(conf, 2),
                "polygon": polygon
            })

    buffered = io.BytesIO()

    image.save(buffered, format="JPEG")

    img_base64 = base64.b64encode(
        buffered.getvalue()
    ).decode("utf-8")

    return jsonify({
        "image_base64": img_base64,
        "detections": detections
    })

if __name__ == "__main__":

    app.run(debug=True)