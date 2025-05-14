def es_primo(n:int) -> bool:
    n = abs (n)
    if n == 0 or n == 1:
        return False
    
   #range(2,4) -> [2,3] 
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#no ver casos particulares, con muchos if. 