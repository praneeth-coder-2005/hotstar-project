import subprocess

# URL to fetch
hotstar_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"
cookies_file = "hotstar_cookies_netscape.txt"  # Ensure this file is in Netscape format

def fetch_hls_stream(url, cookies):
    try:
        # Run yt-dlp to get the HLS stream URL
        command = ["yt-dlp", "--cookies", cookies, "-g", url]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"HLS Stream URL: {result.stdout.strip()}")
        else:
            print(f"Error fetching stream URL: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(f"Fetching HLS stream URL for: {hotstar_url}")
    fetch_hls_stream(hotstar_url, cookies_file)
