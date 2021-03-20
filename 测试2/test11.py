import pyttsx3

teacher = pyttsx3.init()
teacher.say('Hello World!')
rate =teacher.getProperty('rate')   # 获取当前语速（默认值）
print (rate)                        # 打印当前语速（默认值）
teacher.setProperty('rate', 150)
voices = teacher.getProperty('voices')       # 获取当前的音色信息
teacher.setProperty('voice', voices[1].id)
teacher.say('Hello World!')



msg = '''盼望着，盼望着，东风来了，春天的脚步...'''

teacher.say(msg)
teacher.runAndWait()


msg = '''天行健，君子自强不息'''
teacher = pyttsx3.init()
voices = teacher.getProperty('voices')
for i in voices:
    teacher.setProperty('voice', i.id)
    teacher.say(msg)
teacher.runAndWait()