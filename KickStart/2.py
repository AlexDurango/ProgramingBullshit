#!/usr/bin/env python3

def run_case():
    #Definir que variables son de entrada
    left, right= map(int, input().split())
    boring_numbers = 0

    listx=[]
    listx = list(map(int, str(left)))

    for a in range(left, right+1):
        isBoring = True
        listx = list(map(int, str(a)))

        for b in range(len(listx)):
            if (b+1) % 2 == 0:
                if listx[b] % 2 != 0:
                    isBoring = False
                    break
            
            elif (b+1) % 2 != 0:
                if listx[b] % 2 == 0:
                    isBoring = False
                    break
        
        if isBoring:
            boring_numbers +=1


    return boring_numbers


if __name__ == "__main__":
    for i in range(int(input())):
        print(f'Case #{i+1}:',run_case())