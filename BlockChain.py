"""
Block chain for a given set of Transactions!!
Return the last block.
"""

import hashlib


def sha1(text):
    s = hashlib.sha1()
    s.update(text.encode('utf-8'))
    return s.hexdigest()


def getLatestBlock(startBalances, pendingTransactions, blockSize):
    currBlock = 0
    transactions = []
    prev = "0000000000000000000000000000000000000000"
    for idx, trans in enumerate(pendingTransactions):
        if startBalances[trans[0]] >= trans[2]:
            currBlock += 1
            transactions.append(trans)
            startBalances[trans[0]] -= trans[2]
            startBalances[trans[1]] += trans[2]
        if currBlock == blockSize:
            nextHash, nonce = getValidHash(prev, 0, transactions)
            blk = nextHash + ", " + prev + ", " + str(nonce) + ", " + str(transactions)
            currBlock = 0
            transactions = []
            prev = nextHash
    if currBlock != 0:
        nextHash, nonce = getValidHash(prev, 0, transactions)
        blk = nextHash + ", " + prev + ", " + str(nonce) + ", " + str(transactions)

    return blk


def getValidHash(prev, nonce, transactions):
    while True:
        blk = prev + ", " + str(nonce) + ", " + str(transactions)
        hash = sha1(blk)
        if hash[:4] == "0000":
            return hash, nonce
        nonce += 1


print(getLatestBlock([3, 10, 10, 3], [[3, 2, 2], [2, 3, 5], [3, 2, 4], [3, 0, 2], [1, 2, 2]], 2))

