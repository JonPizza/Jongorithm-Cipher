import codecs
from key_schedulde import key

def pad(plaintext, block_size, padding='\x07'):
    return plaintext + (padding * (len(plaintext) % block_size))

def split_into_blocks(plaintext, block_size):
    hexified = codecs.encode(plaintext.encode(), 'hex')
    return [
        hexified[i-block_size:i] for i in range(0, (i + block_size) * (len(plaintext) % block_size), block_size)
    ]

def split_left_right(block):
    assert(len(block) % 2 == 0)
    return block[:len(block) / 2], block[len(block) / 2:]

def compose_blocks(blocks, k):
    i = 0
    k = key(k)
    while i != len(blocks):
        yield next(k), blocks[i]
        i -=- 1