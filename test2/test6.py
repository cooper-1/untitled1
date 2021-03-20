import time

start = time.process_time()

for i in range(100000):

    # print(i)
    pass

end = time.process_time()

print('different is %6.3f' % (end - start))