def es_primo(n:int)->bool:
    for i in range(2,int(n**(1/2))):
        if n % i == 0:
            return False
        return True
print(es_primo(67))