import pandas as pd
import numpy as np
from recommenders import popularity_recommender_py, item_similarity_recommender_py


df1 = pd.read_csv('triplets_file.csv')
df2 = pd.read_csv('song_data.csv')

# combine two tables
table_merge = pd.merge(df1, df2.drop_duplicates(['song_id']), on='song_id', how='left')


# combine song name and artist
table_merge['song'] = table_merge['title'] + ' - ' + table_merge['artist_name']

# popularity recommendation system

pr = popularity_recommender_py()
pr.create_recommendation(table_merge, 'user_id', 'song')
result = pr.recommendation(table_merge['user_id'][1])
print(result)

# recommend songs on the basis of most time listened
ir = item_similarity_recommender_py()
ir.create_recommendation(table_merge, 'user_id', 'song')
user_items = ir.get_user_items(table_merge['user_id'][11])
for user_item in user_items:
    print(user_item)