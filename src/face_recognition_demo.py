# coding:utf-8

import cv2
import face_recognition
from PIL import Image, ImageDraw


def face_square():
    """
    框选人脸部位
    """
    face_image = face_recognition.load_image_file('face.jpg')
    face_location = face_recognition.face_locations(face_image, model='cnn')
    print(face_location)
    pil_image = Image.fromarray(face_image)
    pos = face_location[0]
    d = ImageDraw.Draw(pil_image, 'RGBA')
    d.rectangle((pos[3], pos[0], pos[1], pos[2]))
    pil_image.show()
    pil_image.save('result.jpg')


def show_face():
    """
    显示人脸图片
    """
    image = face_recognition.load_image_file("face.jpg")
    face_locations = face_recognition.face_locations(image, model="cnn")
    top, right, bottom, left = face_locations[0]
    print(
        "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    pil_image.save("result.jpg")
    pass


def face_lipstick():
    """
    上口红
    """
    face_image = face_recognition.load_image_file('face.jpg')
    face_landmarks_list = face_recognition.face_landmarks(face_image)
    print(face_landmarks_list)
    for face_landmarks in face_landmarks_list:
        pil_image = Image.fromarray(face_image)
        d = ImageDraw.Draw(pil_image, 'RGBA')
        d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=3)
        d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=3)
        pil_image.show()
        pil_image.save('result.jpg')


def dynamic_recognition():
    video_capture = cv2.VideoCapture('rtsp://admin:admin@192.168.0.25:554/25')

    face_image = face_recognition.load_image_file("face.jpg")
    face_image_encoding = face_recognition.face_encodings(face_image)[0]

    face_locations = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([face_image_encoding], face_encoding)

                if match[0]:
                    name = "Barack"
                else:
                    name = "unknown"
                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # face_square()
    # face_lipstick()
    dynamic_recognition()
    pass
