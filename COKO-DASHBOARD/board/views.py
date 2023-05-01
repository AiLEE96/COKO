from django.shortcuts import render
from board.models import Corona
from datetime import datetime, timedelta
from board.models import News

def list(request):
    posts = Corona.objects.all().order_by('-localocccnt')
    g_posts = Corona.objects.all().order_by('stdday')
    d_posts = Corona.objects.all().order_by('stdday')
    g_posts = g_posts.values()
    g_posts =g_posts.filter(gubun__icontains="합계")
    print("g_posts", g_posts)
    q = datetime.now().date() - timedelta(1)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        print("list 실행")
        return render(request, 'board/index.html', {'posts': posts, 'q': q, 'g_posts':g_posts, 'd_posts':d_posts })

    else:
        return render(request, 'board/index.html')


def News_list(request):
    posts = News.objects.all().order_by('pubdate')
    print("News_list 실행")
    return render(request, 'board/news.html', {'posts': posts})


def regions(request):

    get_data=request.GET.get('get_data')
    ajax_posts = Corona.objects.all().order_by('stdday')
    ajax_posts = ajax_posts.filter(gubun__icontains= get_data)
    print("regions 실행")
    return render(request, 'board/test.html', {'ajax_posts': ajax_posts, 'get_data': get_data})

def default(request):
    return render(request, 'board/default.html')