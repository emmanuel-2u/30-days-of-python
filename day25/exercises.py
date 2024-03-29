import pandas

df = pandas.read_csv('hacker_news.csv')

def get_title(df):
    print(df['title'])

def first_five(df):
    print(df.head())

def last_five(df):
    print(df.tail())

def only_python(df):
    print(df[df['title'].str.contains('python')])

def only_javascript(df):
    print(df[df['title'].str.contains('javascript')])

first_five(df)

last_five(df)

get_title(df)

only_python(df)

only_javascript(df)