import os
import cv2 
import Equirec2Perspec.Equirec2Perspec as E2P 

if __name__ == '__main__':

    toursFolders = ['tours_1','tours_2','tours_3','tours_4','tours_5','tours_6','tours_7','tours_8','tours_9','tours_10']
    basePath = 'D:/MIRI/hackupc2021/floorfy'
    outputPath = 'D:/MIRI/hackupc2021/floorfy/stage'
    for tourFolder in toursFolders:
        outputTourFolder = os.path.join(outputPath,tourFolder)
        os.mkdir(outputTourFolder)
        fullPathFolder = os.path.join(basePath,tourFolder)
        tours = os.listdir(fullPathFolder)
        for tour in tours:
            outputTourFolderTour = os.path.join(outputTourFolder,tour)
            fullPathFolder2 = os.path.join(fullPathFolder,tour)
            os.mkdir(outputTourFolderTour)
            equirrectangularImages = [f for f in os.listdir(fullPathFolder2) if os.path.isfile(os.path.join(fullPathFolder2, f))]
            for equirrectangularImage in equirrectangularImages:
                outputTourFolderTourImage = os.path.join(outputTourFolderTour,equirrectangularImage)
                os.mkdir(outputTourFolderTourImage)
                equ = E2P.Equirectangular(os.path.join(fullPathFolder2,equirrectangularImage))    # Load equirectangular image
                imgFront = equ.GetPerspective(90, 0, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
                imgRight = equ.GetPerspective(90, 90, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
                imgBack = equ.GetPerspective(90, 180, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
                imgLeft = equ.GetPerspective(90, 270, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
                imgUp = equ.GetPerspective(90, 0, 90, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
                imgDown = equ.GetPerspective(90, 0, -90, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)

                imgH = cv2.hconcat([imgFront, imgRight, imgBack, imgLeft])
                cv2.imwrite(os.path.join(outputTourFolderTourImage,'horizontalView.jpg'), imgH)
                cv2.imwrite(os.path.join(outputTourFolderTourImage,'topView.jpg'), imgUp)
                cv2.imwrite(os.path.join(outputTourFolderTourImage,'bottomView.jpg'), imgDown)
                
                

"""



    equ = E2P.Equirectangular('D:/MIRI/hackupc2021/floorfy/tours_1/242/l_r_equirectangular_242_585ac0c975625.jpeg')    # Load equirectangular image
    
    #
    # FOV unit is degree 
    # theta is z-axis angle(right direction is positive, left direction is negative)
    # phi is y-axis angle(up direction positive, down direction negative)
    # height and width is output image dimension 
    #
    imgFront = equ.GetPerspective(90, 0, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
    imgRight = equ.GetPerspective(90, 90, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
    imgBack = equ.GetPerspective(90, 180, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
    imgLeft = equ.GetPerspective(90, 270, 0, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
    imgUp = equ.GetPerspective(90, 0, 90, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)
    imgDown = equ.GetPerspective(90, 0, -90, 1080, 1080) # Specify parameters(FOV, theta, phi, height, width)

    imgH = cv2.hconcat([imgFront, imgRight, imgBack, imgLeft])
    cv2.imwrite('horizontalView.jpg', imgH)
    cv2.imwrite('topView.jpg', imgUp)
    cv2.imwrite('bottomView.jpg', imgDown)
"""