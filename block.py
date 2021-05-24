from time import time

from printable import Printable

class Block(Printable):
    def __init__(self, index, previous_hash, tranasctions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if timestamp is None else timestamp
        self.transactions = tranasctions
        self.proof = proof
