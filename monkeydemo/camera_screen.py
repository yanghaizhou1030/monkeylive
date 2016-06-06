import time
import io
import threading
import numpy as np
#import ImageGrab
import pyscreenshot as ImageGrab
import PIL

class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    #box = (0,0,320,240)

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    #def get_frame(self):
    #    Camera.last_access = time.time()
    #    self.initialize()
    #    return self.frame

    #@classmethod
    def get_frame(self):
        #with picamera.PiCamera() as camera:
            # camera setup
            #camera.resolution = (320, 240)
            # camera.hflip = True
            #camera.vflip = True

            # let camera warm up
            #camera.start_preview()

            #stream = io.BytesIO()
            #while(True):
                # store frame
                #stream.seek(0)
                #cls.frame = stream.read()
            box = (0,0,320,240)
            printscreen_pil = ImageGrab.grab()
            #reshape_img_data = np.array(printscreen_pil.getdata()).reshape((320,240,3))
            #roiImg = PIL.Image.fromarray(reshape_img_data)
            roiImg = printscreen_pil.crop(box) 
            imgByteArr = io.BytesIO()
            roiImg.save(imgByteArr, format='JPEG')
            frame = imgByteArr.getvalue() 
                # reset stream for next frame
                #stream.seek(0)
                #stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
            #if time.time() - cls.last_access > 20:
                #break
            #    pass
            #cls.thread = None
            return frame
