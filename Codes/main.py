from today_all_stocks import show_table, getTodayData
from general import update_price


symbol="HDFC"
update_price(symbol)
nifty_data, companies_data = getTodayData()
show_table(nifty_data)