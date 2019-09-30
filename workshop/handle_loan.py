import pandas as pd

if __name__ =="__main__":
    loan = pd.read_csv('loan.csv')
    account = pd.read_csv('account_handled.csv')
    status = ['A', 'B', 'C', 'D']
    duration = []
    for index, row in loan.iterrows():
        if row['account_id'] not in account['account_id'].to_list():
            #loan = loan.drop(index)
            print("account_id wrong at ", index, " and account_id=", row['account_id'])
        if row['amount'] < 0:
            print("amount wrong at ", index, " and amount=", row['amount'])
        if row['duration'] % 12 != 0 | row['duration'] < 12:
            print("duration wrong at ", index, " and duration=", row['duration'])
        if row['duration'] * row['payments'] != row['amount']:
            print("payments wrong at ", index, " and payments=", row['payments'])
        if row['status'] not in status:
            print("status wrong at ", index, " and status=", row['status'])
        if row['payduration'] > row['duration'] | row['payduration'] < 0:
            print("payduration wrong at ", index, " and payduraion=", row['payduration'], " and duration=", row['duration'])