import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash = None, previous_block = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = previous_block
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()

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
    

class Blockchain:
    
    def __init__(self):
        self.tail = self._starting_block()
        self.num_elements = 1
    
    def insert_block(self, data):
        prev_hash = self.tail.hash
        new_block = Block(time.time(), data, prev_hash, self.tail)
        self.tail = new_block
        self.num_elements += 1
    
    def get_last_block(self):
        return self.tail
    
    def get_chain_size(self):
        return self.num_elements
    
    def check_blockchain(self):
        block = self.tail
        while block:
            # Check current hash
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
        while block.previous_block:
            block = block.previous_block
        
        return block
        
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

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.insert_block("ABC")
    blockchain.insert_block("Pedro")
    blockchain.insert_block("Daiana")
    blockchain.insert_block("1010101001001001")
    blockchain.insert_block("FInish")
    print(blockchain)
    print(blockchain.get_last_block())
    print(blockchain.get_chain_size())
    print(blockchain.get_root())
    print(blockchain.check_blockchain())