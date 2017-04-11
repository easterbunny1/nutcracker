import sys
import requests


def guess_code(code):
    """ Send a request to the remote server guessing
        the code passed in. """
    rsp = requests.get('http://localhost:8000/keypad/code/green/%d/' % code)
    if rsp.status_code == 200:
        return True
    return False


def try_all_codes(start, finish):
    """ Try all the codes between start and finish """


if __name__ == '__main__':
    try_all_codes(0, 10)
