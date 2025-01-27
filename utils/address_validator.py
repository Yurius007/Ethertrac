import re

def is_address(address):
    regex = r'^(0x)?[0-9a-fA-F]{40}$'
    return bool(re.match(regex, address))

if __name__ == '__main__':
    print(is_address())

