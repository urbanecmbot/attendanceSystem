import random

test_UID = ['22,10,134,118', '134,22,10,118']
def getCard(UID):
    return UID[random.randint(0, 1)]

def Card():
    card_id = getCard(test_UID)
    card_id = card_id.replace(',','')
    print card_id
    return card_id


