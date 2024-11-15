import requests
from moviepy.editor import VideoFileClip, AudioFileClip
video_url = "https://redirector.gv.cmnetworkusercontent.com/video?scope=streaming&itag=134&id=fnoGTfzBafg"
audio_url = "https://redirector.gv.cmnetworkusercontent.com/video?scope=streaming&itag=251&id=fnoGTfzBafg"
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
download_file(video_url, "video.mp4")
download_file(audio_url, "audio.webm")
video = VideoFileClip("video.mp4")
audio = AudioFileClip("audio.webm")
video = video.set_audio(audio)
video.write_videofile("video_con_audio.mp4", codec="libx264", audio_codec="aac")

