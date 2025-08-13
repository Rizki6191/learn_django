from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import PostForm
from blog.models import Post
# Tidak ada kode yang perlu ditambahkan di sini untuk menjalankan fungsi home.
# Create your views here.
def home(request):
    # return HttpResponse("Hello, world!")
    posts = Post.objects.all()  # Mengambil semua post dari database
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
       form = PostForm()
       return render(request, 'blog/create_post.html', {'form': form})
