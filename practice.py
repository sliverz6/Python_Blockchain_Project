MINING_REWARD = 10

genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Jay"
participants = {"Jay"}


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved - amount_sent


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD
    }
    cloned_transactions = open_transactions[:]
    cloned_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": cloned_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input("Recipient please: ")
    tx_amount = float(input("Transaction amount please: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input
    

def verify_chain():
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("Please choose: ")
    print("1: Add a new transaction value")
    print("2: Mine block to blockchain")
    print("3: Output the blockchain")
    print("4: Show the participants")
    print("5: Check transaction validity")
    print("h: Manipulate the blockchain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("Transaction Added!")
        else:
            print("Invalid transaction!")
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("All transactions are valid!")
        else:
            print("There are invalid transaction!")
    elif user_choice == "h":
        if len(blockchain) > 0:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [{"sender": "Lee", "recipient": "Jay", "amount": 100}]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Invalid choice, please select number from menu.")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain!")
        break
    print("Balance of {}: {:6.2f}".format("Jay", get_balance("Jay")))
else:
    print("User left!")
    
print("Done!")