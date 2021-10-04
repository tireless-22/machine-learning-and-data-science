from PIL import Image
import os
from PIL import ImageFilter
image1=Image.open("11.png")
image1.rotate(90).save("11_rotate.png")
image1.convert(mode='L').save("11_converted.png")
image1.filter(ImageFilter.GaussianBlur(10)).save("11_blured.png")







