target=6
nums = [2,4,11,3]
result = [None,None]
obj = {3: 3, 2: 0, 11: 2, 4: 1}

for x in obj:
    y = target - x
    if(y in obj and (x != y)):
        print(y,'y')
        result[1] = obj[x]
        result[0] = obj[y]  
        break

print(result)   