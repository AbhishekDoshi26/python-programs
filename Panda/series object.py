import pandas as pd
subjects = ['TOC', 'AJ', 'WT', 'SE', 'Dot Net']
pd.Series(subjects)
print('\nData without series object: ', subjects)
print('\nData with series object: \n', pd.Series(subjects))

