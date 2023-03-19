def heapify(data, n, i, swaps):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and data[l] > data[largest]:
        largest = l
 
    if r < n and data[r] > data[largest]:
        largest = r
 
    if largest != i:
        swaps.append((i, largest))
        data[i],data[largest] = data[largest],data[i]
        heapify(data, n, largest, swaps)
 
def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps

def main():
    option = input("Enter input type: ")
    data = []

    if "F" in option:
        # input from file
        try:
            file_path = input("Input file path: ")
            with open(f"tests/{file_path}", "r") as file:
                n = int(file.readline().strip())
                data = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    elif "I" in option:
        # input from keyboard
        try:
            n = int(input())
            data = list(map(int, input().split()))
        except ValueError:
            print("Invalid input format.")
            return
    else:
        print("Invalid input type.")
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
