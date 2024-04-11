import hashlib
import time

# Define a class for individual block and hashing
class Block:
    def __init__(self, index, timestamp, previous_hash, records):
        '''
        Constructor for the class 'Block'
        index = unique ID of the block
        timestamp = time of when the block was created
        previous_hash = hash of previous block
        records = dictionary of student records
        '''
        self.index = index;
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.records = records
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        # Computes hash of the block.
        block_string = "{}{}{}{}".format(self.index, str(self.records), self.timestamp, self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Define Blockchain class and it methods
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, {}, time.time(), "0")
        self.chain.append(genesis_block)

    def add_new_record(self, record):
        self.last_record = record

    def validate_record(self, record):
        if not isinstance(record['age'], int) or not 18 <= record['age'] <= 60:
            return False
        return True

    def add_block(self, record):
        if not self.validate_record(record):
            return False

        last_block = self.chain[-1]
        new_block = Block(index=last_block.index + 1,
                          records=record,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        self.chain.append(new_block)
        return True 