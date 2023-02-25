import tkinter as tk
from tkinter import ttk
import webbrowser
import feedparser

class NewsAggregator:
    def __init__(self, master):
        self.master = master
        master.title("Stock News Aggregator")
        
        # Calculate window size and position based on monitor size
        monitor_width = master.winfo_screenwidth()
        monitor_height = master.winfo_screenheight()
        window_width = int(monitor_width * 0.5)
        window_height = int(monitor_height * 0.5)
        window_x = int((monitor_width - window_width) / 2)
        window_y = int((monitor_height - window_height) / 2)
        master.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
        
        # Create tickers input box
        self.tickers_label = tk.Label(master, text="Enter stock tickers (separated by commas):")
        self.tickers_label.pack()
        self.tickers_entry = tk.Entry(master)
        self.tickers_entry.pack()
        
        # Create ticker selection drop-down box
        self.ticker_options = ["AAPL", "GOOGL", "TSLA", "AMZN", "FB"]
        self.ticker_label = tk.Label(master, text="Select a stock ticker:")
        self.ticker_label.pack()
        self.ticker_combobox = ttk.Combobox(master, values=self.ticker_options)
        self.ticker_combobox.pack()
        
        # Create filter input box
        self.filter_label = tk.Label(master, text="Enter keywords to filter (separated by commas):")
        self.filter_label.pack()
        self.filter_entry = tk.Entry(master)
        self.filter_entry.pack()
        
        # Create "Fetch News" button
        self.fetch_button = tk.Button(master, text="Fetch News", command=self.fetch_news)
        self.fetch_button.pack()
        
    # Create news listbox
        self.news_frame = tk.Frame(master)
        self.news_frame.pack(fill=tk.BOTH, expand=True)
        self.news_scrollbar = tk.Scrollbar(self.news_frame)
        self.news_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.news_listbox = tk.Listbox(self.news_frame, yscrollcommand=self.news_scrollbar.set)
        self.news_listbox.pack(fill=tk.BOTH, expand=True)
        self.news_scrollbar.config(command=self.news_listbox.yview)
        self.news_listbox.bind("<Double-Button-1>", self.open_link)
        
    def fetch_news(self):
        # Get tickers from input box or selection drop-down
        tickers = self.tickers_entry.get()
        if not tickers:
            tickers = self.ticker_combobox.get()
        if not tickers:
            return
        
        # Get filter keywords from input box
        filter_keywords = self.filter_entry.get()
        if filter_keywords:
            filter_keywords = filter_keywords.split(",")
        else:
            filter_keywords = []
        
        # Fetch news articles for each ticker
        for ticker in tickers.split(","):
            url = f"https://news.google.com/rss/search?q={ticker}+stock"
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.title
                link = entry.link
                summary = entry.summary
                # Check if any filter keyword is present in the article
                if any(keyword.strip().lower() in summary.lower() for keyword in filter_keywords):
                    continue
                # Create clickable news link
                label = tk.Label(self.master, text=title, fg="blue", cursor="hand2")
                label.pack()
                label.bind("<Button-1>", lambda e: webbrowser.open_new(link))
                
    def open_link(self, event):
        # Open link in default web browser when double-clicked
        selection = self.news_listbox.curselection()
        link = news[selection[0]][1]
        webbrowser.open_new_tab(link)

root = tk.Tk()
my_aggregator = NewsAggregator(root)
root.mainloop()