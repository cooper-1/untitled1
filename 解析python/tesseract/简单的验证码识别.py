# -*-coding:  utf-8 -*-
# @Time    :  2021/2/15 23:32
# @Author  :  Cooper
# @FileName:  简单的验证码识别.py
# @Software:  PyCharm
from PIL import Image
import pytesseract
#打开要识别的图片
code_image=Image.open('13.png')
text=pytesseract.image_to_string(code_image)
print(text)
code_image=code_image.convert('L')
code_image.save('13_1.png')
text=pytesseract.image_to_string(code_image)
print(text)
code_image=code_image.point(lambda x:0 if x<130 else 255)
code_image.save('13_2.png')
#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image)
print(text)