class Account:
    '''
    A class representing details for a bank account object
    '''
    def __init__(self, name: str, amount=0) -> None:
        '''
        Constructor to create initial state of an account object
        :param name: Account's owners name.
        :param amount: Amount in owners account
        '''
        self.__account_name = name
        self.__account_balance = amount

    def deposit(self, amount) -> bool:
        '''
        Method to add money to an account
        :param amount: Amount to be added to account.
        :return: boolean for if the deposit worked or not.
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount) -> bool:
        '''
        Method to take money out of an account
        :param amount: Amount to be withdrawn from account.
        :return: boolean for if the withdrawal was successful or not.
        '''
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Method to access balance of an account
        :return: accounts balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to access name of an account
        :return: name on account
        '''
        return self.__account_name
