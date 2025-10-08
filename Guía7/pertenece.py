#def pertenece (s:list[int],e:int) -> bool:
 #   i : int = 0
  #  for i in s:
   #     if 

def pertenece0 (s:list[int],e:int) -> bool:
    i : int = 0
    res : bool = False
    while i < len(list) and res == False:
        if list[i] == e:
            res = True
        i += 1
    return res
        
def pertenece (s:list[int],e:int) -> bool:
    for i in range(len(s)-1):
        if e == s[i]:
            return True
        else:
            False
        
print(pertenece([1,2,3,4],4))
