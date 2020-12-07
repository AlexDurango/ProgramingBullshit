
def run_case():
    #Definir que variables son de entrada
    n, k ,s = map(int, input().split())
    option1 = k + n
    option2 = k + k - s + n - s
    return min(option1,option2)

if __name__ == "__main__":
    for i in range(int(input())):
        print(f'Case #{i+1}:',run_case())