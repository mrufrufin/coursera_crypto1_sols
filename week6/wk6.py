import gmpy2 as g2
from gmpy2 import mpz

def ceil_sqrt(x):
    sq,rm = g2.isqrt_rem(x)
    return sq + (1 if rm else 0)


N1 = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')

N2 = mpz('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')

N3 = mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')

ct4 = mpz('22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540')
#problem 1
A1 = ceil_sqrt(N1)
x1, rem1 = g2.isqrt_rem(g2.sub(g2.mul(A1, A1),N1))
p1 = g2.sub(A1,x1)
q1 = g2.add(A1,x1)
print(p1)

#problem 2, A-sqrt(N) < 2**20 => A < 2**20 + sqrt(N)
N2sq = g2.isqrt(N2)
uplim = 2**20
for i in range(1,2**20):
    A2 = g2.add(N2sq,i)
    x2 = g2.isqrt(g2.sub(g2.mul(A2, A2),N2))
    p2 = g2.sub(A2,x2)
    q2 = g2.add(A2,x2)
    res2 = g2.mul(p2,q2)
    if res2 == N2:
        break
    
print(p2)

#problem 3
'''
let A = (3p+2q)/2, A is not an int (3p is odd, 2q is even so the sum is odd)
so 2A = (6p+4q)/2 is an int, then 2A is between 6p and 4q and 6p = 2A-x and 4q = 2A+x for some x =>
p = (2A-x)/6 and q = (2A+x)/4
Since N=pq = (2A-x)(2A+x)/24 => 24N = 4A^2 - x^2 => sqrt(4A^2-24N) = x => sqrt((2A-sqrt(24N))^2) = x
'''
twofourN3 = g2.mul(24,N3)
twoA3 = ceil_sqrt(twofourN3)
x3, rem3 = g2.isqrt_rem(g2.sub(g2.mul(twoA3,twoA3),twofourN3))
p3 = g2.div(g2.sub(twoA3,x3),6)
print(p3)

#problem 4
phiN4 = g2.add(g2.sub(g2.sub(N1, p1),q1), 1)
e4 = mpz('65537')
d4 = g2.divm(1,e4,phiN4)
pkcs = g2.powmod(ct4, d4, N1)
print(str(hex(pkcs)).split('00')[1].decode('hex'))
