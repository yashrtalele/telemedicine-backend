from django.http import JsonResponse
from rest_framework import generics
from article.models import Article
from .serializers import ArticleSerializer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
import pickle
import logging
from django.shortcuts import render


# Create your views here.    

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def recommendations(request, id):
    tfv = TfidfVectorizer(min_df=3,max_features=None,ngram_range=(1,3),stop_words='english')
    contentTuple = Article.objects.values_list('content')
    contentList = list(map(lambda item:item[0], contentTuple))
    tfv_matrix = tfv.fit_transform(contentList)
    sig = sigmoid_kernel(tfv_matrix,tfv_matrix)
    sigma_scores = sorted(list(enumerate(list(sig[id]))),key=lambda x:x[1],reverse=True)
    ind = [index[0] for index in sigma_scores[1:11]]
    return ArticleList.as_view(queryset = Article.objects.filter(id__in=ind), serializer_class=ArticleSerializer)(request)

def prediction(request):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('myapp')
    symptoms = [
        int(request.GET.get('s1', '0')),
        int(request.GET.get('s2', '0')),
        int(request.GET.get('s3', '0')),
        int(request.GET.get('s4', '0')),
        int(request.GET.get('s5', '0')),
    ]
    model = pickle.load(open('static/model.sav', 'rb'))

    for i in range(0, 12):
        symptoms.append(0)
    context = {
        'PageName' : 'prediction',
        'PredictedDisease' : model.predict([symptoms])[0]
    }
    return JsonResponse({
        'PredictedDisease' : model.predict([symptoms])[0],
    })