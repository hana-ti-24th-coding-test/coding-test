import sys
L, C = map(int, sys.stdin.readline().split())
list = sorted(sys.stdin.readline().split())
ans = []
# n(index), cnt(모음의 개수), tst(완성되는 비밀번호 문자)
def dfs(n, cnt, tst):
    if n == C:  # 모든 알파벳의 사용 여부를 선택한 경우 종료
        # 비밀번호 길이, 모음개수 >=1, 자음개수>= 2
        if len(tst) == L and cnt >= 1 and L - cnt >= 2:
            ans.append(tst)
        return
    dfs(n+1, cnt + tbl[ord(list[n])], tst + list[n]) # 모음 포함하는 경우
    dfs(n+1, cnt, tst)  # 포함하지 않는 경우


# 모음인 경우 1, 그 외 0이 저장되는 테이블
tbl = [0] * 128  ## ASCII code 영어 소문자 최대값(97~122)
for ch in "aeiou":
    tbl[ord(ch)] = 1


dfs(0, 0, "")
for st in ans:
    print(st)
