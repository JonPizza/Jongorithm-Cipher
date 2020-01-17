import keys
import sys

if len(sys.argv) >= 3 and len(sys.argv[1]) == 64: 
    key = sys.argv[1]
else:
    print(f'Usage:\npython3 {sys.argv[0]} <256 bit hex key> <plaintext filename>')
    exit()

xor = {
    '00': '1',
    '01': '0',
    '10': '0',
    '11': '1'
}

def XOR(b1, b2):
    return xor[str(b1) + str(b2)]

def rotate(blocks, key, round):
    pass
