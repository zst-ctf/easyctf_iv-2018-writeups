#!/usr/bin/env sage
import sys
import os
from queue import Queue
import threading
from sage.doctest.util import Timer

debug = False

# display matrix picture with 0 and X
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print a

# https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/coppersmith.sage
def coppersmith(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    #
    # init
    #
    dd = pol.degree()
    nn = dd * mm + tt

    #
    # checks
    #
    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    #
    # calculate bounds and display them
    #
    """
    * we want to find g(x) such that ||g(xX)|| <= b^m / sqrt(n)
    * we know LLL will give us a short vector v such that:
    ||v|| <= 2^((n - 1)/4) * det(L)^(1/n)
    * we will use that vector as a coefficient vector for our g(x)
    
    * so we want to satisfy:
    2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)
    
    so we can obtain ||v|| < N^(beta*m) / sqrt(n) <= b^m / sqrt(n)
    (it's important to use N because we might not know b)
    """
    if debug:
        # t optimized?
        print "\n# Optimized t?\n"
        print "we want X^(n-1) < N^(beta*m) so that each vector is helpful"
        cond1 = RR(XX^(nn-1))
        print "* X^(n-1) = ", cond1
        cond2 = pow(modulus, beta*mm)
        print "* N^(beta*m) = ", cond2
        print "* X^(n-1) < N^(beta*m) \n-> GOOD" if cond1 < cond2 else "* X^(n-1) >= N^(beta*m) \n-> NOT GOOD"
        
        # bound for X
        print "\n# X bound respected?\n"
        print "we want X <= N^(((2*beta*m)/(n-1)) - ((delta*m*(m+1))/(n*(n-1)))) / 2 = M"
        print "* X =", XX
        cond2 = RR(modulus^(((2*beta*mm)/(nn-1)) - ((dd*mm*(mm+1))/(nn*(nn-1)))) / 2)
        print "* M =", cond2
        print "* X <= M \n-> GOOD" if XX <= cond2 else "* X > M \n-> NOT GOOD"

        # solution possible?
        print "\n# Solutions possible?\n"
        detL = RR(modulus^(dd * mm * (mm + 1) / 2) * XX^(nn * (nn - 1) / 2))
        print "we can find a solution if 2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)"
        cond1 = RR(2^((nn - 1)/4) * detL^(1/nn))
        print "* 2^((n - 1)/4) * det(L)^(1/n) = ", cond1
        cond2 = RR(modulus^(beta*mm) / sqrt(nn))
        print "* N^(beta*m) / sqrt(n) = ", cond2
        print "* 2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n) \n-> SOLUTION WILL BE FOUND" if cond1 < cond2 else "* 2^((n - 1)/4) * det(L)^(1/n) >= N^(beta*m) / sqroot(n) \n-> NO SOLUTIONS MIGHT BE FOUND (but we never know)"

        # warning about X
        print "\n# Note that no solutions will be found _for sure_ if you don't respect:\n* |root| < X \n* b >= modulus^beta\n"
    
    #
    # Coppersmith revisited algo for univariate
    #

    # change ring of pol and x
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # display basis matrix
    if debug:
        matrix_overview(BB, modulus^mm)

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    if debug: print "potential roots:", potential_roots

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    # 
    return roots

def coppersmith_strip(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    #
    # init
    #
    dd = pol.degree()
    nn = dd * mm + tt

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    # Coppersmith revisited algo for univariate
    #

    # change ring of pol and x
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))
    # 
    return roots

ms = {512: 5, 1024: 4, 2048: 6}
ts = {512: 6, 1024: 5, 2048: 7}
ords = {512: [(2,4), (3,4), (5,2), (7,1), (11,1), (13,1), (17,1), (23,1), (29,1), (37,1), (41,1), (53,1), (83,1)]}
MMs = {512: 0x55eb8fbb4ca1e1879d77}

def Ms(nb):
    l = 0
    if 512 <= nb <= 960:
        # added 5 otherwise gen too small
        l = 39 + 5
    elif 992 <= nb <= 1952:
        l = 71
    elif 1984 <= nb <= 3936:
        l = 126
    else:
        assert(False)
    return reduce(lambda x,y: x*y, Primes()[:l], 1)

def test(n):
    M = Ms(n.nbits())
    g = Mod(65537, M)
    N = Mod(n, M)
    try:
        discrete_log(N, g)
        return True
    except:
        return False

def gen(nb):
    M = Ms(nb*2) # maybe they meant key size
    # consider doing rand in [0,ord-1]
    found = False
    while not found:
        a = randrange(M)
        k = randrange(M)
        x = k*M + pow(65537,a,M)

        found = Integer(x).nbits() == nb and is_pseudoprime(x)
    return x

current_a = 0
def update():
    threading.Timer(5, update).start ()
    global current_a
    sys.stdout.write("\ra =" + str(current_a))
    sys.stdout.flush()

def roca(N, nbits):
    M = MMs[nbits]
    m = ms[nbits]
    t = ts[nbits]
    c = discrete_log(Mod(N, M), Mod(65537, M))
    order = Mod(65537, M).order()
    
    print('c', c)
    print('order', order)
    
    start = Integer(int(c/2))
    end = Integer(int(floor((c+order)/2 + 1)))
    print("Trying a from %d to %d" % (start, end))

    try:
        P.<x> = PolynomialRing(Zmod(N))
        gcd_MN = xgcd(M,N)[1]

        update()
        global current_a
        B = 0.5
        for a in IntegerRange(start, end):
            pow_eaM = power_mod(65537, a, M) #Integer(pow(65537,a,M))
            f = x + gcd_MN*pow_eaM
            # k = f.small_roots() # optimization is fo pussies
            X = 2 * (N**B) / M
            k = coppersmith_strip(f, N, B, m, t, X)
            
            if len(k) > 0:
                p = k[0]*M + pow_eaM
                if N%p == 0:
                    print(p, N/p)
                    quit()
            current_a = a
    except KeyboardInterrupt:
        print("\n\nStopped at a = %d" % (a,))


#p = 67794864987998009138082909338101822501607625820941046889559919233556019996657
#q = 105012597964653179720303739126733078595060162964369519808507808822011788988403


if __name__ == '__main__':
    n = int(open('n.txt').read())
    #n = p*q
    roca(n, 512)
