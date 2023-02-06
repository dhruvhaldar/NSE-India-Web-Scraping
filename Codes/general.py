import tkinter as tk
from tkinter import ttk
from jugaad_data.nse import NSELive
import time

def show_data(ticker):
    n = NSELive()
    wait_label.pack(side='top', fill='x')
    while True:
        try:
            q = n.stock_quote(ticker)
            price_label.config(text="Price: Rs " + str(q['priceInfo']['lastPrice']))
            break
        except:
            time.sleep(1)
    wait_label.pack_forget()

root = tk.Tk()
root.title("Stock Ticker")

frame = ttk.Frame(root)
frame.pack(side='top', fill='both', expand=True)

price_label = ttk.Label(frame)
price_label.pack(side='top', fill='x')

wait_label = ttk.Label(frame, text="Waiting for data...")

ticker = tk.StringVar()
ticker_entry = ttk.Entry(frame, textvariable=ticker)
ticker_entry.pack(side='top', fill='x', padx=10, pady=10)

search_button = ttk.Button(frame, text="Search", command=lambda: show_data(ticker.get()))
search_button.pack(side='top', padx=10, pady=10)

root.mainloop()

