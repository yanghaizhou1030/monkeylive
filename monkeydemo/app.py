#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
from camera import Camera

# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera #TODO:need install correct env.

# capture displayscreen image data.
#from camera_capture_screen import Camere #TODO:need to debug.

app = Flask(__name__)


@app.route('/')
def index():
    """monkeylive home page."""
    return render_template('index.html')


def gen(camera):
    """monkeylive generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """monkeylive route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
