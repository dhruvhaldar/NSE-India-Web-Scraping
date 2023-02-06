import tkinter as tk
from jugaad_data.nse import NSELive

n = NSELive()

def show_data():
    company = entry.get()
    q = n.stock_quote(company)
    label['text'] = f"{company}: {q['priceInfo']['lastPrice']}"

root = tk.Tk()
root.title("Stock Price Info")

label = tk.Label(root, text="Enter a company name and press the button", font=("Helvetica", 16))
label.pack()

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

button = tk.Button(root, text="Get Stock Info", command=show_data)
button.pack()

watchlist = tk.Listbox(root)
watchlist.pack()

root.mainloop()
