# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZDBarbqWWK95-2muV8cPlwxfIWsplXiH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from  datetime import datetime

data=pd.read_csv('/USvideos.csv')

data.head()

data.shape

data= data.drop_duplicates()
data.shape

data.describe()

data.info()

columns_to_remove=['thumbnail_link','description']
data=data.drop(columns=columns_to_remove)
data.info()

import datetime

data['trending_date']= data['trending_date'].apply(lambda x: datetime.datetime.strptime(x,'%y.%d.%m'))
data.head(3)

data['publish_time']=pd.to_datetime(data['publish_time'])
data.head(3)

data['publish_month']=data['publish_time'].dt.month
data['publish_day']=data['publish_time'].dt.day
data['publish_hour']=data['publish_time'].dt.hour
data.head(3)

print(sorted(data['category_id'].unique()))
[1,2,10,15,17,19,20,22,23,24,25,26,27,28,29,30,43]

data['category_name']= np.nan
data.loc[data['category_id']==1,'category_name']='Film & Animation'
data.loc[data['category_id']==2,'category_name']='Autos & Vehicles'
data.loc[data['category_id']==10,'category_name']='Music'
data.loc[data['category_id']==15,'category_name']='Pets & Animals'
data.loc[data['category_id']==17,'category_name']='Sports'
data.loc[data['category_id']==19,'category_name']='Travel & Events'
data.loc[data['category_id']==20,'category_name']='Gaming'
data.loc[data['category_id']==22,'category_name']='People & Blogs'
data.loc[data['category_id']==23,'category_name']='Comedy'
data.loc[data['category_id']==24,'category_name']='Entertainment'
data.loc[data['category_id']==25,'category_name']='News & Politics'
data.loc[data['category_id']==26,'category_name']='Howto & Style'
data.loc[data['category_id']==27,'category_name']='Education'
data.loc[data['category_id']==28,'category_name']='Science & Technology'
data.loc[data['category_id']==29,'category_name']='Nonprofits & Activism'
data.loc[data['category_id']==30,'category_name']='Movies'
data.loc[data['category_id']==43,'category_name']='Shows'
data.head()

data['year']=data['trending_date'].dt.year
yearly_counts = data.groupby('year') ['video_id'].count()

#create a bar chart
yearly_counts.plot(kind='bar',title='Total Publish Video Per Year')
plt.xlabel('Year')
plt.ylabel('Total Publish count')

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

#Group by year and sum the views for each year
yearly_views = data.groupby('year')['views'].sum()

#Create a bar chart
yearly_views.plot(kind='bar', title='Total Views Per Year')
plt.xlabel('Year')
plt.ylabel('Total Views')

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

#Group the data by 'category_name' and calculate the sum of the 'views' in each category
category_views = data.groupby('category_name')['views'].sum().reset_index()

#Sort the categories by the total views in descending order
top_categories = category_views.sort_values(by='views', ascending=False).head(5)

#Create a bar chart to visualize the top 5 category

plt.bar(top_categories['category_name'],top_categories['views'])
plt.xlabel('Category Name')
plt.ylabel('Total Views')
plt.title('Top 5 Categories by Total Views')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(data=data,x='category_name',order=data['category_name'].value_counts().index)
plt.title('Count of Videos in Each Category')
plt.xticks(rotation=90)
plt.show()

#Count the number of videos published per hour

videos_per_hour = data['publish_hour'].value_counts().sort_index()

#Create a bar chart
plt.figure(figsize=(12,6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='viridis')
plt.title('Number of Videos Published Per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()

data['publish_time'] = pd.to_datetime(data['publish_time'])

data['publish_date'] = data['publish_time'].dt.date

video_counts_by_date = data.groupby('publish_date').size()

plt.figure(figsize=(12, 6))
sns.lineplot(x=video_counts_by_date.index, y=video_counts_by_date.values)
plt.title('Number of Videos Published Over Time')
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show

#Scatter plot between 'views' and 'likes'

sns.scatterplot(data=data, x='views', y='likes')
plt.title('Scatter Plot of Views vs. Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.show()

plt.figure(figsize = (12,6))

plt.subplots_adjust(wspace=0.2,hspace=0.4, top=0.9)
plt.figure(figsize = (12,6))

plt.subplots_adjust(wspace=0.2,hspace=0.4, top=0.9)
plt.subplot(2,2,1)

# Check if the column name is 'comments_disabled' instead of 'Comments_disabled'
# If it is, change 'Comments_disabled' to 'comments_disabled' in the line below
gr=sns.countplot(x='comments_disabled',data=data)

gr.set_title('Comments Disabled',fontsize=15)
plt.show()

corr_matrix=data['views'].corr(data['likes'])
corr_matrix