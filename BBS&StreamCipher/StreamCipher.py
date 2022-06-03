import random
from Crypto.Util import strxor as XOR

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

def BBS(name, keyLength, generateRangeMin = 1000, generateRangeMax = 10000):
    #primes = [i for i in range(generateRangeMin, generateRangeMax) if (isPrime(i) and (i % 4 == 3))]
    p = random.choice(primes)
    q = random.choice(primes)
    while (p==q):
        q = random.choice(primes)
    N = p*q
    numbers = [i for i in range(generateRangeMin, generateRangeMax) if (i % p != 0 and i % q != 0)]
    x = random.choice(numbers)
    resultNumbers = []
    for i in range(keyLength):
        if (i==0):
            resultNumbers.append((x*x)%N)
        else:
            resultNumbers.append((resultNumbers[i-1]*resultNumbers[i-1])%N)
    output_file = open(name, 'w')
    data = ""
    for i in range(keyLength):
        helper = resultNumbers[i]%2
        output_file.write(str(helper))
        data += str(helper)
    output_file.close()
    return data

def StreamCipherEncrypt(BBSFile, fileName, cryptedFile):
    file = open(fileName,'rb')
    outputFile = open(cryptedFile,'wb')
    dataText = file.read()
    
    dataTextLength = len(dataText)
    dataKey = bytes(BBS(BBSFile, dataTextLength, 10, 1000000), "utf-8")
    outputFile.write(XOR.strxor(dataText, dataKey))

    file.close()
    outputFile.close()

def StreamCipherDecrypt(BBSFile, cryptedFile, decryptedFile):
    file = open(cryptedFile,'rb')
    BBSfile = open(BBSFile,'rb')
    outputFile = open(decryptedFile,'w')
    dataCryptedText = file.read()
    dataKey = BBSfile.read()

    outputFile.write(str(XOR.strxor(dataCryptedText, dataKey).decode("utf-8")))

    BBSfile.close()
    file.close()
    outputFile.close()

def strxor(a, b):
    result = ''
    for x, y, in zip(a, b):
        result += str(ord(x) ^ ord(y))
    return result

def StreamCipherEncryptToBites(BBSFile, fileName, cryptedFile):
    file = open(fileName,'r')
    outputFile = open(cryptedFile,'w')
    dataText = file.read()

    dataTextToBites = ''.join(format(ord(i), '08b') for i in str(dataText))

    dataKey = BBS(BBSFile, len(dataTextToBites), 10, 1000000)
    data = strxor(dataTextToBites, dataKey)
    outputFile.write(data)

    file.close()
    outputFile.close()

def StreamCipherDecryptToBites(BBSFile, cryptedFile, decryptedFile):
    file = open(cryptedFile,'r')
    BBSfile = open(BBSFile,'r')
    outputFile = open(decryptedFile,'w')
    dataCryptedText = file.read()
    dataKey = BBSfile.read()

    data = strxor(dataCryptedText, dataKey)
    answer = ''
    for i in range(0, len(data), 8):
        binary = data[i:i+8]
        ascii = int(binary, 2)
        answer += chr(ascii)

    outputFile.write(answer)

    BBSfile.close()
    file.close()
    outputFile.close()

if __name__=='__main__':
    primes = [i for i in range(10, 100000) if (isPrime(i) and (i % 4 == 3))]
    #StreamCipherEncrypt("BBS_TEST.txt", "TEXT_TEST.txt", "ENCRYPTED_TEST.txt")
    #StreamCipherDecrypt("BBS_TEST.txt", "ENCRYPTED_TEST.txt", "DECRYPTED_TEST.txt")

    StreamCipherEncryptToBites("BBS_TEST_BITES.txt", "TEXT_TEST.txt", "ENCRYPTED_TEST_BITES.txt")
    StreamCipherDecryptToBites("BBS_TEST_BITES.txt", "ENCRYPTED_TEST_BITES.txt", "DECRYPTED_TEST_BITES.txt")
    