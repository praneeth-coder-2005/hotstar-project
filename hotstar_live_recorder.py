import subprocess

def fetch_stream_url(cookies_file, hls_stream_url):
    """
    Fetches the HLS stream URL from Hotstar using yt-dlp and JSON cookies.
    """
    try:
        print(f"Fetching HLS stream URL for: {hls_stream_url}")
        yt_dlp_command = [
            "yt-dlp",
            "--cookies", cookies_file,
            "-g", hls_stream_url
        ]
        # Execute the yt-dlp command and capture output
        stream_url = subprocess.check_output(yt_dlp_command, text=True).strip()
        print(f"Stream URL: {stream_url}")
        return stream_url
    except subprocess.CalledProcessError as e:
        print(f"Error fetching stream URL: {e}")
        return None

def save_stream_to_file(stream_url, output_file):
    """
    Saves the fetched stream URL to an output file.
    """
    try:
        print(f"Saving stream URL to file: {output_file}")
        with open(output_file, 'w') as file:
            file.write(stream_url)
        print(f"Stream URL saved successfully to {output_file}")
    except IOError as e:
        print(f"Error saving stream URL to file: {e}")

if __name__ == "__main__":
    # Configuration
    cookies_file = "hotstar_cookies.json"  # JSON file containing cookies
    hls_stream_url = "https://www.hotstar.com/in/shows/bbs8-24x7-stream-deferred/1271327426/live/watch"
    output_file = "output.m3u8"  # Adjust the output file name as needed

    # Fetch the stream URL
    stream_url = fetch_stream_url(cookies_file, hls_stream_url)
    if stream_url:
        # Save the stream URL to an output file
        save_stream_to_file(stream_url, output_file)
