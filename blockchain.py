from block import Block

# This file defines the class for a Blockchain.

class Blockchain:

    # Initiate a list that will contain all the blocks, initiate a list for any unconfirmed transactions,
    # and create and add the genesis block to to list.
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    # The .genesis_block() method creates the first block in the chain, with a previous hash of 0,
    # and adds it as the first element of the list of blocks.
    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)
        return self.chain


    # The .add_block() method takes a dictionary containing transactions and appends the list of blocks
    # in the blockchain.
    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        # proof = proof_of_work(block)
        self.chain.append(new_block)
        return new_block

    # The .print_blocks() method displays all the blocks currently in the chain.
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    # The .validate_chain() method checks to see if every block in the chain was added in a valid way.
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print("Current hash does not equal generated hash")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print("Previous block's hash got changed")
                return False
        return True


    # The .proof_of_work() method can be used to determine the difficulty of the hash function.
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0"*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
      