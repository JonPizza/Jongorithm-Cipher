import random
import binascii

key_chars = '0123456789abcdef'

def generate_key():
	return ''.join([random.choice(key_chars) for _ in range(64)])

def read_keyfile(filename):
	return open(filename).read()

def export_key_to_keyfile(key, filename):
	return open(filename, 'w').write(key)

def key_to_bitstream(key):
	return binascii.unhexlify(key)
