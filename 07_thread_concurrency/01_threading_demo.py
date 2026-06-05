#in this example we have got one core and multiple threads which are performing task.
#multithreading (concurrency) it is not multiprocessing
import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"brewing chai for #{i}")
        time.sleep(2)

#create threads
order_thread= threading.Thread(target=take_orders)
brew_thread= threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()
#we will have to wait until brew thread also finish execution.both finish

#join means wait until this thread is finishes.
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")