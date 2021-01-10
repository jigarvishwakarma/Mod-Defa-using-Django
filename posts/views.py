from django.shortcuts import render,get_object_or_404
from . models import Post,PostImage
from . forms import PostImageForm,PostForm


# Create your views here.
def blog_view(request):
	posts = Post.objects.all()
	formimg = PostImageForm()
	form = PostForm()
	return render(request,'blog.html',{'posts':posts,'formimg':formimg,'form':form})

def  detail_view(request,id):
	post = get_object_or_404(Post,id=id)
	photos = PostImage.objects.filter(post=post)
	print(post,photos)
	return render(request,'detail.html',{'post':post,'photos':photos})

