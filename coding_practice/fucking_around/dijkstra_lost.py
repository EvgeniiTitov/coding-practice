import threading
import time


'''
https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/
That stuff breaks lol, GO statements break automatic resource cleanup --> must be
dont by hand with custom __exit__()?

Apparently threads/coros can be as bad as goto
'''


def i_write_in_file(file) -> None:
    print("Writer started")
    for i in range(5):
        file.write(str(i))
        print("Writer wrote a line")
        time.sleep(1.0)


def main():
    with open("sample.txt", "w") as file:
        t = threading.Thread(target=i_write_in_file, args=(file,))
        t.start()
        print("Context in main done, closing the file")
    t.join()
    print("Thread joined")


if __name__ == '__main__':
    main()

