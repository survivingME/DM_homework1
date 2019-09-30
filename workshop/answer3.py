import pandas as pd

if __name__ == "__main__":
    district = pd.read_csv('district.csv')
    client = pd.read_csv('client_h_dropped.csv')
    disp = pd.read_csv('disp.csv')
    loan = pd.read_csv('loan_handled.csv')
    district_name = set()

    district_ = district[['district_id', 'district_name']]
    temp = client.join(district_.set_index('district_id'), on='district_id')
    temp = temp.drop(['district_id'], axis=1)

    disp_ = disp[['client_id', 'account_id', 'type']]
    temp = temp.join(disp_.set_index('client_id'), on='client_id')
    temp = temp[temp.columns][temp['type'] == 'OWNER']
    temp = temp.drop(['client_id', 'type'], axis=1)

    loan_ = loan[['account_id', 'amount']]
    loan_join = loan_.join(temp.set_index('account_id'), on='account_id')
    loan_join = loan_join.drop(['account_id'], axis=1)

    for index, row in loan_join.iterrows():
        district_name.add(row['district_name'])

    # loan_sort_by_amount = loan_join.sort_values(by='amount', ascending=False)

    loan_mamount_teen = loan_join[['amount', 'age']][loan_join['age'] < 30]['amount'].mean()
    loan_mamount_mid = loan_join[['amount', 'age']].query('age >= 30 & age < 50')['amount'].mean()
    loan_mamount_old = loan_join[['amount', 'age']][loan_join['age'] >= 50]
    # 163638.40490797546 150638.55238095237 142831.0588235294

    loan_mamount_m = loan_join[['amount', 'age']][loan_join['gender'] == 'm']['amount'].mean()
    loan_mamount_w = loan_join[['amount', 'age']][loan_join['gender'] == 'w']['amount'].mean()
    # 147501.7365269461 155161.37931034484

    '''
    for district in district_name:
        print(district, " mean:", loan_join[['district_name', 'amount']]
        [loan_join['district_name'] == district]['amount'].mean())
    '''
    district_mamount = pd.DataFrame(columns=['district_name', 'amount'])
    for district in district_name:
        district_mamount = district_mamount.append({'district_name': district, 'amount': loan_join[['district_name', 'amount']][loan_join['district_name'] == district]['amount'].mean()}, ignore_index=True)

    district_mamount.to_csv('district_load_mamount.csv', index=False)

