
def solve(eqn:str,increament):
    
    x = 1
    in_res = None
    dec_res = None
    status = 'running'
    while status != 'done':
        if eval(eqn) == 0:
            y = x
            return (y)
        elif eval(eqn) > 0:

            x = x-increament       
            if x == dec_res:
                y = x
                return (dec_res)
            dec_res = x
            #solve(eqn, increament)
        elif eval(eqn) < 0:

            x = x+increament
            #print(x)
            if x == in_res:
                y = x
                return (in_res)
            else:
                in_res = x
                #solve(eqn, increament)
        


print(solve('x**3+x**2-12',0.00001))
