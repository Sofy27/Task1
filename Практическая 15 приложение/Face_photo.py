import cv2
name = input("Введите ваше имя пожалуйста: ")

cap = cv2.VideoCapture(0)

for i in range(30):
    cap.read()

ret, frame = cap.read()

cv2.imwrite(f'ImagesAttendance/{name}.jpg', frame)

cap.release()
print("Вы добавлены в список для входа в приложение")