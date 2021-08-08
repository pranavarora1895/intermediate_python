# Intermediate <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen"/> Topics

This repository demonstrates: 
* Threads
* Locks
* Semaphores
* Events
* Daemon Threads
* Queues
* Socket Programming
* Database Programming
* Logging

> # Multi-threading

Threads are used to execute processes simultaneously. It results in using up lesser execution time, efficient use of memory and good communication between the processes make the application to respond faster.

View this [code](https://github.com/pranavarora1895/python_threads/blob/master/main.py) to see how threading in Python works.

> # Thread Synchronization

Threads make processes work simultaneously, but the problems arise when multiple threads are trying to access the same element, which could lead to run-time errors. To overcome this problem, we can use lock or semaphores.

> ### Lock

Lock is used to lock one process until it finishes, and when it gets released down, it allows other process to execute. It prevents the conflict of accessing the same element, thus eliminating run-time error.

View this [code](https://github.com/pranavarora1895/python_threads/blob/master/ThreadSync.py) to see how lock works.

> ### Semaphores

Semaphores are used when we have to lock the process partially. Suppose, in the given [code](https://github.com/pranavarora1895/python_threads/blob/master/semaphores.py) the process locks for 5 seconds and then it is released.

> # Events

When the events are triggered, they process the related tasks or functions.

View this [code](https://github.com/pranavarora1895/python_threads/blob/master/events.py) to see how event works.

> # Daemon Threads

Daemon Threads are those threads which run even when the whole script is finished executing. These threads are used to perform some task continously like reading a file continously as shown in the [code](https://github.com/pranavarora1895/python_threads/blob/master/daemon_threads.py), where a daemon thread reads the file and other thread prints the text from that file for 30 seconds and finishes executing, but that daemon thread never stops.

> # Queues

Queues are the data structures based on First-In-First-Out (FIFO) concept. Queues are very important while dealing with threads. An example is shown in the [code](https://github.com/pranavarora1895/python_threads/blob/master/queues.py) where the elements of the list are put into the queue and as the multiple threads finish processing the elements, the queue eliminates them.

> # Socket Programming

Socket Programming is used to connect to a server in real-time. The server binds the IP-Address and Port Number and the client listens to that IP Address and Port to establish the connection between the two. Socket programming works on OSI Layer 3 (Network Layer) and Layer 4 (Transport Layer). In Layer 4, we have the option of using either TCP or UDP Models.

View Server Code [Here](https://github.com/pranavarora1895/python_threads/blob/master/sockets.py)

View Client Code [Here](https://github.com/pranavarora1895/python_threads/blob/master/socket_client.py)

> # Database Programming

Python can connect to SQL and NoSQL databases efficiently and using Python's Object Oriented Programming Concepts, we can perform CRUD (Create, Read, Update & Delete) operations in the database.

View this [code](https://github.com/pranavarora1895/python_threads/blob/master/databases.py) to understand how database along with python work. This project used SQLite Database.

> # Logging

Logging is a useful tool to manage any application. It is mostly used by the services teams because they use logs that give useful insights to your running application. Logging have 5 levels.

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

Default Setting in the logging level is CRITICAL. So when we perform logging operation, it only displays CRITICAL information on the console. However, the logging levels can be changed. You can set the formatter where you want to store the log, or you can create your own log.

View this [code](https://github.com/pranavarora1895/python_threads/blob/master/loggers.py) to get the better insights in logging.

* Follow Me On Instagram at [Pranav Arora](https://www.instagram.com/arorapranav187)
* Lets Get Connected on Linkedin at [Pranav Arora](https://www.linkedin.com/in/pranav-arora-354b71bb/)


### ThankYou!




