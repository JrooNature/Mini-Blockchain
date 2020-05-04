from blockchain import Blockchain

# Create a few individual transactions
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# Initialize a blockchain object and display the chain containing just the geneisis block
local_blockchain = Blockchain()
local_blockchain.print_blocks()
print('---------------------------')

# Add transactions to the blockchain the valid way, then display the blockchain.
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.validate_chain()
print("----------------------------")

# Add a transaction to the blockchain the invalid way, and show that the transaction is not valid.
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
