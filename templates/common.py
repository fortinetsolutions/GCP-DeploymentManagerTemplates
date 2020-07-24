import random
import string


def GenerateRandomString(n):
    '''
    Create a random string for use of a suffix takes int returns string of length int
    '''

    rstring = ''
    for _ in range(4):
        l = random.choice(string.ascii_lowercase)
        rstring = rstring + l

    return rstring


def GenerateMachineName(prefix, suffix):
    return prefix + '-' + suffix
