# a sample implementation of the baby step -> giant step algorithm to compute discrete logarithms. 
# it is based on a simple space-time tradeoff
import math
from timeit import default_timer as timer

# h = g^x mod Z
g = 3116701003
h = 1059878588
Z = 3696837919

def calcN(G):
    return math.floor(math.sqrt(G)) + 1


def calcF(N, g, G, Z):
    return pow(g, G - N, Z)


def calcBabySteps(N, g, Z):
    iv = []
    for i in range(0, N):
        if (i == 0):
            iv.append(g ** i % Z)
        else:
            iv.append(iv[i - 1] * g % Z)
    return iv


def calcGiantSteps(N, f, h, iv, Z):
    jv = []
    for j in range(0, N):
        try:
            if(j == 0):
                jv.append((h * f ** j) % Z)
            else:
                jv.append(jv[j - 1] * f % Z)
                i = iv.index(jv[j])
                return i, j      
        except ValueError:
            pass
    return -1, -1


start = timer()   
G = Z - 1
N = calcN(G)

iv = calcBabySteps(N, g, Z)
f = calcF(N, g, G, Z)
i, j = calcGiantSteps(N, f, h, iv, Z)

if(i > 0):
    print("x =", i + j * N)
    print("Solution: ", h, "=", g, "^", i + j * N, "mod", Z)
else:
    print("Could not find a solution.")

end = timer()
print ("Executed in", end - start, "seconds")