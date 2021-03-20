# -*-coding:  utf-8 -*-
# @Time    :  2021/2/15 22:45
# @Author  :  Cooper
# @FileName:  识别中文字符.py
# @Software:  PyCharm
from PIL import Image
import pytesseract
#打开要识别的图片
code_image=Image.open('12.png')

#函数进行识别，提取图片中的文字
text=pytesseract.image_to_string(code_image,lang='chi_sim')
print(text)