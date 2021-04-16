# 블록체인 리스트를 초기화 한다.
genesis_block = {
    "previous_hash": "", 
    "index": 0, 
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "Jay"


def get_last_blockchain_value():
    """ 현재 블록체인 리스트의 마지막 값을 반환한다. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ 
    블록체인 리스트에 마지막 트랜잭션 함께 새로운 통화를 추가한다.

    인수: 
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = "-".join([str(last_block[key]) for key in last_block])
    print(hashed_block)

    block = {
        "previous_hash": hashed_block, 
        "index": len(blockchain), 
        "transactions": open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ 사용자에게 새로운 트랜잭션량을 입력받아 반환한다(부동소수점 숫자). """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    """ 사용자에게 메뉴 선택을 입력받아 반환한다. """
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """ 현재 블록체인 리스트를 콘솔에 출력한다. """
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    """ 블록체인을 검사하여 유효하면 True를, 그렇지 않으면 False를 반환한다. """
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data[0], tx_data[1]
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        mine_block()
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print("Invalid blockchain!")
    #     break
else:
    print("User left!")


print("Done!")
