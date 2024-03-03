# playlist.py
from pytube import YouTube
from pytube import Playlist
import interface


def process_data_playlist(url):
    url_Playlist = Playlist(url)
    actions = {
        1: lambda: find_out_video_url(url_Playlist),
        2: lambda: download_video_playlist(url_Playlist),
    }
    default_action = lambda: print("Processing data if data does not match any of the options")
    
    choice = int(input("1- find out the url of the video in the playlist, \n2- download all videos in the playlist: "))
        
    actions.get(choice, default_action)()
    
    question = input(f"Do you want to do something else? \n(y/n): ")
    if question.lower() =='y': 
        interface()
    elif question.lower() =='n' :
        print (f"BYE!")
    else:
        print("Processing data if data does not match any of the options")
 
def find_out_video_url(url_Playlist):
     try:
        yt = YouTube(url_Playlist)
        playlist_yt = yt.playlist
        print(f"Downloading playlist: {playlist_yt.title}")
        
        path = input("Enter the path to the folder where to download: ")
        
        for videos_url in playlist_yt.video_urls: 
               print("Title: ", yt.title, f"\n URL: ",videos_url)
        print("Download complete")
            
     except Exception as e:
        print("An error occurred: ", str(e))     
        
def download_video_playlist(url_Playlist):
    try:
        yt = YouTube(url_Playlist)
        playlist_yt = yt.playlist
        print(f"Downloading playlist: {playlist_yt.title}")
        
        path = input("Enter the path to the folder where to download: ")
        
        for video_url in playlist_yt.video_urls:
                video = YouTube(video_url)
                video.streams.first().download(path)
        print("Download complete")
        
    except Exception as e:
        print("An error occurred: ", str(e))
        
