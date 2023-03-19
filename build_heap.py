# python3


def build_heap(data):
    swaps = []
    
    
    x = len(data)
    for i in range(x // 2, -1, -1):
        heap(x, data, swaps)

    return swaps


def heap(x, data, swaps):
    
    min = u
    x = len(data)
    
    v = 2*u+1
    if v<n and data[v]<data[min]:
        min = v
    
    w = 2*u+2
    if w<n and data[w]<data[min]:
        min = w
    
    if x != min:
        data[x],data[min] = data[min],data[x]
        swaps.append((x,min))
        heap(min,data,swaps)

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
                    
            
            
            
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    # checks if lenght of data is the same as the said lenght
    
        assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
        swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
