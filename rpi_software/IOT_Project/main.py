import numpy as np
import cv2
from PIL import Image, ImageDraw
import cognitive_face as CF
import time
import kivy
kivy.require('1.10.0')
#import Clock to create a schedule
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.image import AsyncImage

from kivy.core.window import Window

# Loading images asycnhorously:
# https://kivy.org/docs/api-kivy.uix.image.html#kivy.uix.image.AsyncImage

# Example of dynamic screen manager
# https://stackoverflow.com/questions/34787525/kivy-changing-screen-from-python-code


# Specify the camera to use, 0 = built-in
# cap = cv2.VideoCapture(0)

# KEY = 'bead87ccbe074693a5a793d101c8086d'
#KEY = 'b7ae1171b8ad4b68b3839034902418ec'
#CF.Key.set(KEY)
#BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
#CF.BaseUrl.set(BASE_URL)

class ScreenOne(Screen):

    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)

    #this is event that is fired when the screen is displayed.
    def on_enter(self, *args):
        self.displayScreenThenLeave()

    def displayScreenThenLeave(self):

        #schedued after 3 seconds
        Clock.schedule_once(self.changeScreen, 4)
        # Clock.schedule_once(self.acquireImage, 4)

    def acquireImage(self):
        check_photo = 1
        # while(check_photo == 1):
            # Capture frame-by-frame
            # ret, frame = cap.read()
            #if ret == True:
            #    check_photo = 0
            #    # Our operations on the frame come here
            #    color_obj = cv2.cvtColor(frame, cv2.COLORMAP_BONE)
                # Write the frame into the file newImage.jpg
            #    cv2.imwrite('newImage.jpg', color_obj)

             #   faces = CF.face.detect('newImage.jpg')
        # self.ids.label_1_sc1.color = 0,1,0,1
        # self.ids.label_1_sc1.text = "User Found..."
        # time.sleep(10)


    def changeScreen(self, *args):
        # Switch to screen 2
        self.parent.current = "screen2"

class ScreenTwo(Screen):

    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)

    #this is event that is fired when the screen is displayed.
    def on_enter(self, *args):
        self.command()

    def command(self):
        self.ids.img_src.source = 'meandjarred.png'
        self.ids.label_1_sc2.text = "Hello, Bakir Hajdarevic."

    def changeScreen(self):
        if self.manager.current == 'screen2':
            self.manager.current = 'screen3'
        else:
            self.manager.current = 'screen3'


class ScreenThree(Screen):

    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)

    #this is event that is fired when the screen is displayed.
    def on_enter(self, *args):
        pass

    def changeScreen(self):
        if self.manager.current == 'screen3':
            self.manager.current = 'screen1'
        else:
            self.manager.current = 'screen1'

class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

class ScreensApp(App):

    def build(self):
        m = Manager(transition=NoTransition())
        return m

if __name__ == "__main__":
    ScreensApp().run()

