import pandas as pd

if __name__ == "__main__":

    # client_ = client.join(district_.set_index('district_id'), on='district_id')

    district = pd.read_csv('district.csv')
    card = pd.read_csv('card_handled.csv')
    disp = pd.read_csv('disp.csv')
    client_modi = pd.read_csv('client_h_dropped.csv')

    district_ = district[['district_id', 'district_name']]
    card_ = card[['disp_id', 'type']]
    disp_ = disp[['disp_id', 'client_id']]

    temp_card = card_.join(disp_.set_index('disp_id'), on='disp_id')
    temp_card = temp_card.drop(['disp_id'], axis=1)

    temp_card = temp_card.join(client_modi.set_index('client_id'), on='client_id')
    temp_card = temp_card.drop(['client_id'], axis=1)

    temp_card = temp_card.join(district_.set_index('district_id'), on='district_id')
    temp_card = temp_card.drop(['district_id'], axis=1)

    gb_gender = temp_card[temp_card.columns][temp_card['age'] > 50].groupby(['gender'])
    gb_gender.size()

    gb_district = temp_card[temp_card.columns][temp_card['age'] > 50].groupby(['district_name'])
    gb_district.size()

    gb_type = temp_card[temp_card.columns][temp_card['age'] > 50].groupby(['type'])
    gb_type.size()

    temp_card.to_csv('answer.csv', index=False)

    # client_id, gender, age, district_name, type




