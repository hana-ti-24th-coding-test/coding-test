def main():
    num, tape_len = map(int, input().split())
    hole_list = list(map(int, input().split()))
    hole_list = sorted(hole_list)
    result = 1

    start = hole_list[0]

    for idx in hole_list[1:]:
        if idx in range(start, start+tape_len): continue
        else:
            start =idx
            result += 1

    print(result)


if __name__ == '__main__':
    main()
