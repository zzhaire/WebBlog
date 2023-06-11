from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import *
from tools.get_time import cal_time
from pure_pagination import Paginator
from comments.models import Comment


def index(request):
    """首页"""
    all_blogs = BlogInfo.objects.all().order_by('-add_time')
    blogs_nums = all_blogs.count()
    all_tags = TagInfo.objects.all()
    all_category = Category.objects.filter(is_tab=True).order_by('add_time')
    max_category = BlogInfo.objects.values('category__name').annotate(Count('category__name'))
    hot_blogs = BlogInfo.objects.order_by('-click_num')[:8]
    recommend = BlogInfo.objects.filter(is_recommend=True)[:2]
    period = cal_time()

    # 分页
    page_num = request.GET.get('page', '1')
    # 5篇文章一页
    paginator = Paginator(all_blogs, 4)
    if int(page_num) > paginator.num_pages:
        return redirect('/')

    now_page = paginator.page(page_num)

    information = {
        "now_page": now_page,
        "blogs_nums": blogs_nums,
        "all_tags": all_tags,
        "all_category": all_category,
        "max_category": max_category,
        "hot_blogs": hot_blogs,
        "recommend": recommend,
        'period': period,
    }
    return render(request, 'index.html', context=information)


def blog_list(request, kind):
    all_category = Category.objects.filter(is_tab=True).order_by('add_time')
    hot_blogs = BlogInfo.objects.order_by('-click_num')[:8]
    all_tags = TagInfo.objects.filter(category__name=kind)
    TagInfo.objects.filter(category__name=kind)  # 不加__name会使用id查询

    kind_obj = Category.objects.filter(name=kind)
    if kind_obj:
        tag = request.GET.get('tag', '')
        if tag:
            all_blogs = BlogInfo.objects.filter(category__name=kind, taginfo__id=tag)
        else:
            all_blogs = BlogInfo.objects.filter(category__name=kind)
        # 分页
        page_num = request.GET.get('page', '1')
        # 5篇文章一页
        paginator = Paginator(all_blogs, 5)
        if int(page_num) > paginator.num_pages:
            return redirect('/')

        now_page = paginator.page(page_num)

        information = {
            'now_page': now_page,
            'all_tags': all_tags,
            'hot_blogs': hot_blogs,
            'all_category': all_category,
            'kind': kind,
        }
        return render(request, 'list.html', context=information)
    else:
        return redirect(reverse('index'))


def blog_detail(request, id):
    all_category = Category.objects.filter(is_tab=True).order_by('add_time')
    hot_blogs = BlogInfo.objects.order_by('-click_num')[:8]
    all_tags = TagInfo.objects.all()
    # now_blog = BlogInfo.object.filter(id=id)
    # now_blog[0].click_num +=1
    # now_blog[0].save
    now_blog = get_object_or_404(BlogInfo, id=id)
    now_blog.click_num += 1
    now_blog.save()

    comment_list = Comment.objects.filter(comment_blog=id)

    information = {
        'all_category': all_category,
        'hot_blogs': hot_blogs,
        'all_tags': all_tags,
        'now_blog': now_blog,
        'comment_list': comment_list,
    }
    return render(request, 'detail.html', context=information)


def blog_search(request):
    """搜索页面"""
    all_category = Category.objects.filter(is_tab=True).order_by('add_time')
    keyword = request.GET.get('keyword', '')

    if keyword:
        all_blogs = BlogInfo.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
        if all_blogs:

            page_num = request.GET.get('page', '1')
            # 5篇文章一页
            paginator = Paginator(all_blogs, 5)
            if int(page_num) > paginator.num_pages:
                return redirect('/')

            now_page = paginator.page(page_num)

            all_tags = TagInfo.objects.all()
            hot_blogs = BlogInfo.objects.order_by('-click_num')[:5]
            context = {
                "now_page": now_page,
                "all_tags": all_tags,
                "hot_blogs": hot_blogs,
                "all_category": all_category,
            }
            return render(request, 'search_list.html', context)
    return render(request, '404.html', {"all_category": all_category})
