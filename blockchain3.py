# 블록체인을 초기화 합니다.
MINING_REWARD = 10

genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [] 
}
blockchain = [genesis_block]
open_transactions = []
owner = "Jay"
participants = {"Jay"}  # 세트(set)


def hash_block(block):
    """ 해싱한 블록을 반환합니다. 
    
    매개변수:
        :block: 해싱할 블록
    """
    return "-".join([str(block[key]) for key in block])


def print_blockchain_value():
    """ 블록체인의 모든 블록을 출력합니다. """
    for block in blockchain:
        print("블록체인 출력")
        print(block)
    else:
        print("-" * 20)


def get_last_blockchain_value():
    """ 블록체인의 마지막 값을 반환합니다. 값이 없다면 None을 반환합니다. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_balance(participant):
    """잔고를 계산해서 반환합니다. 
    
    매개변수:
        :participant: 잔고 계산을 위한 참여자
    """
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    sent_amount = 0
    for value in tx_sender:
        if len(value) > 0:
            sent_amount += value[0]
    tx_recipient = [[tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant] for block in blockchain]
    received_amount = 0
    for value in tx_recipient:
        if len(value) > 0:
            received_amount += value[0]
    return received_amount - sent_amount


def verify_transaction(transaction):
    """ 유효한 트랙잭션인지 검사합니다. 유효하면 True를 리턴합니다. 

    매개변수:
        :transaction: 트랜잭션
    """
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ 새로운 트랙잭션을 오픈 트랙잭션 리스트에 추가합니다. 
    
    매개변수:
        :sender: 보내는 사람
        :recipient: 받는 사람
        :amount: 거래량
    """
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    if verify_transaction(transaction):
        participants.add(sender)
        participants.add(recipient)
        open_transactions.append(transaction)
        return True
    return False


def mine_block():
    """ 오픈 트랙잭션 리스트를 블록으로 만들어 블록체인에 추가(채굴)합니다. """
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions 
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ 사용자에게 트랜잭션 값을 입력받아 반환합니다. """
    tx_recipient = input("트랙잭션 받는 사람: ")
    tx_amount = float(input("트랜잭션 거래량: "))
    return (tx_recipient, tx_amount)


def get_user_input():
    """ 사용자에게 메뉴 선택 값을 입력받아 반환합니다. """
    user_choice = input("당신의 선택: ")
    return user_choice


def verify_chain():
    """ 블록체인을 검사합니다. 유효하지 않다면 False를, 유효하다면 True를 리턴합니다. """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("블록체인 프로그램!")
    print("원하는 메뉴를 선택하세요.")
    print("1: 트랙잭션 값 추가")
    print("2: 블록체인 채굴")
    print("3: 블록체인 출력")
    print("4: 참여자 목록 출력")
    print("h: 블록 조작")
    print("q: 종료")
    user_choice = get_user_input()
    if user_choice == "1":
        tx_data = get_transaction_value()
        tx_recipient, tx_amount = tx_data
        if add_transaction(tx_recipient, amount=tx_amount):
            print("트랙잭션이 추가되었습니다.")
        else:
            print("트랜잭션 거부!")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_value()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        if len(blockchain) > 0:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": {"sender": owner, "recipient": "Max", "amount": 100} 
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("메뉴에 있는 선택지를 입력하세요!")
    if not verify_chain():
        print("유효하지 않은 블록체인입니다! 시스템 종료.")
        break
    print(get_balance("Jay"))
else:
    print("종료!")
