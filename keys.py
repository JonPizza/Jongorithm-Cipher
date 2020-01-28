import random
import binascii

key_chars = '0123456789abcdef'

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}

bin_to_hex = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'a',
    '1011': 'b',
    '1100': 'c',
    '1101': 'd',
    '1110': 'e',
    '1111': 'f',
}

def hex_to_bin(h):
    return ''.join([hex_to_bin[c] for c in h])

def bin_to_hex(b):
    b = [line[i:i+4] for i in range(0, len(b), 4)]
    return ''.join([bin_to_hex(s) for s in b])

def read_keyfile(filename):
    try:
	    return open(filename).read()
    except FileNotFoundError:
        print(f'Cannot find keyfile "{filename}"')

def export_key_to_keyfile(key, filename):
	return open(filename, 'w').write(key)

def key_to_bitstream(key):
	return binascii.unhexlify(key)
