
# ATM Controller

At least the following flow should be implemented:
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

--------
## Class Card
    - It has username, pin_number.
    - Function named is_inserted checks that card is inserted.
    - Function named check_pin_number checks that input pin_number is same with card's pin_number.
    - Function named select_account is choose account by checking pin_number. Card and Bank Account has One to One Relation in my country, so function only checks it's validation.

## Class BankAccount
    - It has balance, pin_number, card.
    - Function named check_pin_number checks that own pin_number is same with card's pin_number.
    - Fuction named check_balance returns account's balance.
    - Fuction named deposit just add a deposit to balance.
    - Fuction named withdraw checks validation of input money, and withdraw.
    - Fuction named exit shows message, if user picks "1", it's end.

## Main Fuction
    1. I made sample card and account.
    2. if card inserted, ATM will start.
    3. First, it checks pin_number is valid. If you make mistake five times, message will be displayed, and program will be end.
    4. If pin_number is valid, you can choose options between Check Balance, Deposit,  Withdraw, Exit.


