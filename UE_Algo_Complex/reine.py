def placer_reine(Tab,n = 0):
    print(Tab)
    trouve = False
    if n==8:
        trouve = True
        return
    for i in range(8):
        if acceptable(Tab, n, i):
            Tab[n] = i
            placer_reine(Tab, n+1)
            if trouve:
                return Tab
            else:
                Tab[n] = -1

def acceptable(tab, n, i):
    acceptable = True
    if i in tab:
        return False
    for j in range(n):
        if not acceptable:
            return acceptable 
        if abs(i - tab[j]) == abs( n - j):
            acceptable = False
            
    return acceptable

tab = [-1] * 8 
print(placer_reine(tab))