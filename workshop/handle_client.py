import pandas as pd
import datetime

if __name__ == "__main__":
    client = pd.read_csv('client_fix.csv')
    birth_date = []
    gender = []
    '''
    client_drop = client
    drop_list = [4240, 1, 665, 785, 2037, 4239]
    for drop in drop_list:
        client_drop = client_drop.drop(drop)
    month_map = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    '''
    for index, row in client.iterrows():
        year = int("19" + str(row['birth_number'])[:2])
        if str(row['birth_number'])[2:4] >= '50':
            month = int(str(row['birth_number'])[2:4]) - 50
            gender.append('w')
            #month_map[int(row['birth_number'][2:4]) - 50] += 1
        else:
            month = int(str(row['birth_number'])[2:4])
            gender.append('m')
            #month_map[int(row['birth_number'][2:4])] += 1
        day = int(str(row['birth_number'])[-2:])
    #print(month_map)
        try:
            date = datetime.datetime(year, month, day)
            birth_date.append(date.strftime("%Y-%m-%d"))
        except Exception as e:
            print("birth_number wrong at ", index, " because of ", e)

    birth_date_s = pd.Series(birth_date)
    gender_s = pd.Series(gender)

    client['birth_date'] = birth_date_s
    client['gender'] = gender_s
    client = client.drop(['birth_number'], axis=1)

    client.to_csv('client_handled.csv', index=False)