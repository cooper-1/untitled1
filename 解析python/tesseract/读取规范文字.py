# -*-coding:  utf-8 -*-
# @Time    :  2021/2/15 19:58
# @Author  :  Cooper
# @FileName:  读取规范文字.py
# @Software:  PyCharm
from PIL import Image
import pytesseract
#打开要识别的图片
code_image=Image.open('12.png')
#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image)
print(text)
#降噪处理和阈值过滤
code_image=code_image.point(lambda x:0 if x<110 else 255)
#保存图片
code_image.save('3.png')
#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image)
print(text)
#打开要识别的图片
code_image=Image.open('5.png')
#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image)
print(text)
#降噪处理和阈值过滤
code_image=code_image.point(lambda x:0 if x<126 else 255)
#保存图片
code_image.save('6.png')
#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image)
print(text)