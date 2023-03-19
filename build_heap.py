def heapify(lst):
    res = []
    n = len(lst)

    def sift_down(i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and lst[left] < lst[smallest]:
            smallest = left
        if right < n and lst[right] < lst[smallest]:
            smallest = right
        if i != smallest:
            res.append((i, smallest))
            lst[i], lst[smallest] = lst[smallest], lst[i]
            sift_down(smallest)

    for i in range(n // 2, -1, -1):
        sift_down(i)

    return res


def main():
    text = input("choose 'I' for input or 'F' for file")
    if "F" in text:
        f_name = input("Enter file name: ")
        if "a" not in f_name:
            path = './tests/' + f_name
            with open(path, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                lst = list(map(int, file.readline().split()))
    if "I" in text:
        n = int(input())
        lst = list(map(int, input().split()))

    assert lst is not None and len(lst) == n
    swaps = heapify(lst)
    assert len(swaps) <= n * 4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
