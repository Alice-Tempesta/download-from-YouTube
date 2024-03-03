from pytube import YouTube
import requests
import interface


def process_data_video(url_video):
    try:
        yt_video = YouTube(url_video)
    
        print("Title: ", yt_video.title)
        print("Views: ", yt_video.views)
    
        actions = {
            1: lambda: download_video(yt_video),
            2: lambda: download_img(yt_video),
            3: lambda: download_only_sound(yt_video),
        }
        default_action = lambda: print("Processing data if data does not match any of the options")
    
        choice = int(input("1- download video, \n2- download image, \n3- download only sound: "))
        
        actions.get(choice, default_action)()
    
        question = input(f"Do you want to do something else? \n(y/n): ")
        
        if question.lower() == 'y': 
            interface.interface()
        elif question.lower() =='n':
            print (f"BYE!")
        else:
            print("Processing data if data does not match any of the options")
            
    except Exception as e:
        print("An error occurred: ", str(e))

def download_video(yt_video):
    try:
        
        yd = yt_video.streams.get_highest_resolution()
        
        path=input("Enter the path to the folder where to download: ")
        yd.download(path)
        
        print("Download complete")
    
    except Exception as e:
        print("An error occured: ", str(e))

def download_img(yt_video):
    try:
        thumbnail_url = yt_video.thumbnail_url
        print("djfdusjfghfksd")
        path=input("Enter the path to the folder where to download: ")
        name_img=input("Enter the name pic: ")
        thumbnail_path = path + f"\{name_img}.jpg"
        thumbnail_data = requests.get(thumbnail_url).content
        with open(thumbnail_path, 'wb') as thumbnail_file:
            thumbnail_file.write(thumbnail_data)
        
        print("Download complete. Thumbnail saved at:", thumbnail_path)
    
    except Exception as e:
        print("An error occured: ", str(e))
        
def download_only_sound(yt_video):
    try:
        audio_stream = yt_video.streams.get_audio_only()
        path=input("Enter the path to the folder where to download: ")
        audio_stream.download(path)
                   
        print("Download complete")
    
    except Exception as e:
        print("An error occured: ", str(e))
     