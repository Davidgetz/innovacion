x = [10,20,20,10,10,30,50,10,20]
counted = {}
list_pares = []
for i,v in enumerate(x):
    if v in counted:
        counted[v] += 1
        if counted[v]%2 == 0:
            list_pares.append(1)
    else:
        counted[v] = 1

print(sum(list_pares))