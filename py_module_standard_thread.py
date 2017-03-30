import threading
import time


def work(num):
    #print('Worker:%s' % num)
    for i in range(5):
        print('Thread %s' % i)
        time.sleep(1)
    return


for i in range(5):
    # 若写成target=work()就变成了顺序执行，不清楚为什么
    t1 = threading.Thread(target=work, args=(i,))
    # t1.setDaemon(False)
    t1.start()
    # join指当前线程执行完再执行下个线程
    t1.join()

#for _, cheese, color in [1, 2, 3], ['manchego', 'stilton', 'brie'], ['red', 'blue', 'green']:
    #print('{} {}'.format(color, cheese))
