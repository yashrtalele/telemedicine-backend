import numpy as np
import pandas as pd

df = pd.read_csv('./static/articleData.csv')

df = df[['id', 'title', 'content']]

df = df.head(100)

from article.models import Article

Article.objects.values('title')

for i in range(0, df.axes[0].stop):
    object = Article(i, df['title'][i], df['content'][i])
    object.save()

# from sklearn.feature_extraction.text import TfidfVectorizer

# tfv=TfidfVectorizer(min_df=3,max_features=None,ngram_range=(1,3),stop_words='english')

# from sklearn.metrics.pairwise import sigmoid_kernel

# https://stackoverflow.com/questions/5481890/django-does-the-orm-support-the-sql-in-operator