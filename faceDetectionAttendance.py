import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

mark_zuckerberg_image = face_recognition.load_image_file("images/Mark Zuckerberg.jpg")
mark_zuckerberg_encoding = face_recognition.face_encodings(mark_zuckerberg_image)[0]

bill_gates_image = face_recognition.load_image_file("images/Bill Gates.jpg")
bill_gates_encoding = face_recognition.face_encodings(bill_gates_image)[0]

jeff_bezos_image = face_recognition.load_image_file("images/Jeff Bezos.jpg")
jeff_bezos_encoding = face_recognition.face_encodings(jeff_bezos_image)[0]

steve_jobs_image = face_recognition.load_image_file("images/Steve Jobs.png")
steve_jobs_encoding = face_recognition.face_encodings(steve_jobs_image)[0]

elon_musk_image = face_recognition.load_image_file("images/Elon Musk.jpg")
elon_musk_encoding = face_recognition.face_encodings(elon_musk_image)[0]

albert_einstein_image = face_recognition.load_image_file("images/albert_einstein.jpg")
albert_einstein_encoding = face_recognition.face_encodings(albert_einstein_image)[0]

girl_with_a_pearl_earring_image = face_recognition.load_image_file("images/girl_with_a_pearl_earring.jpg")
girl_with_a_pearl_earring_encoding = face_recognition.face_encodings(girl_with_a_pearl_earring_image)[0]

isaac_newton_image = face_recognition.load_image_file("images/isaac_newton.jpg")
isaac_newton_encoding = face_recognition.face_encodings(isaac_newton_image)[0]

marie_curie_image = face_recognition.load_image_file("images/marie_curie.jpg")
marie_curie_encoding = face_recognition.face_encodings(marie_curie_image)[0]

mona_lisa_image = face_recognition.load_image_file("images/mona_lisa.jpg")
mona_lisa_encoding = face_recognition.face_encodings(mona_lisa_image)[0]

van_gogh_image = face_recognition.load_image_file("images/van_gogh.jpg")
van_gogh_encoding = face_recognition.face_encodings(van_gogh_image)[0]

known_face_encoding = [
    albert_einstein_encoding,
    girl_with_a_pearl_earring_encoding,
    isaac_newton_encoding,
    marie_curie_encoding,
    mona_lisa_encoding,
    van_gogh_encoding,
    bill_gates_encoding,
    elon_musk_encoding,
    steve_jobs_encoding,
    mark_zuckerberg_encoding,
    jeff_bezos_encoding
]

known_faces_names = [
    'albert einstein',
    'girl with a pearl earring',
    'isaac newton',
    'marie curie',
    'mona lisa',
    'van gogh'
    'Bill Gates',
    'Elon Musk',
    'Steve Jobs',
    'Mark Zuckerberg',
    'Jeff Bezos',
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv', 'w+', newline = '')
lswriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame =cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    if s: 
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches= face_recognition.compare_faces(known_face_encoding, face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name+' Present', 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lswriter.writerow([name, current_time])
    cv2.imshow("attendance system", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

video_capture.release() 
cv2.destroyAllWindows()
f.close()
