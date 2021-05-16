import os
import cv2 

if __name__ == '__main__':

    toursFolders = ['tours_1','tours_2','tours_3','tours_4','tours_5','tours_6','tours_7','tours_8','tours_9','tours_10']
    basePath = 'D:/MIRI/hackupc2021/floorfy/stage'
    for tourFolder in toursFolders:
        fullPathFolder = os.path.join(basePath,tourFolder)
        tours = os.listdir(fullPathFolder)
        for tour in tours:
            fullPathFolder2 = os.path.join(fullPathFolder,tour)
            scenes = os.listdir(fullPathFolder2)
            for scene in scenes:
                fullPathFolder3 = os.path.join(fullPathFolder2,scene)
                img = cv2.imread(os.path.join(fullPathFolder3,'horizontalView.jpg'))
                imgFront = img[0:1080, 0:1080]
                imgRight = img[0:1080, 1080:2160]
                imgBack = img[0:1080, 2160:3240]
                imgLeft = img[0:1080, 3240:4320]
                cv2.imwrite(os.path.join(fullPathFolder3,'imgFront.jpg'), imgFront)
                cv2.imwrite(os.path.join(fullPathFolder3,'imgRight.jpg'), imgRight)
                cv2.imwrite(os.path.join(fullPathFolder3,'imgBack.jpg'), imgBack)
                cv2.imwrite(os.path.join(fullPathFolder3,'imgLeft.jpg'), imgLeft)