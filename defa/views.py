from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from moviepy.editor import *
from . forms import BookForm
from . models import Book,ListModel,UploadedVideos
from . edit import editing,editlist

def home_page(request):
	videodetails = UploadedVideos.objects.all()
	return render(request,'main.html',{
		'videodetails':videodetails
		})
def watch_app(request):
	books = Book.objects.all()
	return render(request,'watch.html',{'books':books})

def submitvideo(request):
	video_name = request.POST['videoname']
	videos_to_edit = ListModel.objects.all()
	video_count = ListModel.objects.count()
	editlist(videos_to_edit,video_count,video_name)
	return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login/')	
def list_view(request):
	todo = ListModel.objects.all()
	print()
	return render(request,'todolist.html',{
		'todo':todo
		})

def addvideo(request):
	vid_name = ListModel(videos=request.FILES['content'])
	vid_name.save()
	return HttpResponseRedirect('/list/')

def deletevideo(request,deleteid):
	vid_name = ListModel.objects.get(id=deleteid)
	vid_name.delete()
	return HttpResponseRedirect('/list/')

def deleteallvideo(request):
	vid_name = ListModel.objects.all()
	vid_name.delete()
	return HttpResponseRedirect('/list/')

def watch(request,id):
	vid_obj = UploadedVideos.objects.filter(id=id)
	return render(request,'watchid.html',{
		'obj':vid_obj
		})

video_list=[]

def home(request):
	return render(request,'main.html')



def create_app(request):
	return render(request,'main.html')

def home_app(request):
	if request.method=='POST':
		num_of_video = request.POST.get('num')
		for i in range(int(num_of_video)):
			videoinput = request.FILES[i]
			print('-->'+'filename'+str(i+1))
			print(videoinput,videoinput.name)
	'''
	if request.POST.get('submit'):
		num_of_video = request.POST.get('num')
		for i in range(int(num_of_video)):
			videoinput = request.FILES['filename']
			print('-->'+'filename'+str(i+1))
			print(videoinput,videoinput.name)
	#en_name = request.POST.get('intro', False);'''
	#------------------------------------------------
	'''
	if 'intro' in request.POST:
	    en_name = request.POST['intro']
	else:
	    en_name = False
	en_num = request.POST.get('num', False);
	print(en_num)
	pool=[]
	link = ''
	for i in range(int(en_num)):
		pool.append(request.POST.get('filename'+str(i+1), False))
		print()
		print(pool)
		if request.method == 'POST':
			up_vid = request.FILES['filename'+str(i+1)]
			fs = FileSystemStorage()
			video_name = fs.save(up_vid.name,up_vid)
			link = fs.url(video_name)
			print(up_vid.name)
			clip0 = VideoFileClip(settings.MEDIA_ROOT+'//'+video_name)
			clip1 = clip0.subclip(15,35)
		
			#clip1.write_videofile('output//'+en_name+'.mp4')
			print(clip1)
			return redirect('/')'''


	return render(request,'index.html')
# Create your views here.


def book_list(request):
	books = Book.objects.all()
	return render(request,'book_list.html',{'books':books})

def upload_book(request):
	if request.method=='POST':
		form = BookForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			vid_name =form.save()
			print(vid_name)
			return redirect('')
	else:
		form=BookForm()			
	return render(request,'upload_book.html',{'form':form})

def editfun(request):
	books = Book.objects.all()
	print('printing')
	if request.POST.get('ebtn'):
		print(request.POST.get('tval'))
		editing(request.POST.get('tval'))
	return render(request,'edit.html',{'books':books})

def listedit(request):
	books = Book.objects.all()
	for i in books:
		print(i)
	video_list =[]
	if request.POST.get('ebtn'):
		for i in books:
			video_input = request.POST.get(i)
			print(video_input)
	return render(request,'listedit.html',{'books':books})

def singlevideo_view(request):
	#print(video_list)
	if request.method=='POST':
		form = VideoForm(request.POST,request.FILES)
		print(form)
		if form.is_valid():
			vid_name =form.save()
			print(vid_name)
			
	else:
		for i in range(2):
			video_data = VideoForm()
			video_list.append(video_data)
			#print(video_list)
	return render(request,'SingleVideo.html',{'video_data':video_list})