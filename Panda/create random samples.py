import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

# Returns single row randomly
data = bond.sample()

# Returns 10 rows randomly
data = bond.sample(n=10)

# Returns 25% rows randomly
data = bond.sample(frac=0.25)

# Returns 2 columns randomly
data = bond.sample(n=2, axis=1)
