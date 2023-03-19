def build_heap(data):
    
    n = len(data)
    swaps = []
    
    for i in range(n):
        j = i
        
        while j > 0 and data[(j - 1) // 2] > data[j]:
            swaps.append((j, (j - 1) // 2))
            data[j], data[(j - 1) // 2] = data[(j - 1) // 2], data[j]
            j = (j - 1) // 2
            
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
