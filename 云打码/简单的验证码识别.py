# -*-coding:  utf-8 -*-
# @Time    :  2021/2/15 23:32
# @Author  :  Cooper
# @FileName:  简单的验证码识别.py
# @Software:  PyCharm
from PIL import Image
import pytesseract

# 打开要识别的图片
code_image = Image.open('a.jpg')
text = pytesseract.image_to_string(code_image)
print(text)
code_image = code_image.convert('L')
''' img.convert(‘L’)
　　为灰度图像，每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    转换公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000
'''
# 重新保存图片
code_image.save('b.jpg')
text = pytesseract.image_to_string(code_image)
print(text)
code_image = code_image.point(lambda x: 0 if x < 110 else 255)
code_image.save('c.jpg')
# 函数进行识别，提取图片中的文字
text = pytesseract.image_to_string(code_image)
print(text)
