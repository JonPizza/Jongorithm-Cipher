import hashlib
import conf


def sha512_n_times(k, n):
    for _ in range(n):
        k = hashlib.sha512(k).hexdigest()
    return k

def key(k):
    while True:
        yield sha512_n_times(k, conf.SHA512_KEY_SCHEDULE_ROUNDS)