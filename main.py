import cv2
import numpy as np


class FindObject:
    def __init__(self, image, filename):
        self.filename = filename
        self.image = image
        self.font = cv2.cv2.FONT_HERSHEY_SIMPLEX
        self.fontsize = 0.5
        self.fontbold = 1
        self.img = ''
        self.gray_blurred = ...

#         self.detected_circle = ...

    def setParam(self):
        """ prepare image for resume reading """
        # read image
        self.img = cv2.imread(self.image, cv2.IMREAD_COLOR)
        # convert to grayscale
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Bluser using 3*3 kernel.
        self.gray_blurred = cv2.blur(gray, (10, 10))

    def detectCircle(self):
        # Apply Hough transform on the blurred image.
        detected_circles = cv2.HoughCircles(self.gray_blurred,
                                            cv2.HOUGH_GRADIENT, 1, 10, 20, param1=40,
                                            param2=30, minRadius=10, maxRadius=20)

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            print(a, b, r)

            # Draw the circumference of the circle.
            cv2.circle(self.img, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(self.img, (a, b), 1, (0, 0, 255), 3)
#             cv2.putText(self.img, f"(x,y){a,b}", (a-90, b-20), self.font, self.fontsize,
#                         (0, 0, 0), self.fontbold, cv2.LINE_AA)

    #         cv2.imshow("Detected Circle", img)

            fileName = self.filename
            # saving the image
            cv2.imwrite(fileName, self.img)


if __name__ == '__main__':
    fd = FindObject('image.jpg', 'img_output.jpg')
    fd.setParam()
    fd.detectCircle()
