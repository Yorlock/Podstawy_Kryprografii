from decimal import Decimal 
import random

primes = []

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  t = int(n**0.5) 
  h = 5
  while h <= t:
    if n % h == 0: return False
    if n % (h+2) == 0: return False
    h += 6
  return True

def gcd(m,n): 
    if n==0: 
        return m
    else: 
        return gcd(n,m%n)

def RSA():
    p = random.choice(primes)
    q = random.choice(primes)
    while (p==q):
        q = random.choice(primes)
    print(rf"p: {p}, q: {q}")
    n = p*q
    totient = (p-1)*(q-1)
    e = 2
    for k in range(2,totient): 
        if gcd(k,totient)==1:
            e = k
            break
    d = 0
    i = 1
    while(True):
        x = 1 + i*totient
        i += 1
        if x % e == 0: 
            d = int(x/e) 
            break
    return e, n, d

def encryptRSA(e, n, originalTextPath, encryptedTextPath):
    originalTextFile = open(originalTextPath,'r')
    encryptedTextFile = open(encryptedTextPath,'w')
    originalText = list(originalTextFile.read())
    originalTextASCII = []
    for ch in originalText:
        originalTextASCII.append(ord(ch))
    for ch in originalTextASCII:
        encryptedTextFile.write(rf"{str(pow(ch, e) % n)} ")
    originalTextFile.close()
    encryptedTextFile.close()

def decryptRSA(d, n, encryptedTextPath, decryptedTextPath):
    encryptedTextFile = open(encryptedTextPath,'r')
    decryptedTextFile = open(decryptedTextPath,'w')
    encryptedText = encryptedTextFile.read().split()
    encryptedTextASCII = []
    for ch in encryptedText:
        encryptedTextASCII.append(pow(int(ch), d) % n)
    result = ''.join(map(chr, encryptedTextASCII))
    decryptedTextFile.write(str(result))
    encryptedTextFile.close()
    decryptedTextFile.close()

def initRSA(path):
    e, n, d = RSA()
    print(rf"e: {e}, d: {d}, n: {n}")
    encryptRSA(e, n, rf"{path}\original.txt", rf"{path}\encrypted.txt")
    decryptRSA(d, n, rf"{path}\encrypted.txt", rf"{path}\decrypted.txt")

if __name__=='__main__':
    primes = [i for i in range(2, 2000) if (isPrime(i))]
    initRSA(rf"tests\1")
    