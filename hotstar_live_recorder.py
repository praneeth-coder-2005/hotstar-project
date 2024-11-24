import subprocess

# Replace this with your Hotstar video URL
video_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"

# The browser to extract cookies from (e.g., 'chrome', 'firefox', 'edge', etc.)
browser = "chrome"

# Command to fetch the HLS URL using yt-dlp with browser cookies
command = [
    "yt-dlp",
    "--cookies-from-browser", browser,
    "-g",  # Only print the URL
    video_url,
]

def fetch_hls_url():
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        hls_url = result.stdout.strip()
        print(f"Fetched HLS URL: {hls_url}")
        return hls_url
    except subprocess.CalledProcessError as e:
        print(f"Error fetching stream URL: {e.stderr}")
        return None

# Fetch and display the HLS stream URL
hls_url = fetch_hls_url()

if hls_url:
    print("You can now use this HLS URL with any media player or downloader.")
