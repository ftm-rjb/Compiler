#Change the path of TestFile and InputFile in your pc in last line or put the Files on Desktop
import numpy as np
import pandas as pd

rs = ["integer" , "real" , "word" , "char" , "array" , "condition","until","enter","tab"]
dl = ["%" , "=" , "(" , ")" , "+" , "-" , "*" , "'" , "&" , "," , ":"]
dl3 = ["|" , "/" , "<" , ">"]
dl2 = [":=" , "!=" , "<=" , ">=" , "//"]
v = []
D = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
DD = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
L = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
     "R","S","T","U","V","W","X","Y","Z"]
LL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
      "r","s","t","u","v","w","x","y","z"]
strng = ['"']


def Scanner(inpt):
    
    tokens = []
    space = ' '
    j = 0
    
    F = open(inpt , "r")
    line = F.readlines()
    
    print(line)
    
    for j in range(len(line)):
        i = 0
        A = ''
        token = ['' , A]
        m = ''
        n = ''
        w = ''
        
        while(i<len(line[j])):
            
            if(line[j][i] == '#'):
               if((j == len(line)-1) and (i == len(line[j])-1)):
                   A = line[j][i]
                   tokens.append(['END' , A])
                   i += 1
                   continue
               else:
                   A = line[j][i]
                   tokens.append(['ERROR' , A])
                   i += 1
                   continue
                   
            if(line[j][i] == space):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] == space):
                        A += line[j][i]
                        i += 1
                        if(line[j][i] == space):
                            A += line[j][i]
                            i += 1
                            if(line[j][i] == space):
                                A += line[j][i]
                                tokens.append(['RS' , 'tab'])
                                i += 1
                                continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
            
                except IndexError:
                    break
            
            if(line[j][i] == '-' or line[j][i] == '+'):
                A = line[j][i]
                i += 1
                if(line[j][i] in D):
                    A += line[j][i]
                    token[0] = 'Integer'
                    token[1] = A
                    i += 1
                    try:
                        while(line[j][i] in DD):
                            A += line[j][i]
                            token[1] = A
                            i += 1
                            
                        if(line[j][i] == '.'):
                            A += line[j][i]
                            token[0] = 'ERROR'
                            token[1] = A
                            i += 1
                            
                            if(line[j][i] in DD):
                                A += line[j][i]
                                token[0] = 'Real'
                                token[1] = A
                                i += 1
                                
                                while(line[j][i] in DD):
                                    A += line[j][i]
                                    token[1] = A
                                    i += 1
                                    
                                tokens.append(['Real' , A])
                                if(A not in v):
                                    v.append(A)
                                continue
                                
                            else:
                                tokens.append(['ERROR' , A])
                                continue
                            
                        else:
                            tokens.append(['Integer' , A])
                            if(A not in v):
                                v.append(A)
                            continue
                            
                    except IndexError:
                        tokens.append(token)
                        if((A not in v) and (token[0] != 'ERROR')):
                            v.append(A)
                        break
                    
                if(line[j][i] == '0'):
                    A += line[j][i]
                    token[0] = 'Integer'
                    token[1] = A
                    i += 1
                    try:
                        if(line[j][i] == '.'):
                            A += line[j][i]
                            token[0] = 'ERROR'
                            token[1] = A
                            i += 1
                            
                            if(line[j][i] in DD):
                                A += line[j][i]
                                token[0] = 'Real'
                                token[1] = A
                                i += 1
                                
                                while(line[j][i] in DD):
                                    A += line[j][i]
                                    token[1] = A
                                    i += 1
                                
                                tokens.append(['Real' , A])
                                if(A not in v):
                                    v.append(A)
                                continue
                                
                            tokens.append(['ERROR' , A])
                            continue
                        
                        tokens.append(['Integer' , A])
                        if(A not in v):
                            v.append(A)
                        continue
                            
                    except IndexError:
                        tokens.append(token)
                        if((A not in v) and (token[0] != 'ERROR')):
                            v.append(A)
                        break
                
                else:
                    tokens.append(['DL_OP' , A])
                    continue
                
            
            if(line[j][i] in D):
                A = line[j][i]
                token[0] = 'Integer'
                token[1] = A
                i += 1
                try:
                    while(line[j][i] in DD):
                        A += line[j][i]
                        token[1] = A
                        i += 1
                        
                    if(line[j][i] == '.'):
                        A += line[j][i]
                        token[0] = 'ERROR'
                        token[1] = A
                        i += 1
                        
                        if(line[j][i] in DD):
                            A += line[j][i]
                            token[0] = 'Real'
                            token[1] = A
                            i += 1
                            
                            while(line[j][i] in DD):
                                A += line[j][i]
                                token[1] = A
                                i += 1
                                
                            tokens.append(['Real' , A])
                            if(A not in v):
                                v.append(A)
                            continue
                            
                        else:
                            tokens.append(['ERROR' , A])
                            continue
                        
                    else:
                        tokens.append(['Integer' , A])
                        if(A not in v):
                            v.append(A)
                        continue
                        
                except IndexError:
                    tokens.append(token)
                    if((A not in v) and (token[0] != 'ERROR')):
                        v.append(A)
                    break
                
            if(line[j][i] == '0'):
                A = line[j][i]
                token[0] = 'Integer'
                token[1] = A
                i += 1
                try:
                    if(line[j][i] == '.'):
                        A += line[j][i]
                        token[0] = 'ERROR'
                        token[1] = A
                        i += 1
                        
                        if(line[j][i] in DD):
                            A += line[j][i]
                            token[0] = 'Real'
                            token[1] = A
                            i += 1
                            
                            while(line[j][i] in DD):
                                A += line[j][i]
                                token[1] = A
                                i += 1
                            
                            tokens.append(['Real' , A])
                            if(A not in v):
                                v.append(A)
                            continue
                            
                        tokens.append(['ERROR' , A])
                        continue
                    
                    tokens.append(['Integer' , A])
                    if(A not in v):
                        v.append(A)
                    continue
                        
                except IndexError:
                    tokens.append(token)
                    if((A not in v) and (token[0] != 'ERROR')):
                        v.append(A)
                    break
                        
            if((line[j][i] in L) or (line[j][i] in LL)):
                A = line[j][i]
                i += 1
                try:
                    while((line[j][i] in L) or (line[j][i] in LL) or (line[j][i] in DD)):
                        A += line[j][i]
                        i += 1
                    
                    if(A in rs):
                        tokens.append(['RS' , A])
                        continue
                    
                    tokens.append(['ID' , A])
                    if(A not in v):
                        v.append(A)
                    continue
            
                except IndexError:
                    if(A in rs):
                        tokens.append(['RS' , A])
                        break
                    tokens.append(['ID' , A])
                    if(A not in v):
                        v.append(A)
                    break
                    
            if(line[j][i] in strng):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] not in strng):
                        A += line[j][i]
                        i += 1
                        
                        if(line[j][i] in strng):
                            A += line[j][i]
                            tokens.append(['Char' , A])
                            if(A not in v):
                                v.append(A)
                            i += 1
                            continue
                        
                        while(line[j][i] not in strng):
                            A += line[j][i]
                            i += 1
                            if(line[j][i] in strng):
                                break
                            
                    if(line[j][i] in strng):
                        A += line[j][i]
                        tokens.append(['Word' , A])
                        if(A not in v):
                            v.append(A)
                        i += 1
                        continue
                    
                except IndexError:
                    tokens.append(['ERROR' , A])
                    break
            
            if(line[j][i] == '|'):
                A = line[j][i]
                token[0] = 'DL_OP'
                token[1] = A
                i += 1
                try:
                    if(line[j][i] == '|'):
                        A += line[j][i]
                        token[0] = 'comment_1line'
                        token[1] = A
                        i += 1
                        
                        for q in range(i , len(line[j])-1):
                            A += line[j][q]
                            i += 1
                            
                        tokens.append(['comment_1line' , A])
                        if(A not in v):
                            v.append(A)
                        continue
                    
                    if(line[j][i] == '.'):
                        A += line[j][i]
                        token[0] = 'ERROR'
                        token[1] = A
                        i += 1
                        
                        for q in range(i , len(line[j])):
                            m += line[j][q]
                            
                        if('.|' in m):
                            x = m.find('.|')
                            xx = x + i + 1
                            
                            for q in range(i , xx+1):
                                A += line[j][q]
                                i += 1
                            
                            tokens.append(['comment_multiline' , A])
                            if(A not in v):
                                v.append(A)
                            continue
                        
                        else:
                            A += m
                            try:
                                line[j] = ''
                                z = j+1
                                while(z<len(line)):
                                    if('.|' not in line[z]):
                                        A += line[z]
                                        token[1] = A
                                        line[z] = ''
                                        z += 1
                                        continue
                                    else:
                                        y = line[z].find('.|')
                                        for q in range(y+2):
                                            n += line[z][q]
                                        for ww in range(y+2 , len(line[z])):
                                            w += line[z][ww]
                                        A += n
                                        line[z] = w
                                        token[0] = 'comment_multiline'
                                        token[1] = A
                                        i = y + 2
                                        break
                                tokens.append(token)
                                if((A not in v) and (token[0] != 'ERROR')):
                                    v.append(A)
                                continue
                                
                            except IndexError:
                                tokens.append(token)
                                if((A not in v) and (token[0] != 'ERROR')):
                                    v.append(A)
                                break
                        
                    else:
                        tokens.append(['DL_OP' , A])
                        continue

                except IndexError:
                    tokens.append(token)
                    if((A not in v) and (token[0] != 'ERROR') and (token[0] != 'DL_OP')):
                        v.append(A)
                    break
                
            if(line[j][i] in ['<' , '>']):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] == '='):
                        A += line[j][i]
                        tokens.append(['DL_OP' , A])
                        i += 1
                        continue
                    else:
                        tokens.append(['DL_OP' , A])
                        continue
            
                except IndexError:
                    tokens.append(['DL_OP' , A])
                    break
            
            if(line[j][i] in ['/']):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] == '/'):
                        A += line[j][i]
                        tokens.append(['DL_OP' , A])
                        i += 1
                        continue
                    else:
                        tokens.append(['DL_OP' , A])
                        continue
            
                except IndexError:
                    tokens.append(['DL_OP' , A])
                    break
            
            if(line[j][i] == '!'):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] == '='):
                        A += line[j][i]
                        tokens.append(['DL_OP' , A])
                        i += 1
                        continue
                    else:
                        tokens.append(['ERROR' , A])
                        continue
            
                except IndexError:
                    tokens.append(['ERROR' , A])
                    break
            
            if(line[j][i] == ':'):
                A = line[j][i]
                i += 1
                try:
                    if(line[j][i] == '='):
                        A += line[j][i]
                        tokens.append(['DL_OP' , A])
                        i += 1
                        continue
                    else:
                        tokens.append(['DL_OP' , A])
                        continue
            
                except IndexError:
                    tokens.append(['DL_OP' , A])
                    break
            
            if(line[j][i] in dl):
                A = line[j][i]
                tokens.append(['DL_OP' , A])
                i += 1
                continue
            
            if(line[j][i] == '\t'):
                A = line[j][i]
                tokens.append(['RS' , 'tab'])
                i += 1
                continue
            
            if(line[j][i] == '\n'):
                A = line[j][i]
                tokens.append(['RS' , 'enter'])
                i += 1
                continue
            
            else:
                A = line[j][i]
                tokens.append(['ERROR' , A])
                i += 1
                continue
            
    ST = {"Symbol Table      " : rs+dl+dl3+dl2+v}
    
    st = pd.DataFrame(ST)
    print(st)
    print(tokens)
    print('')
    
    for tok in tokens:
        if(tok[0] in ['ID' , 'Integer' , 'Real' , 'Word' , 'Char' , 'ERROR' , 'comment_1line' , 'comment_multiline']):
            tok.pop()
        if(tok[0] == 'RS' or tok[0] == 'DL_OP' or tok[0] == 'END'):
            tok[0] = tok[1]
            tok.pop()
    
    with open('C:/Users/asus/Desktop/InputFileFatemeRajabi.py' , "w") as inp:
        for item in tokens:
            inp.write("%s\n" %item)
    inp.close()
  
Scanner('C:/Users/asus/Desktop/TestFileFatemeRajabi.py')

