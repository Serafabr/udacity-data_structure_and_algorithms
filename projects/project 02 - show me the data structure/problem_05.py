import hashlib
import time

# Block for the blockchain
class Block:

    def __init__(self, timestamp, data, previous_hash = None, previous_block = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = previous_block
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        # Using SHA256 hash function.
        sha = hashlib.sha256()

        # Apply hash on all the data inside the Block
        hash_str = "{}{}{}{}".format(self.timestamp, self.data, self.previous_hash ,self.previous_block).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
    def __str__(self):
        output = "---- Block ----\n"
        output += "Data: {}\n".format(self.data)
        output += "Hash: {}\n".format(self.hash)
        output += "Time: {}\n".format(self.timestamp)
        output += "Prev. Hash: {}\n".format(self.previous_hash)
        output += "---- Block ----\n"
        
        return output
    

# Blockchain data structure.
# Single Linked List (reversed).
# Instead of keeping track of the head, we'll keep track of the tail.
# It steps backwards. It goes to the previous element, and not to the next.
class Blockchain:
    
    def __init__(self):
        # Keep track of the tail
        self.tail = self._starting_block()
        self.num_elements = 1
    
    # Insert a new block. It'll be the new tail.
    def insert_block(self, data):
        # New block keep track of the prev_hash.
        prev_hash = self.tail.hash
        new_block = Block(time.time(), data, prev_hash, self.tail)
        self.tail = new_block
        self.num_elements += 1
    
    # Last block is the tail
    def get_last_block(self):
        return self.tail
    
    def get_chain_size(self):
        return self.num_elements
    
    # Verify if the blockchain is unspoiled.
    # Returns True if it's alright. Otherwise, returns False.
    def check_blockchain(self):
        block = self.tail
        while block:
            # Check current hash for each block
            current_hash = block.calc_hash()
            if not current_hash == block.hash:
                return False
            
            # Check previous hash:
            if block.previous_block:
                previous_hash = block.previous_block.hash
                if not previous_hash == block.previous_hash:
                    return False
            
            block = block.previous_block
        
        return True
        
    def get_root(self):
        block = self.tail
        # Loop back until root
        while block.previous_block:
            block = block.previous_block
        
        return block
        
    # Genesis Block
    def _starting_block(self):
        return Block(
            time.time(),
            None,
            None
        )
    
    def __str__(self):
        output = ""
        block = self.tail
        while block:
            output += str(block) + "\n"
            block = block.previous_block
        
        return output


def test_case_01():
    # Normal case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    
    blockchain = Blockchain()
    blockchain.insert_block("ABC")
    blockchain.insert_block("Pedro")
    blockchain.insert_block("1010101001001001")
    blockchain.insert_block("Finish")
    
    print(blockchain)
    # Answer:
    # ---- Block ----
    # Data: Finish
    # Hash: 4987163b94aead0da4b7eee4539da9f9d47126be03d98fe250abed67cde73726 (it will change, based on timestamp)
    # Time: 1602364268.7755961 (it will change, based on timestamp) 
    # Prev. Hash: a0e406e3c9e3927f85a337892b1344b3d93ae5bf7e1569a3c63ece99cf079ae6 (it will change, based on timestamp)
    # ---- Block ----

    # ---- Block ----
    # Data: 1010101001001001
    # Hash: a0e406e3c9e3927f85a337892b1344b3d93ae5bf7e1569a3c63ece99cf079ae6 (it will change, based on timestamp)
    # Time: 1602364268.775587 (it will change, based on timestamp)
    # Prev. Hash: 5d8e6201df31da32733d63c73b39cba9819400a1cf6292e072e4acc00aeed21f (it will change, based on timestamp)
    # ---- Block ----

    # ---- Block ----
    # Data: Pedro
    # Hash: 5d8e6201df31da32733d63c73b39cba9819400a1cf6292e072e4acc00aeed21f (it will change, based on timestamp)
    # Time: 1602364268.775576 (it will change, based on timestamp)
    # Prev. Hash: 253ede20ffc018f2e1d1beddaf8a1512d5aef029f3033a04d30502cf2312320d (it will change, based on timestamp)
    # ---- Block ----

    # ---- Block ----
    # Data: ABC
    # Hash: 253ede20ffc018f2e1d1beddaf8a1512d5aef029f3033a04d30502cf2312320d (it will change, based on timestamp)
    # Time: 1602364268.7755609 (it will change, based on timestamp)
    # Prev. Hash: bbec664164ee810b5bfaa62c872f37def4d2ff288f5f4f6d10a74f78c39fed05 (it will change, based on timestamp)
    # ---- Block ----

    # ---- Block ----
    # Data: None
    # Hash: bbec664164ee810b5bfaa62c872f37def4d2ff288f5f4f6d10a74f78c39fed05 (it will change, based on timestamp)
    # Time: 1602364268.775527 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----


    print(blockchain.get_last_block())
    # Answer:
    # ---- Block ----
    # Data: Finish
    # Hash: 4987163b94aead0da4b7eee4539da9f9d47126be03d98fe250abed67cde73726 (it will change, based on timestamp)
    # Time: 1602364268.7755961 (it will change, based on timestamp)
    # Prev. Hash: a0e406e3c9e3927f85a337892b1344b3d93ae5bf7e1569a3c63ece99cf079ae6 (it will change, based on timestamp)
    # ---- Block ----
    
    print(blockchain.get_chain_size())
    # Answer:
    # 5
    
    print(blockchain.get_root())
    # Answer:
    # ---- Block ----
    # Data: None
    # Hash: bbec664164ee810b5bfaa62c872f37def4d2ff288f5f4f6d10a74f78c39fed05 (it will change, based on timestamp)
    # Time: 1602364268.775527 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----
    
    print(blockchain.check_blockchain())
    # Answer
    # True
    
    print('---------------------------------------')

def test_case_02():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("Empty blockchain. Just with starting block (genesis)")
    
    blockchain = Blockchain()
    
    print(blockchain)
    # Answer:
    # ---- Block ----
    # Data: None
    # Hash: f3ce565f8d525955dcd11685aa1435e443f792d3d1b33afec01a3f48312fa2f5 (it will change, based on timestamp)
    # Time: 1602364586.971638 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----


    print(blockchain.get_last_block())
    # Answer:
    # ---- Block ----
    # Data: None
    # Hash: f3ce565f8d525955dcd11685aa1435e443f792d3d1b33afec01a3f48312fa2f5 (it will change, based on timestamp)
    # Time: 1602364586.971638 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----
    
    print(blockchain.get_chain_size())
    # Answer:
    # 1
    
    print(blockchain.get_root())
    # Answer:
    # ---- Block ----
    # Data: None
    # Hash: f3ce565f8d525955dcd11685aa1435e443f792d3d1b33afec01a3f48312fa2f5 (it will change, based on timestamp)
    # Time: 1602364586.971638 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----
    
    print(blockchain.check_blockchain())
    # Answer
    # True
    
    print('---------------------------------------')

def test_case_03():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Large Blockchain")
    
    blockchain = Blockchain()

    n = 10000
    for n in range(n):
        blockchain.insert_block("New block n.: " + str(n))
    
    print(blockchain.get_last_block())
    # Answer:
    # ---- Block ----
    # Data: New block n.: 9999
    # Hash: 675029c4759e7a7ea92b5eb8d80d3360e2dbe0fc0b00fa9b461d1625f0871d11 (it will change, based on timestamp)
    # Time: 1602364830.139104 (it will change, based on timestamp)
    # Prev. Hash: b0838c78c6fa45f6fc13168a0aed92d524497ec0812a5e28153ce6be07dd872a (it will change, based on timestamp)
    # ---- Block ----

    
    print(blockchain.get_chain_size())
    # Answer:
    # 10001

    print(blockchain.get_root())
    # Answer:
    # ---- Block ----
    # Data: None
    # Hash: a59029d18de2c93c81e27c84ae01671def487d88f1de4e76ac198456a7914580 (it will change, based on timestamp)
    # Time: 1602364830.0423412 (it will change, based on timestamp)
    # Prev. Hash: None
    # ---- Block ----

    
    print(blockchain.check_blockchain())
    # Answer
    # True
    
    print('---------------------------------------')

if __name__ == "__main__":
    
    test_case_01()
    test_case_02()
    test_case_03()