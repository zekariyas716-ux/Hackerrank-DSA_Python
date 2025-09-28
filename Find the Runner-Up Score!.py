if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arranged = sorted(set(arr))
    print(arranged[-2])
