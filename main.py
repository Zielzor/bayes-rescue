import sys
import random
import itertools
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
import cv2 as cv
from time import sleep

MAP = r"cape_python.png"
#coordinates of the searh areas that will be placed on the map
SA1_CORNERS=(130,265,180,315)
SA2_CORNERS=(80,255,130,305)
SA3_CORNERS=(105,205,155,255)

class Search():
    """Main class of SAS game based on Bayes Theorem """

    def __init__(self,name):
        self.name=name
        self.image=cv.imread(MAP, cv.IMREAD_COLOR)
        if self.image is None:
            print(f"Unable to load image {MAP} from file",file=sys.stderr)
            sys.exit(1)

        self.area_acutal=0
        self.sailor_actual=[0,0]#later on both values dor sailr and are will be randomly assigned
        self.sa1=self.image[SA1_CORNERS[1] : SA1_CORNERS[3],
                          SA1_CORNERS[0] : SA1_CORNERS[2]]
        self.sa2=self.image[SA2_CORNERS[1] : SA2_CORNERS[3],
                          SA2_CORNERS[0] : SA2_CORNERS[2]]
        self.sa3=self.image[SA3_CORNERS[1] : SA3_CORNERS[3],
                          SA3_CORNERS[0] : SA3_CORNERS[2]]

        self.p1=0.2
        self.p2=0.5
        self.p3=0.3

        self.sep1=0
        self.sep2=0
        self.sep3=0
    
    def draw_map(self, lkl): #lkl - last known location
        """Draws the map with the last known location of the sailor
        and search areas
        """
        cv.line(self.image, (20,370), (70,370),(0,0,0),2)
        cv.putText(self.image, "0", (8,370),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,0),2)
        cv.putText(self.image, "50 Seamiles", (71,370),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,0))
        cv.rectangle(self.image, (SA1_CORNERS[0],SA1_CORNERS[1]),(SA1_CORNERS[2],SA1_CORNERS[3]),(0,0,0),1)
        cv.putText(self.image, "1", (SA1_CORNERS[0]+3, SA1_CORNERS[1]+15),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,0))
        cv.rectangle(self.image, (SA2_CORNERS[0],SA2_CORNERS[1]),(SA2_CORNERS[2],SA2_CORNERS[3]),(0,0,0),1)
        cv.putText(self.image, "2", (SA2_CORNERS[0]+3, SA2_CORNERS[1]+15),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,0))
        cv.rectangle(self.image, (SA3_CORNERS[0],SA3_CORNERS[1]),(SA3_CORNERS[2],SA3_CORNERS[3]),(0,0,0),1)
        cv.putText(self.image, "3", (SA3_CORNERS[0]+3, SA3_CORNERS[1]+15),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,0))
        cv.putText(self.image, "+", lkl, cv.FONT_HERSHEY_COMPLEX, 1,(0,0,255))
        cv.putText(self.image, "+ = last know location",(240,355),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,255))
        cv.putText(self.image, "* factual location",(240,20),cv.FONT_HERSHEY_COMPLEX, 1,(0,0,255))
        cv.imshow("Search areas", self.image)
        cv.waitKey(500)
        cv.moveWindow("Search areas", 750, 10)