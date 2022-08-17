#### Threading summary

- General info (bullet points from the notes):

Multithreading (language agnostic) shares the memory heap within the process. 
Any thread can access or modify the objects in the same memory heap. → thread 
is lightweight because it contains less resources aka doesn't carry the memory 
space → reduced overhead of spinning new threads or switching context. 
The downside is objects are shared! To keep the shared objects consistent, 
extra language-specific measurements have to be taken.

Multithreading JAVA
JVM natively supports multithreading running on multiple cores → supports true 
parallel execution on multiple cores. 
How does JAVA handle shared object management? JVM chose to support fine-grained 
locks for each resource or object. In JAVA we can use keywords such as 
synchronised, final and volatile to control shared objects.

Cpython is not thread-safe, the interpreter doesn’t support fine-grained 
locking like JVM. Instead, it has the GIL: any thread must hold the GIL to 
access the memory space, and the parallel execution in CPython is just a 
context switch. In Python multithreading is only suggested for IO-related jobs.

Preemptive multitasking. OSs use timeouts to automatically adjust task 
priorities. If a thread is preempted by a timeout, then it is crunching on 
some data and it gets penalized with lower priority (when it gets to run again). 
If a thread suspends early with the timeout time frame, it gets rewarded with 
higher priority (probably some IO, needs just a couple of ticks, give it
priority for responsiveness). High priority threads always preempt low 
priority threads. 

For threads you create/use real system threads (потоки) (preemptive). 
Real because your OS handles when each one works. GIL uses mutexes to ensure 
only 1 system thread’s working at a time (on VM memory)

In terms of simultaneousness of the processes, only multiprocessing actually 
runs them literally at the same time in parallel on different CPU cores. 
Threading and asyncio both run on a single processor and therefore only run 
one process at a time. They simply cleverly find ways to take turns to speed
up the overall process. ** Even though they do not run processes in parallel 
(only one CPU core is getting used) we still call it concurrency because 
multiple tasks are getting processed at the same time (multiple things, parts 
of our program are being worked on simultaneously). A bit of work here, a bit 
of work there etc. One CPU keeps swapping between the threads and does a 
certain amount of work on each one (preemptive VS cooperative multitasking)

The operating system actually knows about each thread and can interrupt it at 
any time to start running a different thread – pre-emptive multitasking. It’s 
called this way because the OS can pre-empt your thread to make the context 
switch. 

Pre-emptive multitasking is handy in the code because the thread doesn’t need 
to do anything to make the switch. This switch can happen in the middle of a 
single Python statement, even a trivial one like x += 1. It just remembers 
where it left the process.

Asyncio uses cooperative multitasking. The tasks must cooperate by announcing 
when they are ready to be switched out. A user can define the place where the 
control will be given back. That means that the code in the task has to change
a bit to make this happen. We await things that can hang.

Все потоки выполняются в рамках одного и того же процесса 🡺 instance methods 
(методы объекта класса), выполняемые в отдельных потоках, имеют доступ к 
оригинальному экземпляру объекта, а не к его копии. 🡺 Любые изменения, 
выполненные в потоке автоматически видны в остальных потоках. 

Если выполняемая в потоке функция возбудит исключение, интерпретатор выведет 
трассировочное сообщение и завершит работу потока, НО остальная часть 
программы продолжит работу.

Треды ничего не возвращают на прямую (когда вызываешь её). Их суть в том, что 
изменить состояние какого-то глобального объекта результатом своей работы. 
Они обычно отдают результат своей работы добавляя их в очередь в очередь или 
поменять значение переменной (Future, etc)

When the function provided or overridden run() method completes (the code in 
it reaches the end of the method), the thread ends its life, disappears from 
the memory. 

It does make sense to wait for threads to complete (your method stop that kills 
all workers) because if your frame writer is accessing a database and you stop 
the server instantly, the data will be corrupted. But if you join you wait 
until it completes whatever its doing, break out of the loop and kills itself. 
That’s why you really don’t want to reinitialize your threads, but rather 
when you launch your server you initialize your workers ones and communicate 
to them via queues. 

Программа не сможет завершиться пока хотя бы один поток продолжает работу, 
если только он не был запущен как поток-демон (daemon). Queues, events, etc for
signalling when to stop. OR mark your thread asa daemon 

Инструкции байт кода неделимые, поэтому некоторые операции обеспечивают 
безопасную работу с потоками – атомарные операции, их выполнение нельзя 
прервать. При их использовании не нужны блокировки и очереди: list.append(), 
обращение в элементам списков, ключам словарей и атрибутом объектов etc. 
На практике лучше всё же использовать блокировки, т.к. набор атомарных 
операций может изменяться от версии к версии. 

- How to run:
    - instance of threading.Thread(target=, args=(), ...)
    - custom class inheriting from threading.Thread and overriding run()
    - concurrent.futures.ThreadPoolExecutor
    
- Communication:
    - Queue
    - Future
    - Variables in global namespace (bad)

- Sync primitives:
    - Lock
    - RLock
    - Condition
    - Semaphore
    - Event
    - Timer
    - Barrier

- Popular issues:
    - Race conditions: when 1+ threads try to change the same object simultaneously (use locks
        or queues)
    - Starvation: when a thread doesn’t get access to a particular resource 
    for a long time – so its just sitting doing blocked nothing. Poor design
    - Deadlock: overusing mutexes, threads are waiting on each other
    - Livelock: a thread keeps running in a loop without making any progress, 
    bad design or use of mutexes

https://docs.python.org/3/library/threading.html

---

#### Multiprocessing summary

TBA

---

#### Asyncio summary

TBA

##### Structured concurrency and AnyIO

A way to write concurrent programs that's easier than manually taking care of 
the lifespan of concurrent tasks (hello asyncio). 

AnyIO - structured concurrency on top of asyncio + supports trio. Provides nurseries 
among other cool features poorly implemented or entirely missing in asyncio.

TBA
