def clean_netscape_cookies(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        outfile.write("# Netscape HTTP Cookie File\n")  # Add the header
        for line in infile:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip empty lines or comments
            
            fields = line.split()
            if len(fields) < 7:
                print(f"Skipping malformed line: {line}")
                continue

            # Parse fields
            domain, flag, path, secure, expiration, name, value = fields[:7]
            
            # Ensure expiration is a valid integer (fallback to 0 if not)
            try:
                expiration = str(int(float(expiration)))
            except ValueError:
                expiration = "0"
            
            # Fix spacing and write to output
            outfile.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")
    print(f"Cleaned cookies saved to {output_file}")


if __name__ == "__main__":
    input_file = "hotstar_cookies_netscape.txt"
    output_file = "cleaned_hotstar_cookies_netscape.txt"
    clean_netscape_cookies(input_file, output_file)
