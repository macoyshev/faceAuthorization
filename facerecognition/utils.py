import face_recognition
import base64
import PIL


IMG_WB_PATH = 'facerecognition/media/testim.jpg'


def is_tpu_student(students):
    image = face_recognition.load_image_file(IMG_WB_PATH)

    '''check image valid'''
    try:
        image_encoding = face_recognition.face_encodings(image)[0]
    except IndexError:
        return 'INVALID, SHOW FACE'

    for student in students:

        path = 'facerecognition/media/images/' + get_photo_name(student.photo.url)

        photo = face_recognition.load_image_file(path)
        photo_encoding = face_recognition.face_encodings(photo)[0]

        result = face_recognition.compare_faces([photo_encoding], image_encoding)[0]
        if result:

            return student

    return False


def save_wb_image(image_code):
    image = base64.b64decode(image_code)
    with open(IMG_WB_PATH, 'wb') as f:
        f.write(image)
        f.close()


def get_image(path):
    image = PIL.Image.open(path)
    return image


def get_photo_name(url):
    url = url.split('/')[-1]
    return url
