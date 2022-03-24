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

def decrypt_ecb_delete_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]
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

def decrypt_ecb_duplicate_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):]

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

def decrypt_ecb_swap_blocks(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte_init = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):BLOCK_SIZE*int(BLOCKS_NUMBER/2)]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2):BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1)]
    data_byte = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2)] + data_byte_a + data_byte_b + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]

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

def decrypt_ecb_add_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + bytes("aekdqoskzmsdqwda", "utf-8") + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]

    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    start = time.time()
    result = unpad(ecb.decrypt(data_byte), BLOCK_SIZE)
    end = time.time()
    output_file.write(str(result))
    file.close()
    output_file.close()
    if show_data:
        print('MODE ECB - decrypted text: \n' + str(result))
        print('MODE ECB - end of decrypted text')
    print('MODE ECB - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ecb_change_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) - 1] + bytes("x", "utf-8") + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]

    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    start = time.time()
    result = unpad(ecb.decrypt(data_byte), BLOCK_SIZE)
    end = time.time()
    output_file.write(str(result))
    file.close()
    output_file.close()
    if show_data:
        print('MODE ECB - decrypted text: \n' + str(result))
        print('MODE ECB - end of decrypted text')
    print('MODE ECB - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ecb_swap_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte_init = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5]

    data_byte = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + data_byte_b + data_byte_a + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5:]


    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    start = time.time()
    result = unpad(ecb.decrypt(data_byte), BLOCK_SIZE)
    end = time.time()
    output_file.write(str(result))
    file.close()
    output_file.close()
    if show_data:
        print('MODE ECB - decrypted text: \n' + str(result))
        print('MODE ECB - end of decrypted text')
    print('MODE ECB - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ecb_delete_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE ECB - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:]

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

def decrypt_cbc_delete_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]
    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_duplicate_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):]
    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_swap_blocks(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    data_byte_init = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):BLOCK_SIZE*int(BLOCKS_NUMBER/2)]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2):BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1)]
    raw = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2)] + data_byte_a + data_byte_b + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]
    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_add_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    state = IV
    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + bytes("aekdqoskzmsdqwda", "utf-8") + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_change_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) - 1] + bytes("x", "utf-8") + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]
    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_swap_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    data_byte_init = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5]

    raw = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + data_byte_b + data_byte_a + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5:]

    state = IV
    output_data = bytes()
    start = time.time()
    for i  in range(0, len(raw), BLOCK_SIZE):  
        block = raw[i:i+BLOCK_SIZE]
        output_data += XOR.strxor(ecb.decrypt(block), state)
        state = block
    end = time.time()
    output_file.write(str(unpad(output_data, BLOCK_SIZE)))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CBC - decrypted text: \n' + str(output_data))
        print('MODE CBC - end of decrypted text')
    print('MODE CBC - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_cbc_delete_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC - name of file: ' + str(name))
    file = open(name,'rb')
    data_input = file.read()
    raw = data_input[BLOCK_SIZE:]
    output_file = open(en_name, 'w')
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_input[:BLOCK_SIZE]
    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:]
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

def decrypt_cbc_builded_delete_block(name, en_name, show_data = False):
    print('Decrypt MODE CBC builded - name of file: ' + str(name))
    file = open(name,'rb')
    raw = file.read()

    BLOCKS_NUMBER = math.ceil(len(raw) / BLOCK_SIZE) - 1
    raw = raw[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + raw[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]

    output_file = open(en_name, 'w')
    cbc = AES.new(key, AES.MODE_CBC, raw[:BLOCK_SIZE])
    start = time.time()
    output_data = unpad(cbc.decrypt(raw[BLOCK_SIZE:]), BLOCK_SIZE)
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

def decrypt_ctr_builded_delete_block(name, en_name, nonce, show_data = False):
    print('Decrypt MODE CTR builded - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]

    output_file = open(en_name, 'w')
    ctr = AES.new(key, AES.MODE_CTR, nonce=nonce)
    start = time.time()
    output_data = ctr.decrypt(data_byte)
    end = time.time()
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

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
    
    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_delete_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]
    BLOCKS_NUMBER -= 1
    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    #output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_duplicate_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):]
    BLOCKS_NUMBER += 1

    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    end = time.time()
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    #output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_swap_blocks(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte_init = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte_init[:BLOCK_SIZE]
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1):BLOCK_SIZE*int(BLOCKS_NUMBER/2)]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2):BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 1)]
    data_byte = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2 - 2)] + data_byte_a + data_byte_b + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]
    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    #output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_add_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + bytes("aekdqoskzmsdqwda", "utf-8") + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]
    BLOCKS_NUMBER += 1

    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    #output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_change_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) - 1] + bytes("x", "utf-8") + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2):]

    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    output_data = unpad(output_data, BLOCK_SIZE)
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_swap_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte_init = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte_init) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte_init[:BLOCK_SIZE]
    
    data_byte_a = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3]
    data_byte_b = data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5]

    data_byte = data_byte_init[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + data_byte_b + data_byte_a + data_byte_init[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 5:]

    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    output_data = unpad(output_data, BLOCK_SIZE)
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def decrypt_ctr_delete_one_byte_in_block(name, en_name, show_data = False):
    print('Decrypt MODE CTR - name of file: ' + str(name))
    file = open(name,'rb')
    data_byte = file.read()

    output_file = open(en_name, 'w')
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    ecb = AES.new(key, AES.MODE_ECB)
    IV = data_byte[:BLOCK_SIZE]
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 1] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2) + 3:]
    start = time.time()
    keys = []
    for i in range(BLOCKS_NUMBER):
        keys.append(ecb.encrypt(int(int.from_bytes(IV, byteorder='big') + i).to_bytes(16, 'big', signed=False)))
    key_string = bytes()
    for i in range(BLOCKS_NUMBER):
        key_string += keys[i]
    output_data = XOR.strxor(key_string, data_byte[BLOCK_SIZE:], None)
    end = time.time()
    output_data = unpad(output_data, BLOCK_SIZE).decode('utf-8')
    output_file.write(str(output_data))
    file.close()
    output_file.close()
    print('IV:' + str(IV))
    if show_data:
        print('MODE CTR - decrypted text: \n' + str(output_data))
        print('MODE CTR - end of decrypted text')
    print('MODE CTR - time to decrypt data: ' + str(end - start) + '\n')

def create_crypted_files():
    #PASSWORD: password
    #ECB
    encrypt_ecb("tests\small\small.txt", "tests\small\small_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\small\small_alphabet.txt", "tests\small\small_alphabet_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\small\small_one.txt", "tests\small\small_one_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\small\small_simple.txt", "tests\small\small_simple_output_ecb.txt", show_data=False)

    encrypt_ecb("tests\medium\medium.txt", "tests\medium\medium_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\medium\medium_alphabet.txt", "tests\medium\medium_alphabet_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\medium\medium_one.txt", "tests\medium\medium_one_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\medium\medium_simple.txt", "tests\medium\medium_simple_output_ecb.txt", show_data=False)

    encrypt_ecb("tests\huge\huge.txt", "tests\huge\huge_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\huge\huge_alphabet.txt", "tests\huge\huge_alphabet_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\huge\huge_one.txt", "tests\huge\huge_one_output_ecb.txt", show_data=False)
    encrypt_ecb("tests\huge\huge_simple.txt", "tests\huge\huge_simple_output_ecb.txt", show_data=False)

    #CBC
    encrypt_cbc("tests\small\small.txt", "tests\small\small_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\small\small_alphabet.txt", "tests\small\small_alphabet_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\small\small_one.txt", "tests\small\small_one_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\small\small_simple.txt", "tests\small\small_simple_output_cbc.txt", show_data=False)

    encrypt_cbc("tests\medium\medium.txt", "tests\medium\medium_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\medium\medium_alphabet.txt", "tests\medium\medium_alphabet_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\medium\medium_one.txt", "tests\medium\medium_one_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\medium\medium_simple.txt", "tests\medium\medium_simple_output_cbc.txt", show_data=False)

    encrypt_cbc("tests\huge\huge.txt", "tests\huge\huge_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\huge\huge_alphabet.txt", "tests\huge\huge_alphabet_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\huge\huge_one.txt", "tests\huge\huge_one_output_cbc.txt", show_data=False)
    encrypt_cbc("tests\huge\huge_simple.txt", "tests\huge\huge_simple_output_cbc.txt", show_data=False)

    #CTR
    encrypt_ctr("tests\small\small.txt", "tests\small\small_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\small\small_alphabet.txt", "tests\small\small_alphabet_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\small\small_one.txt", "tests\small\small_one_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\small\small_simple.txt", "tests\small\small_simple_output_ctr.txt", show_data=False)

    encrypt_ctr("tests\medium\medium.txt", "tests\medium\medium_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\medium\medium_alphabet.txt", "tests\medium\medium_alphabet_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\medium\medium_one.txt", "tests\medium\medium_one_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\medium\medium_simple.txt", "tests\medium\medium_simple_output_ctr.txt", show_data=False)

    encrypt_ctr("tests\huge\huge.txt", "tests\huge\huge_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\huge\huge_alphabet.txt", "tests\huge\huge_alphabet_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\huge\huge_one.txt", "tests\huge\huge_one_output_ctr.txt", show_data=False)
    encrypt_ctr("tests\huge\huge_simple.txt", "tests\huge\huge_simple_output_ctr.txt", show_data=False)

def example_files():

    #encrypt_ecb("examples\ecb_input.txt", "examples\ecb_output.txt", show_data=False)
    #decrypt_ecb("examples\ecb_output.txt", "examples\ecb_output_decrypted.txt", show_data=False)

    encrypt_cbc_builded("examples\cbc_input.txt", "examples\cbc_output.txt", show_data=False)
    decrypt_cbc_builded_delete_block("examples\cbc_output.txt", "examples\cbc_output_decrypted.txt", show_data=False)
    decrypt_cbc_builded("examples\cbc_output.txt", "examples\cbc_output_decrypted_1.txt", show_data=False)

    #encrypt_cbc_builded("examples\cbc_input_b.txt", "examples\cbc_output_b.txt", show_data=False)
    #decrypt_cbc_builded("examples\cbc_output_b.txt", "examples\cbc_output_decrypted_b.txt", show_data=False)

    #nonce = encrypt_ctr_builded("examples\ctr_input_b.txt", "examples\ctr_output_b.txt", show_data=False)
    #decrypt_ctr_builded("examples\ctr_output_b.txt", "examples\ctr_output_decrypted_b.txt", nonce, show_data=False)

    nonce = encrypt_ctr_builded("examples\ctr_input.txt", "examples\ctr_output.txt", show_data=False)
    decrypt_ctr_builded("examples\ctr_output.txt", "examples\ctr_output_decrypted1.txt", nonce, show_data=False)
    decrypt_ctr_builded_delete_block("examples\ctr_output.txt", "examples\ctr_output_decrypted.txt", nonce, show_data=False)

def create_decrypted_files(input_string, output_string, mode_string):
    delete_block = "decrypt_"+mode_string+"_delete_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_delete_block.txt')"
    duplicate_block = "decrypt_"+mode_string+"_duplicate_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_duplicate_block.txt')"
    swap_blocks = "decrypt_"+mode_string+"_swap_blocks('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_swap_blocks.txt')"
    add_block = "decrypt_"+mode_string+"_add_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_add_block.txt')"
    change_one_byte_in_block = "decrypt_"+mode_string+"_change_one_byte_in_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_change_one_byte_in_block.txt')"
    swap_one_byte_in_block = "decrypt_"+mode_string+"_swap_one_byte_in_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_swap_one_byte_in_block.txt')"
    delete_one_byte_in_block = "decrypt_"+mode_string+"_delete_one_byte_in_block('"+input_string+"_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_delete_one_byte_in_block.txt')"

    eval(delete_block)
    eval(duplicate_block)
    eval(swap_blocks)
    eval(add_block)
    eval(change_one_byte_in_block)
    eval(swap_one_byte_in_block)
    # eval(delete_one_byte_in_block) #error

    delete_block = "decrypt_"+mode_string+"_delete_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_delete_block.txt')"
    duplicate_block = "decrypt_"+mode_string+"_duplicate_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_duplicate_block.txt')"
    swap_blocks = "decrypt_"+mode_string+"_swap_blocks('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_swap_blocks.txt')"
    add_block = "decrypt_"+mode_string+"_add_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_add_block.txt')"
    change_one_byte_in_block = "decrypt_"+mode_string+"_change_one_byte_in_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_change_one_byte_in_block.txt')"
    swap_one_byte_in_block = "decrypt_"+mode_string+"_swap_one_byte_in_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_swap_one_byte_in_block.txt')"
    delete_one_byte_in_block = "decrypt_"+mode_string+"_delete_one_byte_in_block('"+input_string+"_alphabet_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_alphabet_delete_one_byte_in_block.txt')"

    eval(delete_block)
    eval(duplicate_block)
    eval(swap_blocks)
    eval(add_block)
    eval(change_one_byte_in_block)
    eval(swap_one_byte_in_block)
    # eval(delete_one_byte_in_block) #error

    delete_block = "decrypt_"+mode_string+"_delete_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_delete_block.txt')"
    duplicate_block = "decrypt_"+mode_string+"_duplicate_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_duplicate_block.txt')"
    swap_blocks = "decrypt_"+mode_string+"_swap_blocks('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_swap_blocks.txt')"
    add_block = "decrypt_"+mode_string+"_add_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_add_block.txt')"
    change_one_byte_in_block = "decrypt_"+mode_string+"_change_one_byte_in_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_change_one_byte_in_block.txt')"
    swap_one_byte_in_block = "decrypt_"+mode_string+"_swap_one_byte_in_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_swap_one_byte_in_block.txt')"
    delete_one_byte_in_block = "decrypt_"+mode_string+"_delete_one_byte_in_block('"+input_string+"_one_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_one_delete_one_byte_in_block.txt')"

    eval(delete_block)
    eval(duplicate_block)
    eval(swap_blocks)
    eval(add_block)
    eval(change_one_byte_in_block)
    eval(swap_one_byte_in_block)
    # eval(delete_one_byte_in_block) #error

    delete_block = "decrypt_"+mode_string+"_delete_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_delete_block.txt')"
    duplicate_block = "decrypt_"+mode_string+"_duplicate_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_duplicate_block.txt')"
    swap_blocks = "decrypt_"+mode_string+"_swap_blocks('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_swap_blocks.txt')"
    add_block = "decrypt_"+mode_string+"_add_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_add_block.txt')"
    change_one_byte_in_block = "decrypt_"+mode_string+"_change_one_byte_in_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_change_one_byte_in_block.txt')"
    swap_one_byte_in_block = "decrypt_"+mode_string+"_swap_one_byte_in_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_swap_one_byte_in_block.txt')"
    delete_one_byte_in_block = "decrypt_"+mode_string+"_delete_one_byte_in_block('"+input_string+"_simple_output_"+mode_string+".txt', '"+output_string+"_"+mode_string+"_simple_delete_one_byte_in_block.txt')"

    eval(delete_block)
    eval(duplicate_block)
    eval(swap_blocks)
    eval(add_block)
    eval(change_one_byte_in_block)
    eval(swap_one_byte_in_block)
    # eval(delete_one_byte_in_block) #error

def create_all_decrypted_files():
    create_decrypted_files("tests\small\small", "tests\small_result\small", "ecb")
    create_decrypted_files("tests\small\small", "tests\small_result\small", "ctr")
    create_decrypted_files("tests\small\small", "tests\small_result\small", "cbc")

    create_decrypted_files("tests\medium\medium", "tests\medium_result\medium", "ecb")
    create_decrypted_files("tests\medium\medium", "tests\medium_result\medium", "ctr")
    create_decrypted_files("tests\medium\medium", "tests\medium_result\medium", "cbc")

    create_decrypted_files("tests\huge\huge", "tests\huge_result\huge", "ecb")
    create_decrypted_files("tests\huge\huge", "tests\huge_result\huge", "ctr")
    create_decrypted_files("tests\huge\huge", "tests\huge_result\huge", "cbc")

if __name__=='__main__':

    # password = input("Enter password: ")
    password = "password"
    hash_obj = SHA256.new(password.encode('utf-8'))
    key = hash_obj.digest()

    file = open("examples\cbc_output.txt",'rb')
    data_byte = file.read()

    print(data_byte)
    BLOCKS_NUMBER = math.ceil(len(data_byte) / BLOCK_SIZE) - 1
    data_byte = data_byte[:BLOCK_SIZE*int(BLOCKS_NUMBER/2)] + data_byte[BLOCK_SIZE*int(BLOCKS_NUMBER/2 + 1):]
    print(data_byte)
    
    #example_files()
    #create_crypted_files()
    #create_all_decrypted_files()
