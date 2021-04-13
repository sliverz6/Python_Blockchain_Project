# 블록체인 리스트를 초기화 한다.
blockchain = []


def get_last_blockchain_value():
    """ 현재 블록체인 리스트의 마지막 값을 반환한다. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ 
    블록체인 리스트에 마지막 트랜잭션 함께 새로운 통화를 추가한다.

    인수: 
        :transaction_amount: 추가될 트랜잭션량
        :last_transaction: 마지막으로 추가된 트랜잭션 (기본값 [1])

    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ 사용자에게 새로운 트랜잭션량을 입력받아 반환한다(부동소수점 숫자). """
    user_input = float(input("Your transaction amount please: "))
    return user_input


def get_user_choice():
    """ 사용자에게 메뉴 선택을 입력받아 반환한다. """
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """ 현재 블록체인 리스트를 콘솔에 출력한다. """
    for block in blockchain:
        print("Outputting Block")
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "q":
        break
    else:
        print("Input was invalid, please pick a vlue from the list!")
    print("Choice registered!")

print("Done!")
