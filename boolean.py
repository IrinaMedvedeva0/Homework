def is_satisfiable(f):
    spt_str = f.translate(str.maketrans("", "", "() ")).split("/\\")  #original string splitted
    ##print(spt_str)
    
    lits = []                                 #extracting list of literals
    for x in f:
         if x in "abcdefghijklmnopqrstuvwxyz":
             lits.append(x)
             
    lits = sorted(set(lits))
    #print(lits)
    

    cnf = []                                                                  
    for orgn_clause in spt_str:                   #convert to cnf
        if "->" in orgn_clause:                          
            orgn_clause = '~' + orgn_clause
            cnf.append(set(orgn_clause.split("->")))
        elif "\/" in orgn_clause:                       
            cnf.append(set(orgn_clause.split("\/")))
        else: 
            cnf.append(set([orgn_clause]))
    ##print(cnf)
    
    
    for l in lits:                   #removing clauses with tautology      
        x = set([l, '~' + l])
        for i in range(len(cnf)):
            if x == cnf[i]:
                del cnf[i]
    #print(cnf)
    
    
    pl = []                      #set of clauses with common literals
    for c in enumerate(cnf):
        if l in c:
            pl.append(c)
            
    nl = []                              #set of clauses with negated literals
    for c in enumerate(cnf):
        if ('~' + l) in c:
            nl.append(c)   
    
    while pl and nl:                           #resolution method 
        if pl[-1] > nl[-1]:
            a, b = pl[-1], nl[-1]
            del pl[-1]
            del nl[-1]
        elif pl[-1] <= nl[-1]:
            a, b = nl[-1], pl[-1]
            del nl[-1]
            del pl[-1]
        resolved = (cnf[a] or cnf[b]) - x
        if not resolved:
            return False
        del cnf[a]
        del cnf[b]
        cnf.append(resolved)
    else:
        return True
    
        
        
f = input()
responce = is_satisfiable(f)
print(responce)
