import os
import tkinter as tk
import pandas as pd
import requests
import csv

session = requests.session()

headers = {
    'user-agent': "Chrome/87.0.4280.88"
}


def makeDataset(url):
    with open("dataset.csv", "w") as f:
        f.write(session.get(url).text)

    with open("dataset.csv", "r") as f:
        dataset = csv.reader(f)
        niftyData = []
        stockData = []

        for idx, row in enumerate(dataset):
            if 8 <= idx <= 67:
                niftyData.append(row)
            if 120 <= idx:
                stockData.append(row)
    os.remove("dataset.csv")
    return pd.DataFrame(niftyData), pd.DataFrame(stockData)


def getTodayData() -> object:
    webData = session.get(url="https://www.nseindia.com/api/merged-daily-reports?key=favCapital", headers=headers)
    return makeDataset(webData.json()[1]['link'])

def show_table(dataframe):
    root = tk.Tk()
    root.title("Data")

    max_width = {}
    for i, col_name in enumerate(dataframe.columns):
        tk.Label(root, text=col_name, relief="solid").grid(row=0, column=i+1)
        max_width[i] = len(str(col_name))

    for j, row in dataframe.iterrows():
        for i, col_value in enumerate(row):
            tk.Label(root, text=col_value).grid(row=j+1, column=i)
            if len(str(col_value)) > max_width[i]:
                max_width[i] = len(str(col_value))

    for i in range(len(max_width)):
        root.columnconfigure(i, minsize=max_width[i] * 10)

    root.mainloop()