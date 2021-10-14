import sys
sys.setrecursionlimit(1000000000)#just for bigger recursion loop.
x = 1

in_res = None
dec_res = None
def eqnSolve(eqn_state,inc_num):

    def solve(eqn:str,increament):
        global x
        global in_res, dec_res
        if eval(eqn) == 0:
            y = x
            return y
        elif eval(eqn) > 0:

            x = x-increament       
            if x == dec_res:
                y = x
                return dec_res
            dec_res = x
            solve(eqn, increament)
        elif eval(eqn) < 0:

            x = x+increament
            #print(x)
            if x == in_res:
                y = x
                return in_res
            else:
                in_res = x
                solve(eqn, increament)
        solve(eqn, increament)
    solve(eqn_state,inc_num)
    
    return x 

print(eqnSolve('x**3+x**2-12',0.001))
