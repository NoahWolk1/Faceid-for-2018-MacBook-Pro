from opencv.fr import FR
BACKEND_URL = "https://us.opencv.fr"
DEVELOPER_KEY = #Add OpenCV key here

sdk = FR(
        BACKEND_URL,
        DEVELOPER_KEY
)

from opencv.fr.persons.schemas import PersonBase

person = PersonBase(
    [
        #add path of a photo of your face
        #add the path of a photo of your face from a different angle
        #add the path of a photo of your face from a different angle
    ],
    name = "#your name"
)

from opencv.fr.search.schemas import SearchRequest, SearchMode


search_request = SearchRequest(["#path of the photo of your face"])

result = sdk.search.search(search_request)

try:
    print (result[0].person.name)
    print (result[0].score)
except:
    print ("not even close")



import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    color = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    # Display the resulting frame
    cv.imshow('frame', frame)
    search_request = SearchRequest([frame])

    try:
        result = sdk.search.search(search_request)
        print (result[0].person.name)
        print (result[0].score)
        if (result[0].score) > 0.7:
            break
    except:
        print("nope, not face even close")
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
