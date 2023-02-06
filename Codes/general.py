import tkinter as tk
from jugaad_data.nse import NSELive
def update_price(symbol):
    """This code uses the after method of the Tkinter GUI object to schedule a call to update_price every 1000 milliseconds (1 second). The update_price function updates the text of the price_label widget to show the latest price.
    """
    n = NSELive()
    q = n.stock_quote("HDFC")
    price_label.config(text=f"Price: {q['priceInfo']['lastPrice']}")
    root.after(1000, update_price)

root = tk.Tk()
root.title("HDFC Stock Price")

price_label = tk.Label(root, text="", font=("TkDefaultFont", 24))
price_label.pack()



root.mainloop()