#import libraries

import seaborn as sns
sns.set_theme()
from datetime import datetime
from datetime import timedelta
from datetime import date
from sklearn.cluster import KMeans
import numpy as np

#get column of all unique users within the game
unique_users = data['player_id'].unique()

new_columns = ["Challenge Stack", "People Sense", "Knowledge Minigame", "Priority Sense", "Refuse Power Minigame", "Minigame General", "AspirationalAvatar", "Lifeline", "Epilogue", "Avatar Creation", "General"]
for column in new_columns:
    s5_scores[column] = [0]*s5_scores.shape[0]

for user in unique_users:
    #get date for the user impression and convert it to useful format
    one_user = data.loc[data['player_id'] == user]
    date_conversion = one_user.loc[one_user['player_id'] == user, "date"].array
    d0 = datetime.strptime(date_conversion[0], "%Y-%m-%d")

    #calculate the time ranges at which samples were taken for the scores within the game
    time_ranges = []
    for week in s5_scores.loc[s5_scores['player_id'] == user]["weeks"]:
        d2 = d0 + timedelta(days=week*7)
        time_ranges.append(d2)

    # Convert the date to datetime64
    one_user['date'] = pd.to_datetime(one_user['date'], format='%Y-%m-%d')

    for t in range(1, len(time_ranges)):
        # Filter data between two dates so that it falls within the defined ranges in time_ranges array
        start_date = time_ranges[t-1] #start date
        end_date = time_ranges[t] #end data
        filtered_df = one_user.loc[(one_user['date'] >= start_date) & (one_user['date'] < end_date)] #filter mask
        result = filtered_df["event_category"].value_counts() #count the number of points assigned to each category
                                                              #at specific time
        if result.empty:
            continue
        week = ((end_date - d0)/7).days  

        for index, value in result.items():
            if not value:
                continue

        #match points gathered in the Challenge Stack to survey scores
        for index, value in result.items():
            s5_scores.loc[(s5_scores['player_id'] == user) & (s5_scores['weeks'] == week), index] = value

    #each week has the total values for challenge stack and the score for s5_scores

#make scatterplot to represent number of points obtained by each unique user within each cateogory of the game
#over each survey period

sns.relplot(data=s5_scores, x="S5_mean", y="Challenge Stack", col="weeks", height=3)
sns.relplot(data=s5_scores, x="S5_mean", y="People Sense", col="weeks", height=3)
sns.relplot(data=s5_scores, x="S5_mean", y="Knowledge Minigame", col="weeks", height=3)
sns.relplot(data=s5_scores, x="S5_mean", y="Priority Sense", col="weeks", height=3)
