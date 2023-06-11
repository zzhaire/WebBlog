from django.http import JsonResponse
from .form import CommentForm
from .models import Comment
from blogs.models import BlogInfo


# Create your views here.
def comment(request, id):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data.get('content')
            blog = BlogInfo.objects.get(id=id)
            blog.message_num += 1
            blog.save()

            user = request.user
            message = Comment()
            message.comment_user = user
            message.comment_blog = blog
            message.content = content
            message.save()
            return JsonResponse({'status': 'ok', 'msg': '评论成功', 'content': content})
        return JsonResponse({'status': 'false', 'msg': 'illegal content'})
    return JsonResponse({'status': 'false', 'msg': 'please log in '})
