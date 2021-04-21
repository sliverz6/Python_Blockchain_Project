blockchain = []


def get_last_blockchain_value():
    """ 블록체인의 마지막 값을 반환한다. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_value, last_transaction=[1]):
    """ 블록체인에 트랙잭션 값을 추가한다. 마지막 블록체인의 값도 함께 추가된다. 
    
    매개변수:
        :transaction_value: 블록체인에 추가될 트랙잭션 값
        :last_transaction: 블록체인의 마지막 트랙잭션 값
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_value]) 


def get_transaction_value():
    """ 사용자의 트랙잭션 값을 입력 받아 반환한다. """
    return float(input("트랜잭션 값: "))


def get_user_input():
    """ 사용자의 인터페이스 선택 값을 입력 받아 반환한다. """
    return input("당신의 선택: ")


def print_blockchain_elements():
    """ 블록체인의 모든 블록을 출력한다. """
    for block in blockchain:
        print("블록 출력")
        print(block)


while True:
    print("선택지를 골라주세요.")
    print("1: 블록체인에 트랜잭션 값을 추가한다.")
    print("2: 블록체인의 모든 블록을 출력한다.")
    print("q: 종료")
    user_choice = get_user_input()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "q":
        break
    else:
        print("잘못 입력하셨습니다! 메뉴에 있는 선택지를 골라주세요.")

print("종료!")
