
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from articleManager.models import Label, Article

@csrf_protect
def get_all_articles(request):
	data = []
	data += [{'title': a.title, 'img': a.img, 'preview': a.preview} for a in Article.objects.all()]
	articles = json.dumps(data)

	return	JsonResponse(articles)

@csrf_protect
def get_acrticle(request):
	acrticle_id = request.GET.get('id')
	article = Article.objects.get(id=acrticle_id)
	data = [{'title': article.title, 'img': article.img, 'text': article.text}]
	article = json.dumps(data)

	return JsonResponse(article)

@csrf_protect
def get_all_labels(request):
	data = []
	data += [{'label': l.label, 'img': l.img} for l in Label.objects.all()]
	labels = json.dumps(data)

	return JsonResponse(labels)

def render_article_page(request):
	labels = Label.objects.all()
	articles = Article.objects.all()
	return render(request, 'main.html', {})