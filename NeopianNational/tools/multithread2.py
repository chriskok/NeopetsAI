import threading 


def spawnAWorker(i):
    print("%s", i)
    #os.system('start cmd /K ' + workerCmd)
threads = map(lambda i: threading.Thread(target=lambda: spawnAWorker(i)),range(0,10))
for t in threads: t.start()

