# hotstar_live_recorder.py

import subprocess
import sys

# URL of the Hotstar stream
hotstar_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"

# Path to the Netscape-formatted cookies file
cookies_file = "netscape.txt"

def fetch_hls_stream_url():
    try:
        # Run yt-dlp to fetch the HLS stream URL
        result = subprocess.run(
            ["yt-dlp", "--cookies", cookies_file, "-g", hotstar_url],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error fetching stream URL:", e.stderr.strip())
        sys.exit(1)

def record_stream(hls_url, output_file):
    try:
        # Record the stream using ffmpeg
        subprocess.run(
            ["ffmpeg", "-i", hls_url, "-c", "copy", "-bsf:a", "aac_adtstoasc", output_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error recording stream:", e.stderr.strip())
        sys.exit(1)

if __name__ == "__main__":
    print(f"Fetching HLS stream URL for: {hotstar_url}")
    hls_url = fetch_hls_stream_url()
    print(f"HLS stream URL fetched: {hls_url}")

    output_file = "recorded_stream.mp4"
    print(f"Recording stream to file: {output_file}")
    record_stream(hls_url, output_file)
    print("Recording complete.")
