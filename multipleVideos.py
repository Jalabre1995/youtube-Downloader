import pytube
video_list = []

print("Enter your url (End by 'STOP') ")
#If the video 
while True:
    url = input('')
    if url == 'STOP':
        break
    video_list.append(url)
#Iterate over the video
for x video in enumerate(video_list):
    v = pytube.Youtube(video)
    stream = v.streams.get_by_itag(22)
    print(f'Downloading video {x}....')
    stream.download()
    print('Done')