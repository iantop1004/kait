import pandas as pd

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
def get_address(emo):
    df = pd.read_csv('art_data.csv', encoding='cp949')
# df = pandas.read_csv('data.csv', index_col='Name')

    df2 = df[df["emotion"]==emo]
    print(df2)
  
    print(df2.sample(axis=0)["address"])








