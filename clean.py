import pandas as pd
old_data = pd.read_csv(r'CryptocoinsHistoricalPrices.csv', encoding='utf8', sep = ',')
old_data = old_data.dropna()
old_data = old_data[old_data["coin"].isin(["BTC","DASH","ETH","XRP","LTC","BITBTC"])]
old_data = old_data.loc[old_data.groupby(['coin','Date']).apply(lambda x: x['Close'].idxmax())]
new_data=old_data.drop('No',1)
new_data.to_csv("Cryptonew.csv", sep=',')