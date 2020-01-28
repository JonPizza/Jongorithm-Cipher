import sys

if not len(sys.argv) >= 3: 
    print(f'Usage:\npython3 {sys.argv[0]} <key file> [<plaintext filenames> ...]')
    exit()