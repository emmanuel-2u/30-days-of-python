import pandas

obj = { 'first': ['My oh my', 'Akirisore', 'Beautifyl God'], 'last': ['MyFirst', 'Ite', 'My King'] }
print(pandas.DataFrame(obj))
df = pandas.read_csv('weight-height.csv')

print(df.describe())