from concurrent.futures import ThreadPoolExecutor
import time
import threading


class Account:
    def __init__(self, ib):
        self.balance = ib
        # self.lock = threading.Lock() # uncomment this to synchronize

    def transaction(self, name, value):
        # with self.lock: # uncomment this to synchronize
            local_balance = self.balance
            print(f'{name} reads the balance as {local_balance}, and is doing calculation')
            time.sleep(1)
            self.balance = local_balance + value
            print(f'{name} updated the balance as {self.balance}')


if __name__ == '__main__':
    ac = Account(50)
    print(f'Initial balance is {ac.balance}')
    transactions = [["A", "B"], [100, 50]]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(ac.transaction, *transactions)
    print(f'Final balance after two transactions is {ac.balance}')