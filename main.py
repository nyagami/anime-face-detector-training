import cv2
import os.path

def detect(filename, cascade_file):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # cv2.imshow("Gray", gray)
    # cv2.imshow("AnimeFaceDetect", image)
    # cv2.waitKey(0)py
    cv2.imwrite(os.path.join(output_dir, 'detected_' + filename), image)

input_dir = 'input'
output_dir = 'output'
xml = 'animeface.xml'
os.makedirs(output_dir, exist_ok=True)
if not os.path.exists(input_dir):
    raise NotADirectoryError("input dir doenst not exist")
for img in os.listdir(input_dir):
    detect(img, xml)