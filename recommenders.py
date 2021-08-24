import numpy as np
import pandas


# recommend on the basis of popularity
class popularity_recommender_py:
    def __init__(self):
        self.table_data = None
        self.user_id = None
        self.song_id = None
        self.popularity_recommendation = None

    def create_recommendation(self, table_data, user_id, song_id):
        self.table_data = table_data
        self.user_id = user_id
        self.song_id = song_id
        grouping_data = table_data.groupby([self.song_id]).agg({self.user_id: 'count'}).reset_index()
        grouping_data.rename(columns={'user_id': 'score'}, inplace=True)
        table_sort = grouping_data.sort_values(['score', self.song_id], ascending=[0, 1])
        table_sort['Rank'] = table_sort['score'].rank(ascending=0, method='first')
        self.popularity_recommendation = table_sort.head(15)

    def recommendation(self, user):
        user_recommendations = self.popularity_recommendation
        user_recommendations['user_id'] = user
        cols = user_recommendations.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        user_recommendations = user_recommendations[cols]
        return user_recommendations
