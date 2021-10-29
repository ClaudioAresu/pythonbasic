from queue import Queue as q

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    
    def __add__(self, item):
        self.put(item)
    
qu = Queue()
qu + 9
qu + 5
print(qu)
