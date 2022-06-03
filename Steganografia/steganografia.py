import random
from Crypto.Util import strxor as XOR
import skimage.io as io
from math import floor

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

def strxor(a, b):
    result = ''
    for x, y, in zip(a, b):
        result += str(ord(x) ^ ord(y))
    return result

def StreamCipherEncrypt(BBSFile, fileName, cryptedFile):
    file = open(fileName,'r')
    outputFile = open(cryptedFile,'w')
    dataText = file.read()

    dataTextToBites = ''.join(format(ord(i), '08b') for i in str(dataText))

    dataKey = BBS(BBSFile, len(dataTextToBites), 10, 1000000)
    data = strxor(dataTextToBites, dataKey)
    outputFile.write(data)

    file.close()
    outputFile.close()

def StreamCipherDecrypt(BBSFile, cryptedFile, decryptedFile):
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

    outputFile.write(str(answer.encode('utf-8')))

    BBSfile.close()
    file.close()
    outputFile.close()

def HideTextToPhoto(textToHideFile, photoFile, hideTextInPhotoFile, sizeOfTextFile):
    fileToRead = open(textToHideFile,'r')
    secretText = fileToRead.read()
    fileToRead.close()
    textSizeFile = open(sizeOfTextFile, "w")

    img = io.imread(photoFile)
    h, w, _ = img.shape
    maxSizeOfSecretText = int(floor(h * w * 3))
    secretTextSize = len(secretText)
    if secretTextSize > maxSizeOfSecretText:
        print(f"Text is too large {secretTextSize}. Max size is {maxSizeOfSecretText}. Cutting text")
        secretText = secretText[:maxSizeOfSecretText]

    index = 0
    for i in range(h):
        for j in range(w):
            for k in range(3):
                if index < secretTextSize:
                    img[i][j][k] &= 254
                    img[i][j][k] += int(secretText[index])
                    index += 1
                else:
                    io.imsave(hideTextInPhotoFile, img)
                    textSizeFile.write(str(secretTextSize))
                    textSizeFile.close()
                    return
    io.imsave(hideTextInPhotoFile, img)
    textSizeFile.write(str(secretTextSize))
    textSizeFile.close()
    return

def FoundingTextInPhoto(img, h, w, size):
    found = 0
    foundText = ''
    for i in range(h):
        for j in range(w):
            for k in range(3):
                add = str(img[i][j][k] % 2)
                foundText += add
                found += 1
                if found == size:
                    return foundText

def SeekTextToPhoto(foundTextFile, photoFile, sizeOfTextFile):
    sizeOfText = open(sizeOfTextFile, "r")
    size = int(sizeOfText.read())
    sizeOfText.close()
    fileToWrite = open(foundTextFile,'wb')
    img = io.imread(photoFile)
    h, w, _ = img.shape
    foundTextInBin = FoundingTextInPhoto(img, h, w, size)
    fileToWrite.write(bytes(foundTextInBin, 'utf-8'))
    fileToWrite.close()

def TestDataPNG(number):
    StreamCipherEncrypt(rf"files\{number}\BBS.txt", rf"files\{number}\TEXT.txt", rf"files\{number}\ENCRYPTED_TEXT.txt")
    HideTextToPhoto(rf"files\{number}\ENCRYPTED_TEXT.txt", rf"files\{number}\original.png", rf"files\{number}\hidden.png", rf"files\{number}\size.txt")

    SeekTextToPhoto(rf"files\{number}\TEXT_FOUND.txt", rf"files\{number}\hidden.png", rf"files\{number}\size.txt")
    StreamCipherDecrypt(rf"files\{number}\BBS.txt", rf"files\{number}\TEXT_FOUND.txt", rf"files\{number}\DECRYPTED_TEXT.txt")


if __name__=='__main__':
    primes = [i for i in range(10, 100000) if (isPrime(i) and (i % 4 == 3))]
    TestDataPNG(1)
    TestDataPNG(2)
    TestDataPNG(3)