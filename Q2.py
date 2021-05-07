'''
시작 시각 :
종료 시각 :


다음 코드에서, 출력되는 결과값이 왜 실제 출력되어야 하는 결과값보다 작은지 설명하시오.

해당 문제점을 해결하기 위해 사용해야 하는 해결책을 서술하고,
해당 개념을 자율차 코드에 적용하였을 때
1) 어느 부분에 적용할 수 있을지,
2) 이를 통해 어떤 이점을 얻을 수 있는지
서술하시오.

(Optional) 아래 코드의 실행 결과값이 실제 출력되어야 하는 결과값과 동일하게 출력되도록 변경하시오.

*** Write Your Answer Below ***


*** Your Answer Ends Here ***
'''


from threading import Thread


class Count:
    def __init__(self):
        self.count = 0

    def add_offset(self, offset):
        self.count += offset


def worker(idx, limit, count_obj):
    print(idx)
    for _ in range(limit):
        count_obj.add_offset(1)


def run_threads(func, thread_num, limit, count_obj):
    threads = []
    for i in range(thread_num):
        args = (i, limit, count_obj)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


limit = 10 ** 6
thread_num = 7
count = Count()
run_threads(worker, thread_num, limit, count)
print(f"Result should be {thread_num * limit}, but the total count is {count.count}")
