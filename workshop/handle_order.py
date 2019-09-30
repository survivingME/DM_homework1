import pandas as pd

if __name__ == "__main__":
    order = pd.read_csv('order_handled.csv')
    #order = pd.read_csv('order.csv')
    account = pd.read_csv('account_handled.csv')
    symbol_list = [" ", "POJISTNE", "SIPO", "LEASING", "UVER"]

    for index, row in order.iterrows():
        if not len(row['bank_to']) == 2:
            print("bank_to wrong at ", index, " and bank_to=", row['bank_to'])
        '''
        if row['account_id'] not in account['account_id'].to_list():
            print("account_id wrong at ", index, " account_id=", row['account_id'])
            order = order.drop(index)
        if row['amount'] < 0:
            print("amount wrong at ", index)
        if row['k_symbol'] not in symbol_list:
            print("k_symbol wrong at ", index)

    order.to_csv('order_handled.csv', index=False)
    print(order.shape)
    '''

