import pandas as pd
import datetime

if __name__=="__main__":
    client = pd.read_csv('client_handled.csv')
    current_date = datetime.date(2000, 1, 1)
    age = []

    for index, row in client.iterrows():
        born_date = datetime.datetime.strptime(row['birth_date'], "%Y-%m-%d")
        temp_age = current_date.year - born_date.year - 1
        if current_date.month >= born_date.month:
            if current_date.day >= born_date.day:
                temp_age += 1
        age.append(temp_age)
    client['age'] = pd.Series(age)
    client = client.drop(['birth_date'], axis=1)
    client.to_csv('client_h_dropped.csv', index=False)