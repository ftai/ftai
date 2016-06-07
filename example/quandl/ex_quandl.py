
import quandl as ql

ql.ApiConfig.api_key = 'hogehoge' # APIKeyを置かないと取得制限

# 基本的な使い方は公式参照：https://www.quandl.com/
df_GDP = ql.get('ODA/JPN_NGDP_R') # 日本GDP
df_GDP

df_STOCK = ql.get(['NIKKEI/INDEX', 'YAHOO/INDEX_GSPC']) # 日経平均株価、S&P株価
df_STOCK.tail(15)
