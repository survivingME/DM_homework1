import pandas as pd

if __name__ == "__main__":
    client = pd.read_csv('client_handled.csv')
    account = pd.read_csv('account_handled.csv')
    disp = pd.read_csv('disp.csv')
    type = ['OWNER', 'DISPONENT']

    for index, row in disp.iterrows():
        if row['client_id'] not in client['client_id'].to_list():
            print("client_id not exist at ", index)
        if row['account_id'] not in account['account_id'].to_list():
            print("account_id not exist at ", index)
        if row['type'] not in type:
            print("type wrong at ", index)
