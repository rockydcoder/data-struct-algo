# python3

class Thread:
  def __init__(self, ft, ID):
    self.finish_time = ft
    self.id = ID

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.num_jobs = len(self.jobs)
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(self.num_jobs):
          print(self.assigned_workers[i], self.start_times[i]) 

    def Parent(self, i):
      return floor((i-1)/2)

    def LeftChild(self, i):
      return 2*i + 1

    def RightChild(self, i):
      return 2*i + 2

    def SiftDown(self, i):
      minIndex = i
      l = self.LeftChild(i)
      if l < len(self._data) and self._data[minIndex].finish_time > self._data[l].finish_time:
        minIndex = l
      r = self.RightChild(i)
      if r < len(self._data) and self._data[minIndex].finish_time > self._data[r].finish_time:
        minIndex = r
      if i != minIndex:
        self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
        self.SiftDown(minIndex)

    def SiftUp(self, i):
      while i > 0 and self._data[self.Parent(i)].finish_time > self._data[i].finish_time:
        self._data[i], self._data[self.Parent(i)] = self._data[self.Parent(i)], self._data[i]
        i = self.Parent(i)

    def ChangePriority(self, p):
      self._data[0].finish_time += p
      self.SiftDown(0)


    def assign_jobs(self):
        self._data = list()
        for i in range(self.num_workers):
          self._data.append(Thread(0, i))
        self.assigned_workers = list()
        self.start_times = list()
        while len(self.jobs) > 0:
          job = self.jobs.pop(0)
          self.assigned_workers.append(self._data[0].id)
          self.start_times.append(self._data[0].finish_time)
          self.ChangePriority(job)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

