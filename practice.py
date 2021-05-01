from functools import reduce
import hashlib as hl
from collections import OrderedDict

from hash_util import hash_block, hash_string_256

MINING_REWARD = 10

genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
    "proof": 100
}

blockchain = [genesis_block]
open_transactions = []
owner = "Jay"
participants = {"Jay"}


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == "00"


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant] for block in blockchain]
    amount_recieved = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_recieved - amount_sent


def print_blockchain_elements():
    for block in blockchain:
        print("블록 출력")
        print(block)
    else:
        print("-" * 20)


def get_last_transaction_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    # transaction = {
    #     "sender": sender,
    #     "recipient": recipient,
    #     "amount": amount
    # }
    transaction = OrderedDict(
        [("sender", sender), ("recipient", recipient), ("amount", amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    # reward_transaction = {
    #     "sender": "MINING",
    #     "recipient": owner,
    #     "amount": MINING_REWARD,
    # }
    reward_transaction = OrderedDict(
        [("sender", "MINING"), ("recipient", owner), ("amount", MINING_REWARD)])
    cloned_transactions = open_transactions[:]
    cloned_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": cloned_transactions,
        "proof": proof
    }
    blockchain.append(block)
    return True
    

def get_transaction_value():
    tx_recipient = input("받는 사람: ")
    tx_amount = float(input("트랜잭션 수량: "))
    return tx_recipient, tx_amount


def get_user_choice():
    user_choice = input("당신의 선택: ")
    return user_choice


def verify_chain():
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block["transactions"][:-1], block["previous_hash"], block["proof"]):
            print("Proof of work is invalid")
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("메뉴를 선택하세요.")
    print("1: 트랜잭션 추가")
    print("2: 블록 추가")
    print("3: 블록체인 출력")
    print("4: 참여자 목록 출력")
    print("5: 트랜잭션 유효성 검사")
    print("h: 해킹")
    print("q: 종료")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value() 
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("트랜잭션 추가 완료.")
        else:
            print("유효하지 않은 트랜잭션!")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements() 
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("유효한 트랜잭션")
        else:
            print("유효하지 않은 트랜잭션")
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
        print("올바르지 않은 입력입니다. 메뉴의 번호를 선택해주세요.")
    if not verify_chain():
        print("올바르지 않은 블록체인!")
        break
    print("{}의 잔고: {:6.2f}".format("Jay", get_balance("Jay")))
else:
    print("사용자 종료!")

print("프로그램 종료!")
