#First thing first is that we are going to import the library Pythube
import pytube

url = ''
video = pytube.Youtube(url)

#created a varible called stream and made it equal to the video and get the itag of what I want to get it by.

stream = video.streams.get_by_itag(22)
print('Downloading')
stream.download(filename='name of the video')
print('Done')



#Showing how the streams object is structured. 
#This will print out the structure of the video from the url. We can also specify that we want the video to be in mp4.
for string in video.streams:
    if 'video' in str(stream) and 'mp4' str(stream)
    print(stream)


