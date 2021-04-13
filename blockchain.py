# 블록체인 리스트를 초기화 한다.
blockchain = []


def get_last_blockchain_value():
    """ 현재 블록체인 리스트의 마지막 값을 반환한다. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ 
    블록체인 리스트에 마지막 통화와 함께 새로운 통화를 추가한다.

    인수: 
        :transaction_amount: 추가될 통화량
        :last_transaction: 마지막으로 추가된 통화 (기본값 [1])

    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ 사용자에게 새로운 통화량을 입력받아 반환한다(부동소수점 숫자). """
    user_input = float(input("Your transaction amount please: "))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # 블록체인 리스트를 콘솔에 출력한다
    for block in blockchain:
        print("Outputting Block")
        print(block)

print("Done!")
