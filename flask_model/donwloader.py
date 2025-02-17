import yt_dlp
import os

def download_video_part(url, start_time, end_time, output_filename):
    # Define the download options for yt-dlp
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': f'{output_filename}.%(ext)s',  # Output file name
        'quiet': False,  # Suppress logs except for errors
        'download_sections': [f'00:{start_time}-00:{end_time}'],  # Set the time range for the download
    }

    # Use yt-dlp to download the specific video part
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Downloaded the video part and saved as {output_filename}.mp4")

# Example usage
url = r'https://www.youtube.com/watch?v=sr52L-V7Yeo'
start_time = "00:36:36"
end_time = "00:37:36"
output_filename = 'mp4'

download_video_part(url, start_time, end_time, output_filename)
