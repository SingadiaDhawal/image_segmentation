# AI Interactive Image Segmentation

Interactive AI-powered image segmentation and hotspot detection system built using Flask, YOLOv8 Segmentation, SVG overlays, and JavaScript.

This project allows users to:
- Upload an image
- Detect objects using AI
- Highlight exact object borders
- Hover over segmented objects
- Click objects interactively
- Display object names directly inside the image

Unlike traditional object detection systems that use rectangular bounding boxes, this project uses instance segmentation to create accurate object outlines.

---

# Features

- AI Object Segmentation
- Interactive Object Highlighting
- Hover Detection
- Clickable Objects
- Exact Object Borders
- SVG Polygon Rendering
- Real-time Label Display
- In-Memory Image Processing
- No Database Required
- No Image Storage
- Local Machine Compatible
- Lightweight Flask Backend

---

# Demo Functionality

## Hover Over Object

When hovering over an object:
- object border glows
- object area highlights
- label appears automatically

## Click Object

When clicking an object:
- object stays selected
- border color changes
- label remains visible

---

# Technologies Used

## Backend

- Flask
- Ultralytics YOLOv8
- Python

## Frontend

- HTML
- CSS
- JavaScript
- SVG

## AI / Computer Vision

- YOLOv8 Segmentation

---

# Supported Models

| Model | Speed | Accuracy | Recommended For |
|---|---|---|---|
| yolov8n-seg.pt | Fastest | Basic | Low-end PCs |
| yolov8s-seg.pt | Balanced | Good | Most users |
| yolov8m-seg.pt | Slower | High | Better segmentation |
| yolov8l-seg.pt | Slowest | Very High | Powerful systems |

Current project uses:

```python
model = YOLO("yolov8s-seg.pt")
```

---

# Project Structure

```text
project/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

```bash
cd your-repo-name
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
flask
ultralytics
pillow
numpy
torch
torchvision
```

---

# Run Project

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# How It Works

## Step 1 — Upload Image

User uploads:
- room image
- indoor scene
- object image
- AI-generated image

---

## Step 2 — AI Segmentation

YOLOv8 Segmentation model:
- detects objects
- generates segmentation masks
- extracts polygon coordinates

---

## Step 3 — SVG Overlay Generation

Frontend creates:
- interactive SVG polygons
- hoverable object regions
- clickable segmented areas

---

## Step 4 — User Interaction

When user:
- hovers object → border highlights
- clicks object → object stays selected
- label appears inside image

---

# Example Output

## Hover Interaction

```text
Hover Sofa
→ Sofa border glows green
→ Label appears: SOFA
```

## Click Interaction

```text
Click Lamp
→ Lamp stays highlighted
→ Cyan border appears
→ Label remains visible
```

---

# Why Segmentation Instead of Bounding Boxes

Traditional detection:

```text
[ Rectangle Box ]
```

This project uses:

```text
Exact Object Shape
```

Benefits:
- more accurate interaction
- better UI experience
- realistic object highlighting
- precise borders

---

# Performance Notes

## Recommended Settings

```python
results = model(
    image_np,
    conf=0.12,
    imgsz=1280
)
```

### Lower Confidence

Better detection of:
- small objects
- indoor items
- partially visible objects

### Higher Image Size

Improves:
- segmentation quality
- object accuracy
- polygon precision

---

# In-Memory Processing

This project does NOT store uploaded images.

Images are:
- processed in RAM
- converted to Base64
- returned directly to frontend

Benefits:
- faster
- secure
- no disk usage
- no cleanup required

---

# Use Cases

- Interactive Image Tagging
- Smart Shopping Interfaces
- AI Annotation Systems
- Google Lens-like Applications
- Visual Search
- Educational Tools
- AR/VR Interfaces
- AI-Powered Media Applications

---

# Future Improvements

- SAM2 Integration
- Grounding DINO Support
- Multi-object Selection
- Semantic Search
- CLIP Embeddings
- Real-time Webcam Detection
- Video Segmentation
- Object Tracking
- Mobile Optimization
- React Frontend
- FastAPI Backend

---

# Screenshots

## Segmentation Hover

- exact object border highlighting
- dynamic labels
- SVG interaction

## Click Selection

- persistent object selection
- interactive segmentation masks

---

# License

MIT License

---

# Author

Dhawal Singadia

MSc Computer Science  
AI/ML and Full Stack Development

---

# Acknowledgements

- Ultralytics
- YOLOv8
- Flask
- OpenCV Community
- PyTorch
```
