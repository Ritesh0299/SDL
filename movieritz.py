import pandas as pd
ds1=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")
ds1.head()
ds1.shape
ds1.info()
ds1['movie_title']
ds1['budget']
ds1['duration'][:10]
ds1['movie_title'][:10]
ds1[ds1['duration'] > 120] 
# Remove incomplete rows #
ds1.country=ds1.country.fillna(' ')
ds1.duration=ds1.duration.fillna(ds1.duration.mean())
ds1.dropna()
ds1.dropna(how='all')
ds1.num_critic_for_reviews=ds1.num_critic_for_reviews.fillna(ds1.num_critic_for_reviews.mean())

ds1.dropna(axis=1,how='all')


ds2=ds1.to_csv('new_movie_data.csv',encoding="utf-8")
ds2
