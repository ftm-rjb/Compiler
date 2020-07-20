def Parser(inpt):
    
    Fil = open(inpt , "r")
    lin = Fil.read()
    l1 = list(lin.split("\n"))
    ll = []
    for ani in l1:
        ani = ani[2:-2]
        ll.append(ani)
    ll.pop()
    
    terminals = ['integer' , 'real' , 'word' , 'char' , 'array' , 'until' , 'condition' ,
                 'enter' , 'tab' , 'Integer' , 'Real' , 'Word' , 'Char' , 'ID' , ':=' ,
                 '%' , ',' , '(' , ')' , '+' , '-' , '*' , '/' , '//' , "'" , ':' , '&' ,
                 '|' , '=' , '<' , '>' , '<=' , '>=' , '!=' , 'comment_1line' , 'comment_multiline' , '#']
    
    variables = ['Start' , 'Data' , 'Comput' , 'Comment1' , 'Commentm' , 'Loop' , 'IntId' , 'IntRealId' ,
                 'WordId' , 'CharId' , 'CommentEnter' , 'Array' , 'Array1' , 'Array2' , 'Array3' , 'Array4' , 'Array11' , 'Array22' ,
                 'Array33' , 'Array44' , 'Exp0' , 'Exp00'  , 'Exp01' , 'Exp010' , 'Exp02' , 'Exp020' , 'Exp03' , 'Operator' , 'Conditional' , 'Loop1' , 'ConditionalTerm' , 'ConditionalTerm1' , 'Exp1' , 
                 'AndOr' , 'Operand' , 'ConditionalTerm2' , 'Exp2' , 'Exp22' , 'ConditionalSign' , 'Exp222' , 'Exp2' , 'Exp3' , 'Exp33' , 'InternalTerm' , 'InternalTerm1' ,
                 'InternalTerm2' , 'InternalTerm3' , 'Loop2' , 'Loop3' , 'InternalTerm4' , 'InternalTerm5' , 'InternalTerm6']
    
    Start = [['Data' , 'Start'] , ['Data' , 'Start'] , ['Data' , 'Start'] , ['Data' , 'Start'] , ['Data' , 'Start'] , ['Loop' , 'Start'],
             ['Loop' , 'Start'] , ['enter' , 'Start'] , [] , [] , [] , [] , [] , ['Comput' , 'Start'] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , ['Comment1' , 'Start'] , ['Commentm' , 'Start'] , ['EPS']]
    
    Data = [['integer' , 'ID' , ':=' , 'IntId' , '%' , 'CommentEnter'] , ['real' , 'ID' , ':=' , 'IntRealId' , '%' , 'CommentEnter'] ,
            ['word' , 'ID' , ':=' , 'WordId' , '%' , 'CommentEnter'] , ['char' , 'ID' , ':=' , 'CharId' , '%' , 'CommentEnter'] ,
            ['array' , 'Array'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [],
            [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    IntId = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer'] , [] , [] , [] , ['ID'] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , []]
    
    IntRealId = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer'] , ['Real'] , [] , [] , ['ID'] ,
                 [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                 [] , [] , [] , [] , [] , [] , []]
    
    WordId = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , ['Word'] , [] , ['ID'] ,
              [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
    
    CharId = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , ['Char'] , ['ID'] ,
              [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
            
    CommentEnter = [[] , [] , [] , [] , [] , [] , [] , ['enter'] , [] , [] , [] , [] , [] ,
                    [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                    [] , [] , [] , [] , [] , [] , [] , ['comment_1line' , 'enter'] , [] , []]
    
    Array = [['integer' , 'ID' , 'Array1' , '%' , 'CommentEnter'] , ['real' , 'ID' , 'Array2' , '%' , 'CommentEnter'] ,
             ['word' , 'ID' , 'Array3' , '%' , 'CommentEnter'] , ['char' , 'ID' , 'Array4' , '%' , 'CommentEnter'] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Array1 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
              ['EPS'] , [',' , 'Array11'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
    
    Array2 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
              ['EPS'] , [',' , 'Array22'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
    
    Array3 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
              ['EPS'] , [',' , 'Array33'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
    
    Array4 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
              ['EPS'] , [',' , 'Array44'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , []]
    
    Array11 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer' , 'Array1'] , [] , [] , [] ,
               ['ID' , 'Array1'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
               [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Array22 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer' , 'Array2'] , ['Real' , 'Array2'] , [] , [] ,
               ['ID' , 'Array2'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
               [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Array33 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , ['Word' , 'Array3'] , [] ,
               ['ID' , 'Array3'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
               [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Array44 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , ['Char' , 'Array4'] ,
               ['ID' , 'Array4'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
               [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Comput = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              ['ID' , ':=' , 'Exp0' , '%' , 'CommentEnter'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp0 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp01' , 'Exp00'] , ['Exp01' , 'Exp00'] , [] , [] ,
            ['Exp01' , 'Exp00'] , [] , [] , [] , ['Exp01' , 'Exp00'] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
            [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp00 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             ['EPS'] , [] , [] , ['EPS'] , ['+' , 'Exp01' , 'Exp00'] , ['-' , 'Exp01' , 'Exp00'] , [] , [] , [] , [] ,
             [] , [] ,[] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp01 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp02' , 'Exp010'] , ['Exp02' , 'Exp010'] , [] , [] ,
             ['Exp02' , 'Exp010'] , [] , [] , [] , ['Exp02' , 'Exp010'] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp010 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              ['EPS'] , [] , [] , ['EPS'] , ['EPS'] , ['EPS'] , ['*' , 'Exp02' , 'Exp010'] ,
              ['/' , 'Exp02' , 'Exp010'] , ['//' , 'Exp02' , 'Exp010'] , [] ,
              [] , [] ,[] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp02 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp03' , 'Exp020'] , ['Exp03' , 'Exp020'] , [] , [] ,
             ['Exp03' , 'Exp020'] , [] , [] , [] , ['Exp03' , 'Exp020'] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp020 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
              ['EPS'] , [] , [] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] ,
              ['EPS'] , ['EPS'] , ["'" , 'Exp03' , 'Exp020'] ,
              [] , [] ,[] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp03 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer'] , ['Real'] , [] , [] ,
             ['ID'] , [] , [] , [] , ['(' , 'Exp0' , ')'] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Operand = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Integer'] , ['Real'] , [] , [] ,
               ['ID'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
               [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Operator = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                [] , [] , [] , [] , ['+'] , ['-'] , ['*'] , ['/'] , ['//'] , ["'"] ,
                [] , [] ,[] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Comment1 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                [] , [] , [] , [] , [] , [] , [] , ['comment_1line' , 'enter'] , [] , []]
    
    Commentm = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                [] , [] , [] , [] , [] , [] , [] , [] , ['comment_multiline' , 'enter'] , []]
    
    Conditional = [[] , [] , [] , [] , [] , ['until' , '(' , 'ConditionalTerm' , ')' , ':' , 'CommentEnter'] ,
                   ['condition' , '(' , 'ConditionalTerm' , ')' , ':' , 'CommentEnter'] , [] , [] , [] , [] , [] , [] ,
                   [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                   [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Loop = [[] , [] , [] , [] , [] , ['Conditional' , 'Loop1'] , ['Conditional' , 'Loop1'] , [] , [] ,
            [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
            [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Loop1 = [['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] ,
             ['EPS'] , ['tab' , 'InternalTerm1'] , [] , [] , [] , [] ,
             ['EPS'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , ['EPS'] , ['EPS'] , ['EPS']]
    
    Loop2 = [['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] ,
             ['EPS'] , ['tab' , 'InternalTerm4'] , [] , [] , [] , [] ,
             ['EPS'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , ['EPS'] , ['EPS'] , ['EPS']]
    
    Loop3 = [['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] ,
             ['EPS'] , ['tab' , 'InternalTerm5'] , [] , [] , [] , [] ,
             ['EPS'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , ['EPS'] , ['EPS'] , ['EPS']]
    
    InternalTerm1 = [['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['Conditional' , 'Loop2'],
                     ['Conditional' , 'Loop2'] , ['InternalTerm' , 'Loop1'] , [] , [] , [] , [] , [] , ['InternalTerm' , 'Loop1'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , []]
    
    InternalTerm2 = [['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['Conditional' , 'Loop3'],
                     ['Conditional' , 'Loop3'] , ['InternalTerm' , 'Loop2'] , [] , [] , [] , [] , [] , ['InternalTerm' , 'Loop2'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , []]
    
    InternalTerm3 = [['InternalTerm' , 'Loop3'] , ['InternalTerm' , 'Loop3'] , ['InternalTerm' , 'Loop3'] , ['InternalTerm' , 'Loop3'] , ['InternalTerm' , 'Loop3'] , [],
                     [] , ['InternalTerm' , 'Loop3'] , [] , [] , [] , [] , [] , ['InternalTerm' , 'Loop3'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop3'] , ['InternalTerm' , 'Loop3'] , []]
    
    InternalTerm4 = [['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['Conditional' , 'Loop2'],
                     ['Conditional' , 'Loop2'] , ['InternalTerm' , 'Loop1'] , ['tab' , 'InternalTerm2'] , [] , [] , [] , [] , ['InternalTerm' , 'Loop1'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , []]
    
    InternalTerm5 = [['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , ['Conditional' , 'Loop2'],
                     ['Conditional' , 'Loop2'] , ['InternalTerm' , 'Loop1'] , ['tab' , 'InternalTerm6'] , [] , [] , [] , [] , ['InternalTerm' , 'Loop1'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop1'] , ['InternalTerm' , 'Loop1'] , []]
    
    InternalTerm6 = [['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , ['Conditional' , 'Loop3'],
                     ['Conditional' , 'Loop3'] , ['InternalTerm' , 'Loop2'] , ['tab' , 'InternalTerm3'] , [] , [] , [] , [] , ['InternalTerm' , 'Loop2'] , [] , [] ,
                     [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                     [] , ['InternalTerm' , 'Loop2'] , ['InternalTerm' , 'Loop2'] , []]
    
    ConditionalTerm = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp1'] , ['Exp1'] , [] , [] ,
                       ['Exp1'] , [] , [] , [] , ['(' , 'ConditionalTerm' , ')' , 'ConditionalTerm1'] ,
                       ['Exp1'] , [] , [] , [] , [] , [] , [] , [] , [] ,
                       [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    ConditionalTerm1 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                        [] , [] , [] , [] , [] , ['EPS'] , [] , [] , [] , [] , [] , [] , [] , ['AndOr' , 'ConditionalTerm2'] ,
                        ['AndOr' , 'ConditionalTerm2'] , ['Exp22'] , ['Exp22'] , ['Exp22'] , ['Exp22'] , ['Exp22'] , ['Exp22'] , [] , [] , []]
    
    Exp1 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp2' , 'Exp22'] , ['Exp2' , 'Exp22'] , [] , [] ,
            ['Exp2' , 'Exp22'] , [] , [] , [] , [] , ['EPS'] , [] , [] , [] , [] , [] , [] , [] , [] ,
            [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    AndOr = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , ['&'] ,
             ['|'] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    ConditionalTerm2 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                        [] , [] , [] , [] , ['(' , 'ConditionalTerm' , ')' , 'ConditionalTerm1'] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                        [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp2 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Operand' , 'Exp3'] , ['Operand' , 'Exp3'] , [] , [] ,
            ['Operand' , 'Exp3'] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
            [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp22 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
             [] , [] , [] , ['EPS'] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
             ['ConditionalSign' , 'Exp222'] , ['ConditionalSign' , 'Exp222'] , ['ConditionalSign' , 'Exp222'] ,
             ['ConditionalSign' , 'Exp222'] , ['ConditionalSign' , 'Exp222'] , ['ConditionalSign' , 'Exp222'] , [] , [] , []]
    
    ConditionalSign = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                       [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,[] ,
                       ['='] , ['<'] , ['>'] , ['<='] , ['>='] , ['!='] , [] , [] , []]
    
    Exp222 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Exp2' , 'Exp22'] , ['Exp2' , 'Exp22'] , [] , [] ,
              ['Exp2' , 'Exp22'] , [] , [] , [] , ['(' , 'Exp222' , ')' , 'Exp22'] , [] , [] , [] , [] ,
              [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    Exp3 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
            [] , [] , [] , ['EPS'] , ['Operator' , 'Exp33'] , ['Operator' , 'Exp33'] , ['Operator' , 'Exp33'] , ['Operator' , 'Exp33'] , 
            ['Operator' , 'Exp33'] , ['Operator' , 'Exp33'] , [] , [] ,[] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , ['EPS'] , [] , [] , []]
    
    Exp33 = [[] , [] , [] , [] , [] , [] , [] , [] , [] , ['Operand' , 'Exp3'] , ['Operand' , 'Exp3'] , [] , [] ,
             ['Operand' , 'Exp3'] , [] , [] , [] , ['(' , 'Exp2' , ')' , 'Exp3'] , [] , [] , [] , [] ,
             [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , []]
    
    InternalTerm = [['Data'] , ['Data'] , ['Data'] , ['Data'] , ['Data'] , ['Conditional'],
                    ['Conditional'] , ['enter'] , [] , [] , [] , [] , [] , ['Comput'] , [] , [] ,
                    [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] , [] ,
                    [] , ['Comment1'] , ['Commentm'] , []]
    
    mystack = ['Start']
    i = 0
    while(i<len(ll)):
        q = mystack[len(mystack)-1]
        if(ll[i] == 'ERROR'):
            i += 1
            #print(mystack)
            print('You have a Scanner-Error in token %i'%(i))
            continue
        if(ll[i] == '#' and q == 'Start'):
            #print(mystack)
            print('YES')
            break
        else:
            if(q in terminals):
                if(q == ll[i]):
                    i += 1
                    mystack.pop()
                    #print(mystack)
                    continue
                else:
                    #print(mystack)
                    print('Top of stack is diffrent from token %i'%(i+1))
                    print('NO')
                    break
            if(q in variables):
                w = terminals.index(ll[i])
                ww = vars()[q]
                vv = ww[w]
                if(len(vv) == 0):
                    #print(mystack)
                    print('There is no rule for create token %i'%(i+1))
                    print('NO')
                    break
                if(vv[0] == 'EPS'):
                    #print(mystack)
                    mystack.pop()
                    continue
                else:
                    mystack.pop()
                    j = len(vv)-1
                    while (j > -1):
                        f = vv[j]
                        mystack.append(f)
                        j = j-1
                    #print(mystack)
                    continue
    print(mystack)
Parser('C:/Users/asus/Desktop/InputFileFatemeRajabi.py')