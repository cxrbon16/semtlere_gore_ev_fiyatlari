import pandas as pd

df = pd.read_csv('GFG')

def location_data(df):
    def change(location):
        location_splitted = location.rsplit('-')
        try:
            return location_splitted[1]
        except:
            return location

    for i in df['district']:
        df.replace(to_replace=i, value=change(i), inplace=True)

def price_data(df):
    def change(price):
        price = price.rsplit("TL")
        new_price = price[0].replace(",", "")
        return new_price
    for i in df['price']:
        df.replace(to_replace=i, value=change(i), inplace=True)

location_data(df)
price_data(df)
del df['index'], df['title'], df['link']
df.to_csv('manipulated_datas.csv')



