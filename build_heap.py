# python3


def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2, -1, -1):
        heap(i, n, data, swaps)
        
    return swaps


def heap(x, n, data, swaps):
    min = x
    
    v = 2*x+1
    if v<n and data[v]<data[min]:
        min = v
    
    w = 2*x+2
    if w<n and data[w]<data[min]:
        min = w
    
    if x != min:
        data[x],data[min] = data[min],data[x]
        swaps.append((x,min))
        heap(min, n, data, swaps)
        
        
def main():
    
    try:
        
        inp = input("Input: I = keyboard, F = file: ")
        
        if inp.startswith('I'):
            n = int(input())
            data = list(map(int, input().split()))
            
        elif inp.startswith('F'):
            name = "tests/" + input("File name: ")
            with open(name, 'r') as g:
                n = int(g.readline())
                data = list(map(int, g.readline().split()))
                    
            
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
            
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
