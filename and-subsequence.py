t = int(input())

for _ in range(0, t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Filter the elements that can contribute to the AND result >= k
    valid_elements = [x for x in arr if (x & k) == k]


    if not valid_elements:
        print('-1')
    else:
        print(str(len(valid_elements)))