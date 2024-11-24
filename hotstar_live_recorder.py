import subprocess
import sys

# Configuration
cookies_file = "cleaned_hotstar_cookies_netscape.txt"
hotstar_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"

def fetch_hls_url():
    """
    Fetch the HLS stream URL using yt-dlp and cookies file.
    """
    print(f"Fetching HLS stream URL for: {hotstar_url}")
    try:
        # Construct the yt-dlp command
        command = [
            "yt-dlp",
            "--cookies", cookies_file,
            "-g", hotstar_url
        ]
        
        # Run the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check for errors
        if result.returncode != 0:
            print("Error fetching stream URL:")
            print(result.stderr)
            return None
        
        # Extract the HLS URL from stdout
        hls_url = result.stdout.strip()
        print(f"Successfully fetched HLS stream URL: {hls_url}")
        return hls_url
    
    except FileNotFoundError:
        print("Error: yt-dlp is not installed or not found in the system PATH.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    hls_url = fetch_hls_url()
    if hls_url:
        print(f"HLS Stream URL: {hls_url}")
        # Optionally, save the URL to a file or trigger recording logic here.

if __name__ == "__main__":
    main()
