import os
import subprocess
from datetime import datetime

# Temporary directory for recordings
TMP_DIR = "./tmp"
os.makedirs(TMP_DIR, exist_ok=True)

def get_stream_url(hotstar_url):
    """
    Use yt-dlp to extract the HLS (.m3u8) stream URL from the Hotstar live stream,
    including cookies for authentication.
    """
    try:
        print(f"Fetching HLS stream URL for: {hotstar_url}")
        command = [
            "yt-dlp",
            "--cookies", "hotstar_cookies.txt",  # Use the cookies file
            "-g", hotstar_url
        ]
        hls_url = subprocess.check_output(command, text=True).strip()
        print(f"Stream URL fetched: {hls_url}")
        return hls_url
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error fetching stream URL: {e}")

def record_stream(hls_url, output_file):
    """
    Use FFmpeg to record the live stream continuously.
    """
    try:
        print(f"Starting recording. Output file: {output_file}")
        ffmpeg_command = [
            "ffmpeg", "-y", "-i", hls_url,
            "-c:v", "copy", "-c:a", "copy",
            "-f", "mp4", output_file
        ]
        subprocess.run(ffmpeg_command, check=True)
        print(f"Recording completed: {output_file}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"FFmpeg recording failed: {e}")

def main():
    # Hotstar live stream URL
    hotstar_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"

    # Fetch the HLS stream URL
    try:
        hls_url = get_stream_url(hotstar_url)
    except Exception as e:
        print(e)
        return

    # Prepare the output file name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(TMP_DIR, f"hotstar_live_{timestamp}.mp4")

    # Start recording
    try:
        record_stream(hls_url, output_file)
        print(f"Recording completed. File saved at: {output_file}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
