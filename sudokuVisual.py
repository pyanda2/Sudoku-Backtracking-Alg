import cv2 as cv
import numpy as np

# return sudoku board threshold
def thresholdBoard(imagePath):
    squareLength = 450

    image = cv.imread(imagePath, cv.IMREAD_UNCHANGED)
    image = cv.resize(image, (squareLength, squareLength))  
    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurGrayImage = cv.GaussianBlur(grayImage, (5, 5), 0)
    thresholdImage = cv.adaptiveThreshold(blurGrayImage,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    return thresholdImage


    
raw = cv.imread('sudBoard2.PNG', cv.IMREAD_UNCHANGED)
raw = cv.resize(raw, (450, 450))
cv.imshow('raw', raw)

blankImage = np.zeros((450, 450, 3), np.uint8)

imgThresh = thresholdBoard('sudBoard2.PNG')
cv.imshow('threshold', imgThresh)

# finding contours
contours, hierarchy, = cv.findContours(imgThresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
imageContours = raw.copy()
imageBigContour = raw.copy()
cv.drawContours(imageContours, contours, -1, (0, 255, 0), 3)

cv.imshow('Contours', imageContours)

def findBiggestContour(contours):
    biggest = np.array([])
    maxArea = 0
    for i in contours:
        area = cv.contourArea(i)
        if area > 50:
            perimeter = cv.arcLength(i, True)
            approx = cv.approxPolyDP(i, 0.02 * perimeter, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest, maxArea

def reorder(points):
    points = points.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)
    newPoints[0] = points[np.argmin(add)]
    newPoints[3] = points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    newPoints[1] = points[np.argmin(diff)]
    newPoints[2] = points[np.argmax(diff)]
    return newPoints

biggest, maxArea = findBiggestContour(contours)
if biggest.size != 0:
    biggest = reorder(biggest)
    cv.drawContours(imageBigContour, biggest, -1, (0, 255, 0), 10)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [450, 0], [0, 450], [450, 450]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imageWarpColored = cv.warpPerspective(raw, matrix, (450, 450))
    imageDetectedDigits = blankImage.copy()
    imageWarpColored = cv.cvtColor(imageWarpColored, cv.COLOR_BGR2GRAY)

cv.imshow('Biggest contours', imageBigContour)
while True:
        # cv.waitKey(0)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()