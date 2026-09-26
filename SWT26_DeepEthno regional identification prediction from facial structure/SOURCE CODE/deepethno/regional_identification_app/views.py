from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
import cv2
import pymysql
import traceback, sys, os
from ultralytics import YOLO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin/admin_login.html')


def login_action(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'Admin' and password == 'Admin':
        return render(request, 'admin/admin_home.html')
    else:
        context = {'msg': 'Login failed..!'}
        return render(request, 'admin/admin_login.html', context)


def admin_home(request):
    return render(request, 'admin/admin_home.html')


def logout(request):
    return render(request, 'index.html')



def upload_dataset(request):
    return render(request, 'admin/upload_dataset.html')


def upload_action(request):
    global dataset
    dataset = "dataset\\"
    context = {'data':"Dataset Uploaded Successfully...!!"}
    return render(request, "admin/upload_dataset.html", context)
    

    
global train, valid

def generate_image(request):
    global train, valid
    train = "train"
    valid = "valid"

    context = {'train':len(train), 'validation':len(valid)}
    return render(request, 'admin/generate_image.html', context)

global model

def build_model(request):
    global train, valid, model

    if os.path.exists('runs/train/deepethno/weights/best.pt'):
        # Load the trained model
        model = YOLO("runs/train/deepethno/weights/best.pt")  # Ensure path is correct

        context = {"data": " Yolo Model Loaded ,Successfully...!!"}
        return render(request, 'admin/build_model.html', context)
    else:
        model = YOLO('yolov8n.pt')

        model.train(data='data.yaml', epochs=50,
                    imgsz=640,
                    batch=8,
                    name='deepethno',
                    project='runs/train'
                    )

        context = {"data": " Model Generated Successfully.."}
        return render(request, 'admin/build_model.html', context)



def user_registration(request):
    return render(request, 'user/user_registration.html')


def registration_action(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password != confirm_password:
        return render(request, 'user/user_registration.html', {'msg': 'Passwords do not match'})

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="deepethno",
        charset="utf8"
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s OR email=%s", (username, email))
    existing_user = cur.fetchone()

    if existing_user:
        con.close()
        return render(request, 'user/user_registration.html', {'msg': 'Username or Email already exists!'})

    cur.execute(
        "INSERT INTO user (username, email, password) VALUES (%s, %s, %s)",
        (username, email, password)
    )
    con.commit()
    con.close()
    return render(request, 'user/user_registration.html', {'msg': 'Registration Successful!'})


def user_login(request):
    return render(request, 'user/user_login.html')


def user_login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    con = pymysql.connect(host="localhost", user="root", password="",
                          database="deepethno", charset='utf8')
    cur = con.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    con.close()

    if user:
        request.session['username']=username
        return render(request, 'user/user_home.html', {'username': username})
    else:
        return render(request, 'user/user_login.html', {'msg': 'Invalid username or password'})


def user_home(request):
    return render(request, 'user/user_home.html')



def upload_image(request):
    return render(request, 'user/upload_image.html')


def upload_image_action(request):
    global filename, uploaded_file_url
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        # Save inside media/uploads
        fs = FileSystemStorage(location='media/uploads', base_url='/media/uploads/')
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)  # URL for template (e.g. /media/uploads/myimg.jpg)
        abs_path = fs.path(filename)  # filesystem path (e.g. D:/.../media/uploads/myimg.jpg)

        print("File System Path:", abs_path)
        print("URL Path:", uploaded_file_url)

        # ---- Save into database ----
        con = pymysql.connect(
            host="localhost", user="root", password="",
            database="deepethno", charset='utf8'
        )
        uname=request.session['username']
        cur = con.cursor()
        cur.execute('delete from uploaded_images')
        cur.execute("INSERT INTO uploaded_images (user,image_path) VALUES (%s,%s)", (uname,uploaded_file_url,))
        con.commit()
        con.close()
        #
        # # OpenCV load (use absolute path)
        # imagedisplay = cv2.imread(abs_path)
        # cv2.imshow("Uploaded Image", imagedisplay)
        # cv2.waitKey(0)

    context = {'data': 'Test Image Uploaded Successfully','uploaded_file_url':uploaded_file_url}
    return render(request, 'user/upload_image.html', context)

def Recognize(request):
    con = pymysql.connect(
        host="localhost", user="root", password="",
        database="deepethno", charset='utf8'
    )
    cur = con.cursor()
    cur.execute("SELECT image_path FROM uploaded_images ORDER BY id DESC LIMIT 1")  # get last uploaded
    row = cur.fetchone()
    con.close()

    if row:
        db_path = row[0]  # e.g. "/media/uploads/myimage.jpg"
        print("Path from DB:", db_path)

        # Convert DB path (URL) to absolute path
        abs_path = os.path.join(settings.BASE_DIR, db_path.lstrip("/"))
        print("Absolute Path:", abs_path)

        # Load and display with OpenCV
        imagedisplay = cv2.imread(abs_path)

        model = YOLO("runs/train/deepethno/weights/best.pt")
        results = model(imagedisplay, conf=0.1)

        # Get class names from the model
        class_names = model.names #{0: 'Bhutan', 1: 'Brazil', 2: 'Dubai', 3: 'India', 4: 'Korean', 5: 'Nigeriaa', 6: 'South_Africa'}
        print(class_names)
        # Loop through results and extract class labels
        final_labels = []  # store all detected labels
        for result in results:
            boxes = result.boxes
            if boxes is not None and boxes.cls is not None:
                for cls_id in boxes.cls:
                    label = class_names[int(cls_id)]
                    final_labels.append(label)
                    print("Detected class:", label)
            else:
                print("No detections.")

        # Decide how to pick the "Final Label"
        if final_labels:
            # Option 1: take the first detection
            final_label = final_labels[0]

            # Option 2: take the last detection (your current logic)
            final_label = final_labels[-1]

            # Option 3: majority vote if multiple detections
            from collections import Counter
            final_label = Counter(final_labels).most_common(1)[0][0]

            print("Final Label::", final_label)
        else:
            final_label = "No detection"

        # YOLO draws bounding boxes by itself
        im_array = result.plot()

        # Save result without final label text
        cv2.imwrite("Static/Result.jpg", im_array)

        print("Final Label:: " + str(final_label))

    return render(request, 'user/Result.html')