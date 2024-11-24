import json

def convert_to_netscape(json_file, netscape_file):
    with open(json_file, 'r') as infile:
        cookies = json.load(infile)
    
    with open(netscape_file, 'w') as outfile:
        outfile.write("# Netscape HTTP Cookie File\n")
        for cookie in cookies:
            domain = cookie.get("domain", "")
            flag = "TRUE" if cookie.get("hostOnly", False) else "FALSE"
            path = cookie.get("path", "/")
            secure = "TRUE" if cookie.get("secure", False) else "FALSE"
            expiration = int(cookie.get("expirationDate", 0)) if "expirationDate" in cookie else "0"
            name = cookie.get("name", "")
            value = cookie.get("value", "")
            outfile.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
    
    print(f"Converted cookies saved to {netscape_file}")

# Input JSON file and output Netscape file
input_file = "hotstar_cookies.json"  # Your JSON file
output_file = "hotstar_cookies_netscape.txt"  # Output file in Netscape format

convert_to_netscape(input_file, output_file)
