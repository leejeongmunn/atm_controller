"""
최소한 다음 흐름을 구현해야 합니다.

카드 삽입 => PIN 번호 => 계정 선택 => 잔액/입금/출금 보기
단순화를 위해 이 세상에는 1달러 지폐만 있고 센트는 없습니다. 따라서 계정 잔액은 정수로 나타낼 수 있습니다.

코드를 실제 은행 시스템과 통합할 필요는 없지만 향후 실제 은행 시스템과 통합할 수 있다는 점을 염두에 두십시오.
ATM의 실제 현금 보관함과 통합할 필요는 없지만 미래에 통합하기를 원한다는 점을 염두에 두십시오.
그리고 그것들과 통합하더라도 우리는 우리의 코드를 테스트하고 싶습니다.
은행 통합 및 현금 보관함 및 카드 리더기와 같은 ATM 하드웨어를 구현하는 것은 이 작업의 범위가 아니지만 컨트롤러 부분(은행 시스템, 현금 보관함 등 제외)을 테스트하는 것은 범위 내에 있습니다.

은행 API는 ATM에 PIN 번호를 제공하지 않지만 PIN 번호가 정확한지 여부는 알려줄 수 있습니다.
작업에 따라 다른 엔지니어가 사용자 인터페이스를 구현할 수 있어야 합니다. REST API, RPC, 네트워크 통신 등을 구현할 필요가 없고 함수/클래스/메서드 등만 구현하면 됩니다.
프로젝트에서 설명할 가치가 없다고 생각되면 복잡한 실제 문제를 단순화할 수 있습니다.
"""
class Card:
    def __init__(self, username, pin_number) -> None:
        self.username = username
        self.pin_number = pin_number

    def is_inserted(self, inserted : bool):
        return inserted

    def check_pin_number(self, pin_number):
        return self.pin_number == pin_number

    def select_account(self, pin_number):
        return self.check_pin_number(self, pin_number)


class BankAccount:
    def __init__(self, card,  balance, pin_number) -> None:
        self.balance = balance
        self.pin_number = pin_number
        self.card = card

    def check_pin_number(self):
        if self.pin_number == self.card.pin_number:
            return True
        return False

    # def is_certificated(self, certificated:bool=False):
    #     return certificated

    def check_balance(self):
        return self.balance

    def deposit(self, money:int):
        self.balance += money
        return self.balance

    def withdraw(self, money:int):
        if self.balance >= money:
            self.balance -= money
            return True
        return False

    def make_deposit(self):
        money = int(input("How much would you like to deposit?  "))
        if money > 0:
            return self.deposit(money=money)
        return False

    def make_withdrawal(self):
        money = int(input("How much would you like to withdraw?  "))
        if self.balance >= money:
            return self.withdraw(money=money)
        print("\nCan't withdraw\n") # 표현 바꾸기
        return

    def exit(self):
        return int(input("""
        Are you sure you want to quit?
        1. Yes
        2. No
        """))



select_menu_msg ="""
Select Option :
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
"""

sample_username = "James"
sample_pin_number = "123456"


def main():
    card = Card(username=sample_username, pin_number=sample_pin_number)
    account = BankAccount(card=card, balance=10000, pin_number=sample_pin_number)

    error_cnt = 0
    while card.is_inserted(True) and error_cnt < 5:
        pin_number = input("Please Input Your PIN Number :  ")
        if card.select_account(pin_number=pin_number) and account.check_pin_number():
            is_certificated = True
            break
        else:
            error_cnt += 1

    if error_cnt == 5:
        print("\nVisit a branch to change your PIN number\n")
        return

    while is_certificated:
        option = int(input(select_menu_msg))
        if option == 4:
            ans = account.exit()
            if ans == 1:
                print("Thank You.")
                break
        elif option == 2:
            account.make_deposit()
            balance = account.check_balance()
            print(f"\nYour balance is {balance} $\n")
        elif option == 3:
            account.make_withdrawal()
            balance = account.check_balance()
            print(f"\nYour balance is {balance} $\n")
        elif option == 1:
            balance = account.check_balance()
            print(f"\nYour balance is {balance} $\n")
        else:
            print("Wrong Option\n")
    card.is_inserted(False)

if __name__ == "__main__":
    main()







