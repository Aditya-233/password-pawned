import sys
import requests
import hashlib

def get_respone(hash_chars):
    # hash_chars -> first 5 only..
    url = 'https://api.pwnedpasswords.com/range/' + hash_chars
    response = requests.get(url=url)
    if response.status_code != 200:
        raise RuntimeError("Api not working..")
    
    resp = response.text.splitlines()
    new_dict = {}
    for res in resp:
        password, cnt = res.split(":")
        new_dict[password] = int(cnt)

    return new_dict

def check_if_pawned(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pass[:5], sha1pass[5:]

    password_list = get_respone(head)
    return password_list.get(tail, 0)

def main(args):
    for p in args:
        cnt = check_if_pawned(p)
        print(f'{p} is pawned {cnt} times')

if __name__ == "__main__":
    main(sys.argv[1:])
    
# Usage -> python3 checker.py qwerty abcd abc1234
# Can optimize using threading or directly checking tail while making new_dict
