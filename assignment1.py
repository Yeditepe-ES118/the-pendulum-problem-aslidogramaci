import numpy as np
def find_period(L0,L1):
    if L1>L0>0:
        for l in range(L0,L1+1,1):
            g = 9.81 #in m/s^2
            T0 = 2 * np.pi * np.sqrt(L0/g)
            T1 = 2 * np.pi * np.sqrt(L1/g)
            print("Output is %f" %t)
            return (T0,T1)

    