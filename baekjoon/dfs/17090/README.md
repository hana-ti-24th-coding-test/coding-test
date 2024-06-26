## 문제
크기가 N×M인 미로가 있고, 미로는 크기가 1×1인 칸으로 나누어져 있다. 미로의 각 칸에는 문자가 하나 적혀있는데, 적혀있는 문자에 따라서 다른 칸으로 이동할 수 있다.

어떤 칸(r, c)에 적힌 문자가

U인 경우에는 (r-1, c)로 이동해야 한다.
R인 경우에는 (r, c+1)로 이동해야 한다.
D인 경우에는 (r+1, c)로 이동해야 한다.
L인 경우에는 (r, c-1)로 이동해야 한다.
미로에서 탈출 가능한 칸의 수를 계산해보자. 탈출 가능한 칸이란, 그 칸에서 이동을 시작해서 칸에 적힌대로 이동했을 때, 미로의 경계 밖으로 이동하게 되는 칸을 의미한다.## 입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
## 출력
첫째 줄에 미로의 크기 N, M(3 ≤ N, M ≤ 500)이 주어진다. 둘째 줄부터 N개의 줄에는 미로의 각 칸에 적힌 문자가 주어진다.

## 예제 입력

### 입력 1

```
3 3
DDD
DDD
DDD
```

### 출력 1

```
9
```

### 입력 2

```
3 3
DDR
DLU
LLL
```

### 출력 2

```
9
```

### 입력 3

```
3 3
RRD
RDD
ULL
```

### 출력 3

```
0
```

### 입력 3

```
3 4
RRDD
RRDR
DULU
```

### 출력 3

```
4
```