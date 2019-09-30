import pandas as pd

if __name__ == "__main__":
    card = pd.read_csv('card_handled.csv')
    disp = pd.read_csv('disp.csv')
    type = []

    for index, row in card.iterrows():
        if row['disp_id'] not in disp['disp_id'].to_list():
            print("disp_id wrong at ", index)
        '''
        if row['type'] not in ['classic', 'junior', 'gold']:
            print(index)
            type.append('gold')
        else:
            type.append(row['type'])
    type_s = pd.Series(type)
    card['type'] = type_s
    card.to_csv('card_handled.csv', index=False)
    '''