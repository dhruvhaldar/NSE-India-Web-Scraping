from email.feedparser import FeedParser
import tkinter as tk
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
        
        # Create filter input box
        self.filter_label = tk.Label(master, text="Enter keywords to filter (separated by commas):")
        self.filter_label.pack()
        self.filter_entry = tk.Entry(master)
        self.filter_entry.pack()
        
        # Create "Fetch News" button
        self.fetch_button = tk.Button(master, text="Fetch News", command=self.fetch_news)
        self.fetch_button.pack()
        
        # Create news listbox
        self.news_listbox = tk.Listbox(master)
        self.news_listbox.pack(fill=tk.BOTH, expand=True)
    
    def fetch_news(self):
        # Clear existing news items
        self.news_listbox.delete(0, tk.END)
        
        # Get tickers and filter keywords from input boxes
        tickers = self.tickers_entry.get().split(",")
        filters = self.filter_entry.get().split(",")
        
        # Fetch news for each ticker
        for ticker in tickers:
            url = f"https://news.google.com/rss/search?q={ticker}+stock&hl=en-US&gl=US&ceid=US:en"
            feed = feedparser.parse(url)
            
            # Add news items to listbox
            for entry in feed.entries:
                if any(filter.lower() in entry.title.lower() for filter in filters):
                    continue
                self.news_listbox.insert(tk.END, entry.title)
                self.news_listbox.itemconfig(tk.END, foreground="blue", cursor="hand2")
                self.news_listbox.bind("<Double-Button-1>", self.open_link)
    
    def open_link(self, event):
        # Open selected news item in default web browser
        index = self.news_listbox.curselection()[0]
        url = "https://news.google.com" + FeedParser.entries[index].link[1:]
        webbrowser.open(url)

root = tk.Tk()
app = NewsAggregator(root)
root.mainloop()