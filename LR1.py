import numpy as np

D = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
DD = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
L = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
     "R","S","T","U","V","W","X","Y","Z"]
LL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
      "r","s","t","u","v","w","x","y","z"]

def Diff(li1, li2): 
    li_dif = []
    for i in li1:
        if i not in li2:
            li_dif.append(i)
    return li_dif 

def ind(l , a):
    s = []
    for i in range(len(l)):
        if(l[i] == a):
            s.append(i)
    return s

def bast(l , x , var):
    v = []
    g = 0
    while g < len(l):
        d = l[g].find('.')
        if l[g][d+1] in var and l[g][d+1] not in v:
            v.append(l[g][d+1])
            c = ind(var , l[g][d+1])
            j = 0
            while j < len(c):
                aa = x[c[j]].find(':=')
                xxxx = x[c[j]]
                xxxx = xxxx[:aa+3] + '.' + xxxx[aa+3:]
                if xxxx not in l:
                    l.append(xxxx)
                j += 1
                continue
        g += 1
        continue

def LR1(x):
    var = []
    l = []
    role = []
    for xx in x:
        i = 0
        X = ''
        while i < len(xx):
            if xx[i] in L or xx[i] in LL:
                A = xx[i]
                i += 1
                while xx[i] in L or xx[i] in LL or xx[i] in DD:
                    A += xx[i]
                    i += 1
                    continue
                if xx[i] == ' ' :
                    i += 1
                    var.append(A)
                    if xx[i]+xx[i+1] == ':=':
                        i += 2
                        for ii in range(i+1 , len(xx)):
                            X += xx[ii]
                        role.append(X)
                        l = l + X.split(' ')
                        
                    else:
                        print("Error in role %i"%(i))
                else:
                    print("Error in role %i"%(i))
                break
            else:
                print("Error in role %i"%(i))
        
    term = list(dict.fromkeys(Diff(l,var)))
    va  = []
    i = 0
    for i in range(len(var)):
        if var[i] not in va:
            va.append(var[i])
    
    print('Terminals = %s'%(term))
    print('Variables = %s'%(va))
    I = []
    I0 = []
    xxx = []
    join = []
    count = 1
    First = {}
    Follow = {}
    last = {}
    
    for i in range(len(va)):
        First.update({va[i] : []})
        Follow.update({va[i] : []})
        last.update({va[i] : []})
    
    #First
    s = 0
    while s < len(role):
        rul = role[s].split(' ')
        for ss in First.keys():
            if ss == var[s]:
                if rul[0] not in First[ss] and rul[0] != var[s]:
                    First[ss].append(rul[0])
        s += 1
        continue
    
    for ss in First.keys():
        S = First[ss]
        for i in range(len(S)):
            if S[i] in var:
                SS = First[S[i]]
                for ii in SS:
                    if ii in term and ii != '?':
                        First[ss].append(ii)
    
    for ss in First.keys():
        for zz in First[ss]:
            if zz in var:
                for Z in First[zz]:
                    if Z in term and Z != '?':
                        First[ss].append(Z)
                First[ss].remove(zz)
    
    for ss in First.keys():
        First[ss] = list(dict.fromkeys(First[ss]))
    
    s = 0
    while s < len(role):
        kk = []
        rul = role[s].split(' ')
        S = 0
        while S < len(rul):
            if rul[S] in var and '?' in First[rul[S]]:
                if S != len(rul)-1:
                    if rul[S+1] in term:
                        First[var[s]].append(rul[S+1])
                    else:
                        for g in First[rul[S+1]]:
                            if g != '?':
                                First[var[s]].append(g)
                        S += 1
                        continue
                else:
                    First[var[s]].append('?')
            
            break
        s += 1
        continue
                    
        if len(kk) == 0:
            First[var[s]].append('?')
        s += 1
        continue
    
    s = 0
    while s < len(role):
        kk = []
        rul = role[s].split(' ')
        S = 0
        while S < len(rul):
            if rul[S] in var and '?' in last[rul[S]]:
                if S != 0:
                    if rul[S-1] in term:
                        last[var[s]].append(rul[S-1])
                    else:
                        for g in last[rul[S-1]]:
                            if g != '?':
                                last[var[s]].append(g)
                        S += 1
                        continue
                else:
                    last[var[s]].append('?')
            
            break
        s += 1
        continue
                    
        if len(kk) == 0:
            last[var[s]].append('?')
        s += 1
        continue
    
    print('First = %s'%(First))
    
    
    for j in x:
        f = j + ' ,'
        xxx.append(f)
        
    #I0
    a = xxx[0].find(':=')
    y = xxx[0]
    y = y[0:a+3] + '.' + y[a+3:]
    I0.append(y)
    I.append(I0)
    
    #yal
    #Ii
    n = 0
    while n < len(I):
        ll = []
        vv = []
        var0 = []
        roles = []
        z = 0
        
        for dd in Follow.keys():
            Follow[dd] = []
            
        if n != 0 :
            for u in I[n]:
                o = u.find(':=')
                g = u[:o-1]
                U = len(u)
                uu = u.find(',')
                u = u[uu+1:U-1]
                G = u.split(',')
                for gg in G:
                    Follow[g].append(gg)
                    
        bast(I[n] , xxx , var)
        while z < len(I[n]):
            a = I[n][z].find(':=')
            A = I[n][z][:a-1]
            var0.append(A)
            aa = I[n][z].find(',')
            AA = I[n][z][a+3:aa-1]
            aaa = AA.find('.')
            AA = AA[:aaa] + AA[aaa+1:]
            roles.append(AA)
            z += 1
            continue
            
        g = 0
        while g < 2:
            s = 0
            while s < len(roles):
                rul = roles[s].split(' ')
                for i in range(len(rul)):
                    if rul[i] in var and i != len(rul)-1:
                        if rul[i+1] in term:
                            Follow[rul[i]] = list(np.unique(Follow[rul[i]] + [rul[i+1]]))
                        if rul[i+1] in var:
                            Follow[rul[i]] = list(np.unique(Follow[rul[i]] + First[rul[i+1]]))
                            if '?' in First[rul[i+1]]:
                                Follow[rul[i]].remove('?')
                                Follow[rul[i]] = list(np.unique(Follow[rul[i]] + Follow[rul[i+1]]))
                    if rul[i] in var and i == len(rul)-1:
                        Follow[rul[i]] = list(np.unique(Follow[rul[i]] + Follow[var0[s]]))
                s += 1
                continue
            g += 1
            continue
        
        i = 0
        while i < len(I[n]):
            a = I[n][i].find(':=')
            A = I[n][i][:a-1]
            x = Follow[A]
            for s in range(len(x)):
                d = '{},'.format(x[s])
                I[n][i] = I[n][i] + d
            i += 1
            continue
            
        z = 0
        while z < len(I[n]):
            
            d = I[n][z].find('.')
            
            pp = 0
            while pp < n:
                if I[n] == I[pp]:
                    count = count - 1
                    q = 0
                    I.pop(n)
                    
                    while q < len(join):
                        
                        if(int(join[q][2][1:]) == n):
                            join[q][2] = 'I{}'.format(pp)
                            
                        q += 1
                        continue
                    
                    q = 0
                    while q < len(join):
                        
                        if(int(join[q][2][1:]) > n):
                            join[q][2] = 'I{}'.format(int(join[q][2][1:]) - 1)
                            
                        q += 1
                        continue
                    
                pp += 1
                continue
            
            if I[n][z][d+1] in var:
                
                if I[n][z][d+1] not in vv:
                    
                    vv.append(I[n][z][d+1])
                    
                    #make node
                    join.append(['I{}'.format(n) , I[n][z][d+1] , 'I{}'.format(count)])
                    w = I[n][z][:d] + I[n][z][d+1:]
                    w = w[:d+2] + '.' + w[d+2:]
                    I.append([w])
                    count += 1
                    z += 1
                    continue
                
                if I[n][z][d+1] in vv:
                    
                    cc = 0
                    while cc < len(join):
                        if join[cc][1] == I[n][z][d+1] and int(join[cc][0][1:]) == n:
                            ccc = int(join[cc][2][1:])
                            w = I[n][z][:d] + I[n][z][d+1:]
                            w = w[:d+2] + '.' + w[d+2:]
                            I[ccc].append(w)
                            break
                        cc += 1
                        continue
                    z += 1
                    continue
            
            if I[n][z][d+1] in term:
                
                if I[n][z][d+1] not in ll:
                    
                    join.append(['I{}'.format(n) , I[n][z][d+1] , 'I{}'.format(count)])
                    ll.append(I[n][z][d+1])
                    w = I[n][z][:d] + I[n][z][d+1:]
                    w = w[:d+2] + '.' + w[d+2:]
                    I.append([w])
                    count += 1
                    z += 1
                    continue
                
                if I[n][z][d+1] in ll:
                    cc = 0
                    while cc < len(join):
                        if (join[cc][1] == I[n][z][d+1] and int(join[cc][0][1:]) == n):
                            ccc = int(join[cc][2][1:])
                            w = I[n][z][:d] + I[n][z][d+1:]
                            w = w[:d+2] + '.' + w[d+2:]
                            I[ccc].append(w)
                            break
                        
                        cc += 1
                        continue
                    z += 1
                    continue
                
            if I[n][z][d+1] == ',':
                z += 1
                continue
        
        n += 1
        continue
    
    for p in range(len(I)):
        for q in range(len(I[p])):
            g = I[p][q].find(',')
            gg = len(I[p][q])
            G = I[p][q][g+1:gg-1]
            I[p][q] = I[p][q][:g+1]
            GG = G.split(',')
            GG = list(dict.fromkeys(GG))
            for z in GG:
                d = '{},'.format(z)
                I[p][q] += d
            gg = len(I[p][q])
            I[p][q] = I[p][q][:gg-1]
    
    print('Nodes:')
    for zz in range(len(I)):
        print('I%i = %s'%(zz , I[zz]))
    print('Graph:')
    for zz in join:
        print(zz)
    
x = ['SP := S #' , 
     'A := b A' ,
     'A := b' , 
     'S := a B b' ,
     'S := A B' , 
     'B := B b' , 
     'B := a' ,]
LR1(x)