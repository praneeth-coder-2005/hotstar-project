import json

def convert_to_netscape(json_file, output_file):
    """
    Converts a JSON cookies file to Netscape format for yt-dlp compatibility.
    """
    try:
        with open(json_file, 'r') as infile:
            cookies = json.load(infile)
        with open(output_file, 'w') as outfile:
            outfile.write("# Netscape HTTP Cookie File\n")
            for cookie in cookies:
                domain = cookie.get('domain', '')
                flag = 'TRUE' if cookie.get('hostOnly') else 'FALSE'
                path = cookie.get('path', '/')
                secure = 'TRUE' if cookie.get('secure') else 'FALSE'
                expiration = int(cookie.get('expirationDate', 0))
                name = cookie.get('name', '')
                value = cookie.get('value', '')
                outfile.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
        print(f"Converted cookies saved to {output_file}")
    except Exception as e:
        print(f"Error converting cookies: {e}")

if __name__ == "__main__":
    input_file = "hotstar_cookies.json"  # Input JSON cookies file
    output_file = "hotstar_cookies_netscape.txt"  # Output Netscape cookies file
    convert_to_netscape(input_file, output_file)
