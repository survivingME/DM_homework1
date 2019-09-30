import pandas as pd

if __name__ == "__main__":
    trans = pd.read_csv('trans.csv')
    account = pd.read_csv('account_handled.csv')
    type = ['VYDAJ', 'PRIJEM']
    operation = ['VYBER KARTOU', 'VKLAD', 'VYBER', 'PREVOD NA UCET', 'PREVOD Z UCTU']
    symbol = ['POJISTNE', 'SLUZBY', 'UROK', 'SANKC. UROK', 'SIPO', 'DUCHOD', 'UVER', ' ']
    for index, row in trans.iterrows():
        if row['account_id'] not in account['account_id'].to_list():
            trans = trans.drop(index)
            print("account_id wrong at ", index, " and account_id=", row['account_id'])
        if row['type'] not in type:
            print("type wrong at ", index, " and type=", row['type'])
        if row['operation'] not in operation:
            print("operation wrong at ", index, " and operation=", row['operation'])
        try:
            int(row['balance'])
        except Exception as e:
            trans = trans.drop(index)
            print("balance wrong at ", index, " and balance=", row['balance'])
        if row['k_symbol'] not in symbol:
            print("symbol wrong at ", index, " and symbol=", row['k_symbol'])
    trans.to_csv('trans_handled.csv', index=False)
    '''
        try:
            if not len(row['bank']) == 2:
                print("bank wrong at ", index, " and bank=", row['bank'])
        except Exception as e:
            print("bank wrong at ", index, " and bank=", row['bank'])
    '''

