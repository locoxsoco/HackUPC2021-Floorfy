import os
import shutil

if __name__ == '__main__':
    properties = [482665, 427924, 877907, 878056, 874523, 517173, 426977, 877388,
       877238, 877255, 482767, 877717, 823082, 549433, 877881, 878058,
       878436, 878057, 517660, 428594, 877471, 877882, 484211, 425475,
       517964, 866088, 485641, 877237, 803202, 517191, 866962, 877801,
       866289, 877003, 867189, 518112, 878168, 877070, 866383, 553661,
       463521, 448884, 550346, 797102, 877303, 874301, 484167, 873927,
       877182, 517718, 550906, 551976, 876456, 515339, 553709, 550890,
       533656, 867516, 486039, 484231, 517789, 449340, 515968, 427921,
       874135, 519279, 517698, 515616, 267731, 877080, 804061, 515460,
       865807, 440836, 448905, 796187, 534156, 500845]

    toursFolders = ['tours_1','tours_2','tours_3','tours_4','tours_5','tours_6','tours_7','tours_8','tours_9','tours_10']
    basePath = 'D:/MIRI/hackupc2021/floorfy/stage'
    outputPath = 'D:/MIRI/hackupc2021/floorfy/analytics'
    for tourFolder in toursFolders:
        fullPathFolder = os.path.join(basePath,tourFolder)
        tours = os.listdir(fullPathFolder)
        for tour in tours:
            if int(tour) in properties:
                try:
                    outputFolder = os.path.join(outputPath,tourFolder)
                    os.mkdir(outputFolder)
                except:
                    print('')
                outputFolder2 = os.path.join(outputFolder,tour)
                os.mkdir(outputFolder2)
                fullPathFolder2 = os.path.join(fullPathFolder,tour)
                scenes = os.listdir(fullPathFolder2)
                for scene in scenes:
                    inputFolder = os.path.join(os.path.join(os.path.join(basePath,tourFolder),tour),scene)
                    images = os.listdir(os.path.join(inputFolder))
                    print(images)
                    outputFolder3 = os.path.join(outputFolder2,scene)
                    os.mkdir(outputFolder3)
                    for image in images:
                        shutil.copyfile(os.path.join(os.path.join(fullPathFolder2,scene),image), os.path.join(outputFolder3,image))

                