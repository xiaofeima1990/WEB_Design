#coding: utf-8
# Create your views here.

from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from blog.models import Article,Tag,Classification
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    context_dict = {}

    articles = Article.objects.all()
    paginator = Paginator(articles,2) #the number of articles in each page
    page_num = request.GET.get('page')   #by method 'get'
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = RequestContext(request)
    classification = Classification.objects.all()
    article_list = Article.objects.order_by('-publish_time')[:3]


    context_dict['articles']= articles
    context_dict['classification'] = classification
    context_dict['article_list'] = article_list

    return render_to_response('blog/index.html',
                  context_dict,                    
                  context)

def content(request, id):
    context_dict = {}

    article = get_object_or_404(Article, id=id)
    classification = Classification.objects.all()
    context = RequestContext(request)
    article_list = Article.objects.order_by('-publish_time')[:3]



    context_dict['article']= article
    context_dict['classification'] = classification
    context_dict['article_list'] = article_list

    return render_to_response('blog/content.html',
                  context_dict,
                  context)


def about(request):
    context_dict = {}

    classification = Classification.objects.all()
    article_list = Article.objects.order_by('-publish_time')[:3]

    context = RequestContext(request)
    context_dict['classification'] = classification
    context_dict['motto'] = "stay hard stay stupid"
    context_dict['article_list'] = article_list


    return render_to_response('blog/about.html',
                  context_dict,
                  context)


def classification(request):
    context_dict = {}
    cat_dict={}

    classification = Classification.objects.all()
    for cat in classification:
        articles = Article.objects.filter(classification=cat)
        cat_dict[cat.name] = articles
          


    # try:
    #     cate = Classification.objects.get(id=id)
    # except Classification.DoesNotExist:
    #     raise Http404
    # articles = Article.objects.filter(classification=cate)
  
    classification = Classification.objects.all()
    article_list = Article.objects.order_by('-publish_time')[:3]

    context_dict['classification'] = classification
    
    context_dict['cat_dict'] = cat_dict
    context_dict['article_list'] = article_list


    context = RequestContext(request)

    return render_to_response('blog/classification.html',
                              context_dict,
                              context)



def suggest_art(request):
        context = RequestContext(request)
        article_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']

        article_list = get_article_list(5, starts_with)

        return render_to_response('blog/category_list.html', {'article_list': article_list }, context)



def get_article_list(max_results=0, starts_with=''):
    art_list = []
    if starts_with:
        art_list = Article.objects.filter(name__startswith=starts_with)
    else:
        art_list = Article.objects.all()

    if max_results > 0:
        if (len(art_list) > max_results):
            art_list = art_list[:max_results]
    
    return art_list