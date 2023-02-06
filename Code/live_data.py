import tkinter as tk
from jugaad_data.nse import NSELive

def update_price():
    n = NSELive()
    q = n.stock_quote("HDFC")
    price_label.config(text=f"Price: {q['priceInfo']['lastPrice']}")
    root.after(1000, update_price)

root = tk.Tk()
root.title("HDFC Stock Price")

price_label = tk.Label(root, text="", font=("TkDefaultFont", 24))
price_label.pack()

update_price()

root.mainloop()