from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(all_posts)
    return render(request, 'blogs/post_list.html', {'all_posts': all_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
