from pytube import YouTube

url = input('Enter the URL of the YouTube video to be downloaded : ')
video = YouTube(url)
print('Video Title : ', video.title)
print('Link for Video Thumbnail : ', video.thumbnail_url)
video = video.streams.get_lowest_resolution()
video.download()
