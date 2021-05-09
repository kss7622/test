'''
시작 시각 : 22:16
종료 시각 : 22:46


다음 코드에서, 출력되는 결과값이 왜 실제 출력되어야 하는 결과값보다 작은지 설명하시오.

해당 문제점을 해결하기 위해 사용해야 하는 해결책을 서술하고,
해당 개념을 자율차 코드에 적용하였을 때
1) 어느 부분에 적용할 수 있을지,
2) 이를 통해 어떤 이점을 얻을 수 있는지
서술하시오.

(Optional) 아래 코드의 실행 결과값이 실제 출력되어야 하는 결과값과 동일하게 출력되도록 변경하시오.

*** Write Your Answer Below ***
프로세스는 보통 직렬 단위로 한 개의 일을 순서대로 처리하는데, 병렬적으로 실행함으로써 처리속도를 높이는 방법이 쓰레드다.
이는 파이썬의 경우 모든 스레드가 거의 동등한 처리 시간 동안 실행하게 하려고 실행중인 스레드를 잠시 중지하고 차례로 다른 스레드를 재개한다.
그래서 공유 메모리 공간값이 제대로 저장되지 않아. Q2에서 출력 결과값이 실제 출력되어야하는 결과값보다 작게 된다.
따라서 다수의 쓰레드의 공유 리소스 접근을 조절할 필요가 있는데, 이는 lock 객체를 이용해 해결이 가능하다.
다수의 쓰레드와 lock 객체를 이용하면, 프로세스의 처리 속도를 높일 수 있고, 이는 자율차 부문에서 인식, 경로계산 처리 속도를 높일 수 있다.
이를 통해 딜레이로 인한 충돌 사고를 방지할 수 있다.
*** Your Answer Ends Here ***
'''

import threading
lock=threading.Lock()
class Count:
    def __init__(self):
        self.count = 0

    def add_offset(self, offset):
        self.count += offset


def worker(idx, limit, count_obj):
    print(idx)
    lock acquire()
    for _ in range(limit):
        count_obj.add_offset(1)
    lock release()


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
