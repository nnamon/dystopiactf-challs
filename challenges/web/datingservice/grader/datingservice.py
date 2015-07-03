from bottle import get, post, request, response, run # or route

from PIL import Image, ImageDraw
import datetime
import StringIO
import base64

def safeeval(co):
    if ";" in co:
        return "Sorry, unsafe detected!"
    else:
        try:
            data = eval(co)
        except:
            return "Error in safeeval()..."
        return data

def generate_dateimg(fmt):
    img = Image.new('L', (180,20), 255)
    draw = ImageDraw.Draw(img)
    text_to_draw = safeeval("datetime.datetime.now().strftime('%s')" % fmt)
    draw.text((2,2), text_to_draw)
    del draw

    image_buffer = StringIO.StringIO()
    img.save(image_buffer, format="PNG")
    imgStr = image_buffer.getvalue()
    return imgStr


@get('/') # or @route('/login')
def dating():
    return '''
        <html><head><title>Dating Service</title><body>
        Want a date?!? Here's your date:<br />
        <img src="/date?format=%25A%20%25Y-%25m-%25d%20%25H%3A%25M%3A%25S%25p" />
        </body>
        </html>
    '''

@get('/date')
def date_img():
    if not request.query["format"]:
        return "ERROR"
    data = generate_dateimg(request.query["format"])
    response.set_header("Content-Type", "image/png")
    return data

run(host="0.0.0.0", port=1348, server="gunicorn", workers=4)
