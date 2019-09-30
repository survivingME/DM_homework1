import pandas as pd

if __name__ == "__main__":
    district = pd.read_csv('district.csv')
    client = pd.read_csv('client_h_dropped.csv')
    disp = pd.read_csv('disp.csv')
    tran = pd.read_csv('trans_handled.csv')
    amount = []
    district_names = set()
    mid = range(30, 50)

    district_ = district[['district_id', 'district_name']]
    temp = client.join(district_.set_index('district_id'), on='district_id')
    temp = temp.drop(['district_id'], axis=1)

    disp_ = disp[['client_id', 'account_id', 'type']]
    temp = temp.join(disp_.set_index('client_id'), on='client_id')
    temp = temp[temp.columns][temp['type'] == 'OWNER']
    temp = temp.drop(['client_id', 'type'], axis=1)

    for index, row in tran.iterrows():
        if row['type'] == 'VYDAJ':
            amount.append(row['amount'])
        else:
            amount.append(row['amount'] * -1)
    amount_s = pd.Series(amount)
    tran['amount'] = amount_s

    tran_join = tran[['account_id', 'amount']]
    tran_join = tran_join.join(temp.set_index('account_id'), on='account_id')

    for index, row in tran_join.iterrows():
        district_names.add(row['district_name'])

    tran_join_teen = tran_join[['account_id', 'amount', 'age']][tran_join['age'] < 30]
    tran_join_old = tran_join[['account_id', 'amount', 'age']][tran_join['age'] >= 50]
    tran_join_mid = tran_join[['account_id', 'amount', 'age']].query('age >= 30 & age < 50')

    # abs_out gby age detail
    abs_out_de_teen = tran_join_teen.groupby(['age', 'account_id']).sum()
    abs_out_de_mid = tran_join_mid.groupby(['age', 'account_id']).sum()
    abs_out_de_old = tran_join_old.groupby(['age', 'account_id']).sum()

    abs_out_de_teen.to_csv('abs_out_de_teen.csv')

    # abs_out gby age mean
    abs_out_mean_teen = abs_out_de_teen.mean()
    abs_out_mean_mid = abs_out_de_mid.mean()
    abs_out_mean_old = abs_out_de_old.mean()

    print("abs_out group by age teen mean: ", abs_out_mean_teen)
    print("abs_out group by age mid mean: ", abs_out_mean_mid)
    print("abs_out group by age old mean: ", abs_out_mean_old)

    # abs_out gby gender detail
    abs_out_de_gender = tran_join[['account_id', 'amount', 'gender']].groupby(['gender', 'account_id']).sum()

    # abs_out gby gender mean
    abs_out_mean_gm = tran_join[['account_id', 'amount', 'gender']][tran_join['gender'] == 'm'].groupby(
        ['gender', 'account_id']).sum().mean()
    abs_out_mean_gw = tran_join[['account_id', 'amount', 'gender']][tran_join['gender'] == 'w'].groupby(
        ['gender', 'account_id']).sum().mean()

    print("abs_out group by gender man mean: ", abs_out_mean_gm)
    print("abs_out group by gender woman mean: ", abs_out_mean_gw)
    # abs_out gby district detail
    abs_out_de_district = tran_join[['account_id', 'amount', 'district_name']].groupby(
        ['district_name', 'account_id']).sum()

    # abs_out gby district mean
    for district_name in district_names:
        print("District ", district_name, " mean: ", tran_join[['account_id', 'amount', 'district_name']]
        [tran_join['district_name'] == district_name].groupby(['district_name', 'account_id']).sum().mean())



