import random

test_UID = ['22,10,134,118', '134,22,10,118']
def getCard(UID):
    return UID[random.randint(0, 2)]

def Card():
    return getCard(test_UID)
