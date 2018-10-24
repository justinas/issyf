import requests
from PIL import Image

def image_from_url(url):
    resp = requests.get(url, stream=True)
    return Image.open(resp.raw)

def get_quadrants(image):
    w, h = image.size
    top_left     = image.crop((  0,   0, w/2, h/2))
    top_right    = image.crop((w/2,   0,   w, h/2))
    bottom_left  = image.crop((  0, h/2, w/2, h))
    bottom_right = image.crop((w/2, h/2,   w, h))
    return (top_left, top_right, bottom_left, bottom_right)
