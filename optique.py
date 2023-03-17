from monte_carlo import Env, Grand

env = Env (
        N = 500,
        prec = 5
)

A = Grand(150,1,env)
O = Grand(200,1,env)
Ap = Grand(250,1,env)

oa = A-O
oap = Ap-O

fp = oap*oa / (oa-oap)

print(f"f' = {fp}cm")
