import sys
from collections import deque
T = int(input())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    # 입력이 배열의 형태[0,1] 이므로 두번째와 마지막에서 두번째까지의 문자열만을 슬라이싱한다.
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        queue = deque()
    # R의 횟수 세기
    reverse = 0
    # error를 체크하는 flag 출력을 위해 필요
    error = False
    for i in range(len(p)):
        # R이 나올때마다 전부 뒤집지 않고 뒤집은 횟수를 더해서 홀수일때만 마지막에 뒤집을 것
        if p[i] == 'R':
            reverse += 1
        elif p[i] == 'D':
            if len(queue) == 0:
                print('error')
                error = True
                break
            else:
                # 뒤집고 빼든, 빼고 뒤집든 결과가 같으므로
                if reverse % 2 == 1:
                    # 뒤집었을땐 마지막 수
                    queue.pop()
                else:
                    # 안뒤집었을땐 처음 수 빼기
                    queue.popleft()
    # 에러가 아닐때만 배열 출력
    if not error:
        if reverse % 2 == 1:
            queue.reverse()
        # '구분자'.join(리스트)
        print('[' + ','.join(queue) + ']')



