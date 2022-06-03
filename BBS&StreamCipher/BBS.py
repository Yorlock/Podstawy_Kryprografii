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

def singleTest(result, keyLength):
    sumOfOnes = sum(result)
    if sumOfOnes < 10275 and sumOfOnes > 9725:
        return True
    print("Number of 1's: " + str(sumOfOnes))
    return False

def seriesTest(result, keyLength):
    series = [0] * 6
    length = 0
    for i in range(keyLength):
        if i == 0:
            last = result[i]
            length += 1
        else:
            if result[i] != last:
                if (result[i] == 1):
                    series[length-1] += 1
                length = 1
                last = result[i]
            else:
                if length < 6:
                    length += 1
    if series[0] >= 2685 or series[0] <= 2315:
        print("String 1:", series[0])
        return False
    if series[1] >= 1386 or series[1] <= 1114:
        print("String 2:", series[1])
        return False
    if series[2] >= 723 or series[2] <= 527:
        print("String 3:", series[2])
        return False
    if series[3] >= 384 or series[3] <= 240:
        print("String 4:", series[3])
        return False
    if series[4] >= 209 or series[4] <= 103:
        print("String 5:", series[4])
        return False
    if series[5] >= 209 or series[5] <= 103:
        print("String 6+:", series[5])
        return False
    return True

def longSeriesTest(result, keyLength):
    length = 0
    for i in range(keyLength):
        if i == 0:
            last = result[i]
            length += 1
        else:
            if result[i] != last:
                if (length > 25):
                    print("Length: " + str(length))
                    return False
                length = 1
                last = result[i]
            else:
                length += 1
    return True

def pokerTest(result, keyLength):
    series = [0] * 16
    for i in range(0,keyLength,4):
        index = result[i]*8+result[i+1]*4+result[i+2]*2+result[i+3]
        series[index] += 1
    seriesSquared = []
    for i in range(16):
        seriesSquared.append(series[i]**2)
    x = 16/5000 * sum(seriesSquared) - 5000
    if x < 2.16 or x > 46.17:
        print("Value: " + str(x))
        return False
    return True

def createFile(name, keyLength, generateRangeMin = 1000, generateRangeMax = 10000):
    primes = [i for i in range(generateRangeMin, generateRangeMax) if (isPrime(i) and (i % 4 == 3))]
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
    for i in range(keyLength):
        helper = resultNumbers[i]%2
        output_file.write(str(helper))

def checkFile(name):
    file = open(name, 'r')
    tmp = file.read()
    keyLength = len(tmp)
    result = []
    #print("File: " + str(name))
    if(keyLength < 20000):
        print("The length is not enough: " + str(keyLength) + " (should be at least 20000)\n")
        return 
    for i in range(20000):
        result.append(int(tmp[i]))
    singleTestRun = singleTest(result, 20000)
    seriesTestRun = seriesTest(result, 20000)
    longSeriesTestRun = longSeriesTest(result, 20000)
    pokerTestRun = pokerTest(result, 20000)
    file.close()
    print("Single test: " + str(singleTestRun))
    print("Series test: " + str(seriesTestRun))
    print("Long series test: " + str(longSeriesTestRun))
    print("Poker test: " + str(pokerTestRun))
    if singleTestRun and seriesTestRun and longSeriesTestRun and pokerTestRun:
        return 1
    return 0

def streamCipherEncrypt():
    print("d")
def streamCipherDecrypt():
    print("d")


if __name__=='__main__':

    createFile("nisttest.txt", 1000000, 10, 10000000)    
    checkFile("nisttest.txt")

    """
    correct = 0
    size = 0
    primes = [i for i in range(10, 1000000) if (isPrime(i) and (i % 4 == 3))]
    for i in range(100): #Correct: 1.0
        createFile("milion2.txt", 20000, 10, 1000000)
        correct += checkFile("milion2.txt")
        size += 1
    print("Correct: " + str(correct/size))
    """
    