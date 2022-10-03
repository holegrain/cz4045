import praw
import pandas as pd
import time
import os

reddit = praw.Reddit(client_id='Ov0hf5hbdxVwAtI9CdodYw', client_secret='pzpqglx6N3_WoIAgJlMGsUowUkdwsw', user_agent='cz4045OMC')

start_time = time.time()

if os.path.exists('data.csv'):
    data = pd.read_csv('data.csv', index_col=0)
else: 
    data = pd.DataFrame()

#https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
while True:
    output = []
    n = 10
    t0 = time.time()
    posts = reddit.subreddit('offmychest').new(limit=n)
    for post in posts:
        output.append([post.title, post.id])
    t1= time.time() - t0
    print(t1)

    df = pd.DataFrame(output, columns=['title', 'id'])
    data = pd.concat([df, data]).drop_duplicates('id').reset_index(drop=True)
    print('length:', len(data))
    data.to_csv('data.csv')
    time.sleep(60.0 - ((time.time() - start_time) % 60.0))