import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)


def add_millions(number):
    return str(number)+' Millions'


# bond['Box Office'] = bond['Box Office'].apply(add_millions)
# print(bond)


def good_movie(row):
    actor = row[1]
    budget = row[4]
    if actor == 'Sean Connery':
        return 'The best'
    elif actor == 'Roger Moore' and budget > 40:
        return 'Enjoyable'
    else:
        return 'Get Lost!'


bond.apply(good_movie, axis='columns')
