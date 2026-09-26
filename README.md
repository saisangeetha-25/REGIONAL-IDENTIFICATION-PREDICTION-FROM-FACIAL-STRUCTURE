# Regional Identification Prediction from Facial Structure

A computer vision and deep learning web application that predicts the regional class associated with a facial image using a trained YOLO object-detection model. The application is built with Django and integrates OpenCV, Ultralytics YOLO, PyTorch, and MySQL.

## 📌 Project Overview

**Regional Identification Prediction from Facial Structure** is a web-based computer vision application developed to perform image-based regional classification using a trained YOLO model.

The application allows users to:

* Register and log in to the system
* Upload a facial image
* Store uploaded image information in a MySQL database
* Process the uploaded image using OpenCV
* Run the trained YOLO model for prediction
* Extract the detected regional class
* Generate an annotated image containing detection results

The trained model currently contains **7 classes**:

1. Bhutan
2. Brazil
3. Dubai
4. India
5. Korean
6. Nigeriaa
7. South_Africa

> **Note:** These class names are reproduced from the project's `data.yaml` configuration.

---

## 🚀 Key Features

* User registration and login
* Admin interface
* Facial image upload
* MySQL database integration
* YOLO-based image prediction
* OpenCV image processing
* Detection result visualization
* Bounding-box visualization using YOLO
* Majority-vote selection when multiple detections are returned
* Django-based web interface

---

## 🛠️ Technology Stack

| Technology          | Purpose                                      |
| ------------------- | -------------------------------------------- |
| Python              | Application and machine learning development |
| Django              | Web application framework                    |
| Ultralytics YOLO    | Object detection and prediction              |
| PyTorch             | Deep learning framework                      |
| OpenCV              | Image processing                             |
| NumPy               | Numerical operations                         |
| Pillow              | Image handling                               |
| Matplotlib          | Visualization                                |
| MySQL               | Database                                     |
| PyMySQL             | Python-MySQL connectivity                    |
| HTML/CSS/JavaScript | Front-end interface                          |

### Main Dependencies

```text
django==2.1.7
PyMySQL==0.9.3
opencv-python==4.13.0.92
ultralytics==8.0.145
matplotlib==3.5.3
numpy==1.21.6
Pillow==9.5.0
torch==1.13.1
torchvision==0.14.1
```

---

## 🧠 Machine Learning Model

The project uses **Ultralytics YOLO** for image-based object detection.

The application loads the trained model from:

```text
runs/train/deepethno/weights/best.pt
```

If a trained model is not available, the project code can initialize a YOLOv8 nano model and train it using the configured dataset.

The training configuration in the application includes:

```python
model.train(
    data='data.yaml',
    epochs=50,
    imgsz=640,
    batch=8,
    name='deepethno',
    project='runs/train'
)
```

### Dataset Classes

The configured dataset contains 7 classes:

```text
Bhutan
Brazil
Dubai
India
Korean
Nigeriaa
South_Africa
```

---

## 🔄 Application Workflow

```text
User Registration/Login
        ↓
Upload Facial Image
        ↓
Image Stored in media/uploads
        ↓
Image Path Stored in MySQL
        ↓
OpenCV Loads Image
        ↓
Trained YOLO Model
        ↓
Object Detection
        ↓
Extract Detected Class
        ↓
Majority Vote
        ↓
Generate Annotated Result
        ↓
Display Prediction
```

---

## 📂 Project Structure

```text
SWT26_DeepEthno regional identification prediction from facial structure/
│
├── SOURCE CODE/
│   └── deepethno/
│       │
│       ├── dataset/
│       │   ├── train/
│       │   │   ├── images/
│       │   │   └── labels/
│       │   └── valid/
│       │       ├── images/
│       │       └── labels/
│       │
│       ├── deepethno/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── wsgi.py
│       │   └── __init__.py
│       │
│       ├── regional_identification_app/
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── views.py
│       │   └── tests.py
│       │
│       ├── media/
│       │   └── uploads/
│       │
│       ├── static/
│       │   ├── css/
│       │   ├── img/
│       │   └── js/
│       │
│       ├── Templates/
│       │   ├── admin/
│       │   └── user/
│       │
│       ├── runs/
│       │   └── train/
│       │       └── deepethno/
│       │           └── weights/
│       │
│       ├── data.yaml
│       ├── manage.py
│       └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saisangeetha-25/REGIONAL-IDENTIFICATION-PREDICTION-FROM-FACIAL-STRUCTURE.git
```

```bash
cd REGIONAL-IDENTIFICATION-PREDICTION-FROM-FACIAL-STRUCTURE
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

The application uses **MySQL** through PyMySQL.

Create a database named:

```text
deepethno
```

The application expects MySQL to be available locally.

Current database configuration used by the application:

```text
Host: localhost
User: root
Database: deepethno
```

The application uses database tables for user information and uploaded image information.

> Before deploying the application publicly, database credentials should be moved to environment variables rather than being stored directly in source code.

---

## ▶️ Running the Application

Navigate to the Django project directory:

```powershell
cd "SOURCE CODE\deepethno"
```

Run the Django development server:

```powershell
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## 🖼️ Prediction Process

When a user uploads an image:

1. Django receives the uploaded image.
2. The image is saved under `media/uploads`.
3. The image path is stored in MySQL.
4. OpenCV loads the uploaded image.
5. The trained YOLO model is loaded.
6. YOLO performs detection.
7. Detected class IDs are converted into class names.
8. If multiple detections are returned, the application uses the most frequent detected class.
9. YOLO generates an annotated image with bounding boxes.
10. The result is saved as:

```text
Static/Result.jpg
```

---

## 📊 Model Configuration

The dataset configuration contains:

```yaml
nc: 7

names:
  - Bhutan
  - Brazil
  - Dubai
  - India
  - Korean
  - Nigeriaa
  - South_Africa
```

The application training configuration uses:

```text
Epochs: 50
Image Size: 640
Batch Size: 8
Model: YOLOv8 Nano initialization when a trained model is unavailable
```

---

## 📸 Screenshots

Add screenshots of the following pages to showcase the project:

### Home Page

```text
Add screenshot here
```

### User Registration/Login

```text
Add screenshot here
```

### Image Upload

```text
Add screenshot here
```

### Prediction Result

```text
Add screenshot here
```

---

## 🔮 Future Improvements

Potential improvements include:

* Improve model performance through additional training data
* Add proper model evaluation metrics
* Improve authentication and password security
* Move database credentials to environment variables
* Add CSRF and other production security protections
* Improve prediction-result presentation
* Add automated testing
* Add API endpoints for model inference
* Deploy the application to a cloud platform
* Improve dataset organization and reproducibility

---

## ⚠️ Important Note

This project involves facial images and regional classification. Any deployment or dataset sharing should follow applicable privacy, consent, and data-protection requirements.

The repository should contain only images/data that the project author is permitted to distribute publicly.

---

## 👩‍💻 Author

**Sai Sangeetha Padakanti**

B.Tech – Computer Science and Engineering

GitHub: [saisangeetha-25](https://github.com/saisangeetha-25)
Emaill: saisangeetha4925@gmail.com

---

## 📄 Project Documentation

Additional project documentation can be included in the repository under the `DOCUMENT` directory.

---

## ⭐ Project Highlights

**Domain:** Computer Vision / Deep Learning

**Framework:** Django

**Model:** YOLO / Ultralytics

**Database:** MySQL

**Image Processing:** OpenCV

**Deep Learning:** PyTorch
