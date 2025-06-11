import threading

def say_hello(i):
    print("Hello " + str(i) + " from thread " + str(threading.current_thread().name))
    #thread.sleep(10)

for i in range(2):
    print("Hello from main thread")
    thread = threading.Thread(target=say_hello, args=(i,))
    thread.start()
    thread.join()
    threading.Event().wait(5)