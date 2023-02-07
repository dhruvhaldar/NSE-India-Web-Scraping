"""from today_all_stocks import show_table, getTodayData
from general import update_price


update_price()"""
from today_all_stocks import show_table, getTodayData


nifty_data, companies_data = getTodayData()
show_table(nifty_data)