from io import StringIO
import requests
import pandas as pd
import datetime
from datetime import datetime , timedelta
import bs4
import tkinter as tk
from tkinter import ttk
from requests import Session

"""
    This function creates a GUI using the Tkinter library. The show_table function creates a window with a table that displays the data from the input dataframe. The input company symbol is passed to the getHistoryData function, which retrieves the stock data from NSE India's website and returns it as a dataframe. The returned dataframe is then passed to the show_table function, which displays the data in a table within a GUI window.
    """

session = requests.session()
headers = {
    "user-agent": "Chrome/87.0.4280.88"
}
head = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}

def getHistoryData(company, from_date=(datetime.today().strftime("%d-%m-%Y")), to_date=(datetime(datetime.today().year - 1, datetime.today().month,datetime.today().day).strftime("%d-%m-%Y"))):
    session.get("https://www.nseindia.com", headers=head)
    session.get("https://www.nseindia.com/get-quotes/equity?symbol=" + company, headers=head)  # to save cookies
    session.get("https://www.nseindia.com/api/historical/cm/equity?symbol="+company, headers=head)
    url = "https://www.nseindia.com/api/historical/cm/equity?symbol=" + company + "&series=[%22EQ%22]&from=" + from_date + "&to=" + to_date + "&csv=true"
    webdata = session.get(url=url, headers=head)
    df = pd.read_csv(StringIO(webdata.text[3:]))
    return df

def show_table(df):
    root = tk.Tk()
    frame = ttk.Frame(root)
    frame.pack()
    table = ttk.Treeview(frame, columns=df.columns)
    table.pack()

    for col in df.columns:
        table.heading(col, text=col.capitalize())
        table.column(col, width=100, anchor="center")
        table['show'] = 'headings'

    for i, row in df.iterrows():
        table.insert("", "end", values=list(row))

    root.mainloop()

def niftyHistoryData(varient, from_date = ((datetime(datetime.today().year - 1, datetime.today().month, datetime.today().day) + timedelta(days=2)).strftime("%d-%m-%Y")), to_date =(datetime.today().strftime("%d-%m-%Y"))):
    varient = varient.upper()
    varient = varient.replace(' ', '%20')
    varient = varient.replace('-', '%20')
    webData = session.get(
        url="https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?indexType=" + varient +
            "&fromDate=" + from_date + "&toDate=" + to_date,
        headers=head)
    soup = bs4.BeautifulSoup(webData.text, 'html5lib')
    return pd.read_csv(StringIO(soup.find('div', {'id': 'csvContentDiv'}).contents[0].replace(':','\n')))

if __name__ == "__main__":
    df = getHistoryData('SHREECEM',from_date='30-04-2020',to_date='30-04-2021')
    show_table(df)
#print(getHistoryData('SHREECEM',from_date='30-04-2020',to_date='30-04-2021'))
# print(niftyHistoryData('NIFTY 50'))