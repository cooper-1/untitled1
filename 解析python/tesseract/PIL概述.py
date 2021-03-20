# -*-coding:  utf-8 -*-
# @Time    :  2021/2/15 17:43
# @Author  :  Cooper
# @FileName:  PIL概述.py
# @Software:  PyCharm
from PIL import Image
code_image=Image.open('1.jpg')
code_image=code_image.point(lambda x:x*1.5)
code_image.save('2.png')