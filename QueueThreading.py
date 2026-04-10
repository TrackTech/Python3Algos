from queue import Queue
import typing
import threading
class Ticket():
    def __init__(self)
        self.comments = []
        self.queue = Queue(maxsize=100)
        self.running = True
        # self._background()
        self.workerThreads = None
        self.maxThreads=100
        self.threadLock = threading.Lock()

        self._background()

    def _queueProcess(self):
        while self.running:
            c = self.queue.get() # call is blocking
            if c is None: # sentinel send to the queue, we are done.
                break
            self.comments.append(c)
            self.queue.task_done()
        
    def _background(self):
        with self.threadLock:
            if not len(self.workerThreads):
                self.workerThread = []
            
            self.workerTheads = [t for t in self.workerThread if t.is_alive()]
            while len(self.workerThreads)<self.maxThreads:
                t = threading.Thread(target=self._queueProcess,daemon=True))
                t.start()
                self.workerThread.append(t)
        
    def addComments(comments:List[str])->bool:
        for c in comments:
            self.queue.put(c)
        return True
    
