import yt_dlp
import sys
import time

def search_youtube(song_name):
    """Search YouTube and get the best available song link."""
    search_query = f"ytsearch:{song_name} official audio"
    
    options = {
        'quiet': True,
        'extract_flat': True,
        'default_search': 'ytsearch',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(search_query, download=False)
        if 'entries' in info and len(info['entries']) > 0:
            return info['entries'][0]['url']
    
    return None

def download_music(yt_url):
    """Downloads the audio from YouTube."""
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([yt_url])

def show_progress():
    """Simulates a download progress bar."""
    for i in range(0, 101, 10):
        sys.stdout.write(f"\rDownloading: {i}%")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nDownload complete!")

if __name__ == "__main__":
    song_name = input("Enter the song name: ")
    print("\nSearching for YouTube link...")
    
    yt_link = search_youtube(song_name)
    
    if yt_link:
        print(f"\nFound YouTube Link: {yt_link}")
        print("\nStarting download...")
        show_progress()
        download_music(yt_link)
    else:
        print("\nCould not find a suitable YouTube link.")
