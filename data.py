import pandas as pd

tables = pd.read_html("https://tproger.ru/articles/python-pandas/")

print(tables[0])