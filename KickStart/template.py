#!/usr/bin/env python3

def run_case():
    #Definir que variables son de entrada
    n, k ,s = map(int, input().split())

    return n, k ,s

if __name__ == "__main__":
    for i in range(int(input())):
        print(f'Case #{i+1}:',run_case())