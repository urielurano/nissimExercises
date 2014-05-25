def makeNumbers():
    try:
        A = []
        rfile = open('neutrinos.txt','r')
        if rfile:
            for line in rfile:
                if line.find('#') == -1:
                    decl, ra, medAngErr = [float(t) for t in line.split()]
                    A = decl
    except:
        raise
                    

makeNumbers()
