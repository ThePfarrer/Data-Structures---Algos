from queue_impl import Queue

class PrintManager:
    def __init__(self):
        self.queue = Queue()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            self.__print_job(self.queue.dequeue())

    def __print_job(self, document):
        print(document)


if __name__ == "__main__":
    print_manager = PrintManager()

    print_manager.queue_print_job("First Document")
    print_manager.queue_print_job("Second Document")
    print_manager.queue_print_job("Third Document")
    print_manager.run()