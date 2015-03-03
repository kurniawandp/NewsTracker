# Google News Semeantic Analytics
Simple analytics tool that finds and scores a subject's news presence to be either positive or negative, all in real-time.

Using Scrapy, this web spider goes through 4 sections of the Google News Page (Technology, Business, U.S., Worldwide), and finds all articles with the subject mentioned and then, using a third-party semantic analytics tool, rates the article to be either a positive or negative article. In the end, it compiles all these found articles and ranks it in terms of their sources (the more credible the better eg. The Wall Street Journal), and declares that the subject has a positive, negative, or no, news presence. 
