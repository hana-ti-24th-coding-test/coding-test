# Hana TI 24th - Coding test

> **TBD: Study convention**
f
### 진행 요일

- 매주 월요일 18:00 ~ TBD
- 매주 수요일 16:00 ~ TBD

---

### 폴더 구조

```
├── README.md -> github readme file
├── baekjoon -> 백준 플랫폼 문제 및 풀이 모음
│   ├── greedy -> 알고리즘 분류
│   │   └── 1449 -> 백준 문제 번호
│   │       ├── README.md -> 문제 설명
│   │       └── sol.py -> 풀이 코드
│   └── template -> 백준 플랫폼 용 문제 설명을 위한 템플릿
│       └── README.md
└── programmers -> 프로그래머스 플랫폼 문제 및 풀이 모음
    ├── heap
    │   └── 디스크 컨트롤러 -> 프로그래머스 문제 명
    │       ├── README.md -> 문제 설명
    │       └── sol.py -> 풀이 코드
    └── template -> 프로그래머스 플랫폼 용 문제 설명을 위한 템플릿
        └── README.md
```

---

### 진행 방식

> 진행 방식의 경우 모두의 의견이 필요함, 아래는 **김민재**가 생각한 예시 진행 방식

> **Prerequisite**:
>
> 1. 각자 본인의 branch의 생성(ex) 김민재의 경우, **mj.kim** 이라는 branch가 있어야 함)
>
> 2. 풀어야 하는 알고리즘의 폴더가 이미 생성되어있다고 가정

1. Remote main branch에서 local의 본인 branch로 pull -> Github에 있는 main과 본인 로컬에 있는 branch 동기화
2. 본인의 branch에서 알고리즘 폴더에 풀 문제에 대한 설명이 적혀있는 readme 작성
3. 각자가 정해진 알고리즘의 특정 레벨을 풀거나 품 (푸는 경우, 제한시간 40분)
4. 사다리 타기를 통한 발표자 선정
5. 발표자를 포함한 모든 인원은 main branch로 pull request
6. 발표자를 제외한 인원의 문제 및 코드 리뷰 (pull request 창) (제한시간 ~ 15분)
7. 발표자는 본인의 코드 발표
8. Pull request에 올라온 코드 main으로 merge

---

###  Git을 통한 코드 관리 순서

1. 원격 저장소의 main branch를 local로 pull -> 이를 통한 원격 저장소와 본인 컴퓨터의 branch 동기화
```bash
$ git pull origin main
```

2. 코드 작성

3. 작성한 코드 커밋 (Keyword: **Git commit**)

4. 커밋한 내용 푸쉬 (Keyword: **Git push**)

---

### 자주 쓰는 git 명령어 혹은 기능
> 지극히 김민재의 개인 사견이며... pull, push, commit 명령어는 다루지 않겠습니다! 제가 업무하면서 자주 썼던 명령어 모음이라 생각하시면 좋을 것 같습니다

1. **checkout**: 브랜치 이동 명령어
    ```bash
    # test라는 branch를 만들고 해당 branch로 이동
    # 이미 test라는 branch 존재 시 error 발생 -> -b 옵션 때문
    # -b 옵션: 새로운 브랜치를 만들겠다는 마인드

    $ git checkout -b test # 새로운 test branch를 만들고 해당 브랜치로 이동
    $ git checkout already_existing # 이미 존재하는 already_existing이라는 브랜치로 이동
    ```

2. **stash**: 현재 변경 사항 임시 저장
    - 작업을 하다보면, **작업 도중에 다른 사람이 작업한 내용을 반영**해야할 경우가 있음 -> 이 경우, 원격 branch에서 pull을 해야함
    - 하지만 **pull을 할 경우, 본인의 작업환경(작업하고 있는 로컬 branch)에 변경 사항이 없어야 함** -> 난 이미 작업을 하고 있어서 변경된 내용이 있음... 날려야 하나?
    - 이 경우, **stash를 사용하여 해결 가능**
    - 해당 기능은 명령어 보단 IDE가 제공해주는 UI를 사용하는 것을 추천!

---

### 참고 자료
1. [Github 사용법 (예림씨 자료)](https://rimye.notion.site/Github-0fd219caac2848e79eed4c74d53802f3?pvs=4)
2. [문제 모음집](https://github.com/tony9402/baekjoon)
3. 강의 자료
    - 동빈나
        - [그리디 & 구현](https://youtu.be/2zjoKjt97vQ?si=bCisAZS2f4iWpnSf)
        - [dfs, bfs](https://youtu.be/7C9RgOcvkvo?si=qjIytjzpFYpI5ff5)
        - [다이나믹 프로그래밍](https://youtu.be/5Lu34WIx2Us?si=u2HPUj3u8ubdsxBA)
        - [lcs](https://youtube.com/watch?v=z8KVLz9BFIo&si=lp-hsG7KXH9SQDpf)
        - [최단 경로 알고리즘](https://youtu.be/acqm9mM1P6o?si=dJw-_KGsLoK8rv0q)
        - [Union-find, 크루스칼, 위상정렬](https://youtu.be/aOhhNFTIeFI?si=IxtSROGJQZv9bOgU)
4. markdown
    - [docs](https://www.markdownguide.org/getting-started/)
    - [예시 (김민재 프로젝트 readme)](https://github.com/SW-Engineering-Team1/agricola_backend/blob/main/README.md)
