import pandas as pd

if __name__ == "__main__":
    account = pd.read_csv('account.csv')
    id = []
    frequency = []
    district_id = []
    account = account.drop_duplicates()
    for index, row in account.iterrows():
        try:
            int(row['account_id'])
            id.append(row['account_id'])
        except Exception as e:
            print("account_id at ", index, " because of ", e)
            id.append(row['account_id'][:row['account_id'].find("_")])
        if row['frequency'] not in ['POPLATEK MESICNE', 'POPLATEK TYDNE', 'POPLATEK PO OBRATU']:
            print("frequency wrong at ", index)
            frequency.append('POPLATEK MESICNE')
        else:
            frequency.append(row['frequency'])

    id_s = pd.Series(id)
    frequency_s = pd.Series(frequency)
    account['account_id'] = id_s
    account['frequency'] = frequency_s
    account.to_csv('account_handled.csv', index=False)
