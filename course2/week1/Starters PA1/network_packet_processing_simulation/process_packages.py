# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []
        self.current_requests = 0

    def Process(self, request):
        for time in self.finish_time_:
            if time > request.arrival_time:
                break
            if time <= request.arrival_time:
                self.finish_time_.pop(0)
                self.current_requests -= 1

        
        if self.current_requests == 0:
            self.finish_time_.append(request.arrival_time + request.process_time)
            self.current_requests += 1
            return Response(False, request.arrival_time)

        if self.current_requests < self.size:
            last_finish_time = self.finish_time_[self.current_requests-1]
            self.finish_time_.append(last_finish_time + request.process_time)
            self.current_requests += 1
            return Response(False, last_finish_time)

        return Response(True, -1)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
