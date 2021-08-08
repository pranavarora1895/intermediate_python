import threading

event = threading.Event()


def myFunction():
    print("Waiting for event to trigger!!")
    event.wait()
    print("Performing Action XYZ now...")


t1 = threading.Thread(target=myFunction)
t1.start()

x = input("Do you want to trigger the event?? (y/n): ")
if x == 'y':
    event.set()
