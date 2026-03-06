from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

from .models import Feedback
from .forms import FeedbackForm


def feedback_list(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')

    else:
        form = FeedbackForm()
    context = {
        'form':form,
        'feedback':Feedback.objects.filter(is_active=True).order_by('-created_at')
     }
    return render(request,'feedback.html',context)



@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)



@login_required
def about(request):
    return render(request, 'about.html')
