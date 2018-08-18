import math
q = int(raw_input())
def Primest(K):
    N=K*24
    r=bytearray([1])*(N//3);r[0]=0;j=2
    for i in range(int(N**0.5)//3+1):
        if r[i]:
            I=3*i+1|1
            r[((I*I)//3)::2*I]=bytearray([0])*((N//6-(I*I)//6-1)//I+1)
            r[(I*I+4*I-2*I*(i&1))//3::2*I]=bytearray([0])*((N//6-(I*I+4*I-2*I*(i&1))//6-1)//I+1)
    for i, p in enumerate(r):
        if p:
            j += 1
            if j == K:
                print(i*3+1|1)
                break
for i in range(q):
	k = int(raw_input())
	Primest(k)
