from video import process_data_video
from playlist import process_data_playlist

def interface():
    question = input(f"Do you want to work with a playlist(p) or video(v)? \n(p/v): ")
    
    if question.lower() == 'p': 
        url_playlist = input("Enter playlist URL: ")
        process_data_playlist(url) 
        
    elif question.lower() == 'v':
        url = input("Enter the YouTube URL: ")
        process_data_video(url) 
    else:
        print("Processing data if data does not match any of the options")