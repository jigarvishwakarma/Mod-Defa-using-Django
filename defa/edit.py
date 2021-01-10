import random
from moviepy.editor import *
from moviepy.video import *
from django.conf import settings
from . models import UploadedVideos
from PIL import Image
import ntpath
reslution = {'2160p':'3840x2160',
			'1440p':'2560x1440',		
			'1080p':'1920x1080',	
			'720p':'1280x720',	
			'480p':'854x480',	
			'360p':'640x360',	
			'240p':'426x240'}
			
def editing(name):
	print('fun '+name+'-->'+settings.MEDIA_ROOT+'\\'+name.replace('/', '\\'))
	clip0 = VideoFileClip(settings.MEDIA_ROOT+'\\'+name.replace('/', '\\')[4:])
	clip1 = clip0.subclip(15,35)
	clip1.write_videofile('output//'+'test'+'.mp4')
	print(clip1)

def editlist(video_list,num,name,res=(640,360)):
	img_list=['sky blue.png','green.png','red.png','blue.png','orange.png','purpel.png']
	final_video_list = []
	current_rank=num
	final_video_thumb = ''
	thumb_created = 0
	final_video_name = str(name)
	final_video_path = str(settings.MEDIA_ROOT+'\\output\\'+final_video_name+'.mp4')
	final_video_media_path = str('med\\output\\'+final_video_name+'.mp4')

	res = (640,360) #(1920,1080)
	for i in video_list:
		print(i)
		clip_time = 5
		raw_video = settings.MEDIA_ROOT+'\\'+str(i).replace('/', '\\')
		clip0 = VideoFileClip(raw_video)
		duration_val = int(clip0.duration)
		start_time=random.randrange(0,duration_val-clip_time,1)
		clip1=clip0.subclip(start_time,start_time+clip_time)
		clip1 = clip1.resize(newsize=res)
		if thumb_created==0:
			create_video_thum= Image.fromarray(clip1.get_frame(1))
			final_video_thumb=str(settings.MEDIA_ROOT+'\\output\\thumb\\'+final_video_name+str(random.random())+'.jpg')
			create_video_thum.save(final_video_thumb)
			thumb_created=1
			print(final_video_thumb)
		print(current_rank,clip1)
		if current_rank%2==0:
			pos_name_val=('left','bottom')
			pos_rank_val=('left','center')
			pos_im_val=('left','top')
		else:
			pos_name_val=('right','bottom')
			pos_rank_val=('right','center')
			pos_im_val=('right','top')
		head,tail=ntpath.split(raw_video)
		tail=tail[:-4]
		w,h=clip1.size
		im_clip=ImageClip(settings.MEDIA_ROOT+str('\\slides\\'+str(img_list[random.randrange(0,5,1)]))).set_opacity(0.65).set_duration(clip_time).set_position(pos_im_val).resize((int(w/3),h))
		rank_clip = TextClip("{}".format(str(current_rank)), fontsize=int(h/2), color='white').set_duration(clip_time).set_fps(clip1.fps).set_position(pos_rank_val)
		name_text=TextClip('{}'.format(str(tail)),fontsize=int(w/20),color='white').set_duration(clip_time).set_fps(clip1.fps).set_position(pos_name_val)
		overlay = CompositeVideoClip([clip1,im_clip,rank_clip,name_text]).set_duration(clip_time).set_fps(clip1.fps)
		final_video_list.append(overlay)
		current_rank=current_rank-1
	final_video = concatenate_videoclips(final_video_list)
	final_video.write_videofile(final_video_path)
	upoad_details = UploadedVideos(video_name=final_video_name,
		video_path=final_video_media_path,
		video_thum=final_video_thumb)
	upoad_details.save()

