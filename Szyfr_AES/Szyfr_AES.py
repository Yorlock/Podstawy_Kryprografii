from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util import strxor as XOR
import time
import os
import math
from base64 import b64encode
from base64 import b64decode

BLOCK_SIZE = 16

def encrypt_ecb(name, en_name, show_data = False):
    print('Encrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'wb')
    ecb = AES.new(key, AES.MODE_ECB)
    start = time.time()
    result = ecb.encrypt(pad(data_byte, BLOCK_SIZE))
    end = time.time()
    output_file.write(result)
    file.close()
    output_file.close()
    if show_data:
        print('MODE ECB - encrypted text: \n' + str(result))
        print('MODE ECB - end of encrypted text')
    print('MODE ECB - time to encrypt data: ' + str(end - start) + '\n')

def decrypt_ecb(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    start = time.time()
    result = unpad(ecb.decrypt(data_byte), BLOCK_SIZE).decode('utf-8')
    end = time.time()
    output_file.write(str(result))
    file.close()
    output_file.close()
    if show_data:
        print('MODE ECB - decrypted text: \n' + str(result))
        print('MODE ECB - end of decrypted text')
    print('MODE ECB - time to decrypt data: ' + str(end - start) + '\n')

def encrypt_cbc(name, en_name, show_data = False):
    print('Encrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()
    
    data_byte = pad(data_byte, BLOCK_SIZE)
    output_file = open(en_name, 'wb')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = get_random_bytes(BLOCK_SIZE)
    print('IV: ' + str(IV))
    output_file.write(IV)
    state  = IV
    output_data  = []
    start = time.time()
    for i  in range(0,len(data_byte), BLOCK_SIZE):
        block = data_byte[i:i+BLOCK_SIZE]
        y = ecb.encrypt(XOR.strxor(block, state, None))
        output_data.append(y)
        output_file.write(y)
        state = y
    end = time.time()
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - encrypted text: \n' + str(output_data))
        print('MODE CBC - end of encrypted text')
    print('MODE CBC - time to encrypt data: ' + str(end - start) + '\n')

def decrypt_cbc(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE).decode('utf-8')))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def encrypt_cbc_builded(name, en_name, show_data = False):
    print('Encrypt MODE CBC builded - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'wb')
    IV = get_random_bytes(BLOCK_SIZE)
    cbc = AES.new(key, AES.MODE_CBC, IV)
    print('IV: ' + str(IV))
    start = time.time()
    output_data = IV + cbc.encrypt(pad(data_byte, BLOCK_SIZE))
    end = time.time()
    output_file.write(output_data)
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - encrypted text: \n' + str(output_data))
        print('MODE CBC - end of encrypted text')
    print('MODE CBC - time to encrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_builded(name, en_name, show_data = False):
    print('Decrypt MODE CBC builded - name of file: ' + str(name))
    file = open(name,'rb')
    raw = file.read()

    output_file = open(en_name, 'w')
    cbc = AES.new(key, AES.MODE_CBC, raw[:BLOCK_SIZE])
    start = time.time()
    output_data = unpad(cbc.decrypt(raw[BLOCK_SIZE:]), BLOCK_SIZE).decode('utf-8')
    end = time.time()
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def encrypt_ctr_builded(name, en_name, show_data = False):
    print('Encrypt MODE CTR builded - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'wb')
    ctr = AES.new(key, AES.MODE_CTR)
    start = time.time()
    output_data = ctr.encrypt(pad(data_byte, BLOCK_SIZE))
    print('IV: ' + str(ctr.nonce))
    end = time.time()
    output_file.write(output_data)
    file.close()
    output_file.close()
    if show_data:
        print('MODE CTR - encrypted text: \n' + str(output_data))
        print('MODE CTR - end of encrypted text')
    print('MODE CTR - time to encrypt data: ' + str(end - start) + '\n')
    return ctr.nonce

def decrypt_ctr_builded(name, en_name, nonce, show_data = False):
    print('Decrypt MODE CTR builded - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    ctr = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = time.time()
    output_data = unpad(ctr.decrypt(data_byte), BLOCK_SIZE).decode('utf-8')
    end = time.time()
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def encrypt_ctr(name, en_name, show_data = False):
    print('Encrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    data_byte = pad(data_byte, BLOCK_SIZE)
    IV = get_random_bytes(BLOCK_SIZE)
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE)
    output_file = open(en_name, 'wb')
    ecb = AES.new(key, AES.MODE_ECB)
    keys = []
    start = time.time()
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    end = time.time()
    output_data = IV + XOR.strxor(data_byte, key_string, None)
    output_file.write(output_data)
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - encrypted text: \n' + str(output_data))
        print('MODE CTR - end of encrypted text')
    print('MODE CTR - time to encrypt data: ' + str(end - start) + '\n')

def decrypt_ctr(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    keys = []
    
    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    end = time.time()
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

if __name__=='__main__':

    password = input("Enter password: ")
    hash_obj = SHA256.new(password.encode('utf-8'))
    key = hash_obj.digest()

    encrypt_ecb("tests\ecb_input.txt", "tests\ecb_output.txt", show_data=False)
    decrypt_ecb("tests\ecb_output.txt", "tests\ecb_output_decrypted.txt", show_data=False)

    encrypt_cbc("tests\cbc_input.txt", "tests\cbc_output.txt", show_data=False)
    decrypt_cbc_builded("tests\cbc_output.txt", "tests\cbc_output_decrypted.txt", show_data=False)

    encrypt_cbc_builded("tests\cbc_input_b.txt", "tests\cbc_output_b.txt", show_data=False)
    decrypt_cbc_builded("tests\cbc_output_b.txt", "tests\cbc_output_decrypted_b.txt", show_data=False)

    nonce = encrypt_ctr_builded("tests\ctr_input_b.txt", "tests\ctr_output_b.txt", show_data=False)
    decrypt_ctr_builded("tests\ctr_output_b.txt", "tests\ctr_output_decrypted_b.txt", nonce, show_data=False)

    encrypt_ctr("tests\ctr_input.txt", "tests\ctr_output.txt", show_data=False)
    decrypt_ctr("tests\ctr_output.txt", "tests\ctr_output_decrypted.txt", show_data=False)