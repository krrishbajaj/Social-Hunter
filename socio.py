import argparse
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from colorama import init, Fore, Style
import concurrent.futures
import time
import pyfiglet
import random
import webbrowser
import os
import subprocess
import sys

def install_requirements():
    try:
        import requests  # Example dependency
    except ImportError:
        print("Missing dependencies detected. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")


# Initialize colorama
init(autoreset=True)

# ASCII Art Display
print()
print()
print("Welcome to Your Tool")
text = "Social Hunter"
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE]
ascii_art = pyfiglet.figlet_format(text, font="ansi_shadow")
chosen_color = random.choice(colors)
print(chosen_color + ascii_art + Style.RESET_ALL)

# Social media patterns
social_media_patterns = {
    'Facebook': r'facebook\.com/[a-zA-Z0-9_.-]+',
    'X (formerly Twitter)': r'twitter\.com/([a-zA-Z0-9_.-]+|@[a-zA-Z0-9_.-]+)',
    'LinkedIn': r'linkedin\.com/[a-zA-Z0-9_.-]+',
    'LinkedIn Custom': r'linkedin\.com/company/[a-zA-Z0-9_.-]+',
    'TikTok': r'tiktok\.com/@[a-zA-Z0-9_.-]+',
    'Instagram': r'instagram\.com/[a-zA-Z0-9_.-]+',
    'Reddit': r'reddit\.com/[a-zA-Z0-9_.-]+',
    'Pinterest': r'pinterest\.com/[a-zA-Z0-9_.-]+',
    'Flickr': r'flickr\.com/[a-zA-Z0-9_.-]+',
    'Snapchat': r'snapchat\.com/[a-zA-Z0-9_.-]+',
    'Vimeo': r'vimeo\.com/[a-zA-Z0-9_.-]+',
    'Quora': r'quora\.com/[a-zA-Z0-9_.-]+',
    'Medium': r'medium\.com/[a-zA-Z0-9_.-]+',
    'Tumblr': r'tumblr\.com/[a-zA-Z0-9_.-]+',
    'YouTube': r'youtube\.com/(channel|user)/[a-zA-Z0-9_.-]+',
    'YouTube Custom': r'youtube\.com/[a-zA-Z0-9_.-]+',
    'YouTube Short': r'youtu\.be/[a-zA-Z0-9_.-]+',
    'Generic Social Media': r'(twitter|facebook|linkedin)\.com/[a-zA-Z0-9_.-]+',
    'X Custom': r'x\.com/[a-zA-Z0-9_.-]+'
}

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(Fore.RED + f"Failed to fetch {url}: {e}")
        return None

def extract_social_media_links(html, base_url):
    if not html:
        return set()
    
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    social_links = set()

    for link in links:
        href = link['href']
        parsed_url = urlparse(href)
        
        if not parsed_url.scheme:  # Handle relative URLs
            href = base_url + href
        
        for platform, pattern in social_media_patterns.items():
            if re.search(pattern, href, re.IGNORECASE):
                social_links.add((platform, href))
                break
    
    return social_links

def read_subdomains(file_path):
    try:
        with open(file_path, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
        return subdomains
    except FileNotFoundError:
        print(Fore.RED + f"File not found: {file_path}")
        return []

def process_subdomain(subdomain):
    url = subdomain if subdomain.startswith(("http://", "https://")) else f"http://{subdomain}"
    print(Fore.YELLOW + f"Fetching {url}...")
    html = fetch_html(url)
    if html:
        base_url = urlparse(url).scheme + "://" + urlparse(url).netloc
        social_links = extract_social_media_links(html, base_url)
        if social_links:
            print(Fore.GREEN + f"Social media links found for {url}:")
            for platform, link in social_links:
                print(Fore.CYAN + f"{platform}: {link}")
        else:
            print(Fore.YELLOW + f"No social media links found for {url}.")
        return social_links
    return set()

def save_social_links_html(all_social_links, output_html):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Social Media Links</title>
        <link rel="icon" href="https://example.com/favicon.ico" type="image/x-icon">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f9; color: #333; }}
            h1 {{ color: #0056b3; text-align: center; }}
            .summary {{ margin: 20px 0; padding: 10px; background-color: #eaf7ff; border-left: 5px solid #0056b3; }}
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
            th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
            th {{ background-color: #0056b3; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            a {{ color: #0056b3; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            footer {{ margin-top: 20px; text-align: center; color: #888; }}
            .tooltip {{ position: relative; display: inline-block; }}
            .tooltip .tooltiptext {{ 
                visibility: hidden; 
                width: 140px; 
                background-color: black; 
                color: #fff; 
                text-align: center; 
                padding: 5px 0; 
                border-radius: 6px; 
                position: absolute; 
                z-index: 1; 
                bottom: 125%; 
                left: 50%; 
                margin-left: -75px;
                opacity: 0;
                transition: opacity 0.3s;
            }}
            .tooltip:hover .tooltiptext {{ visibility: visible; opacity: 1; }}
            .dark-mode {{ background-color: #1e1e1e; color: #ccc; }}
            .dark-mode table {{ color: white; }}
            .filter-bar, .pagination, .export-section {{ margin: 20px 0; }}
        </style>
        <script>
            function toggleDarkMode() {{
                document.body.classList.toggle('dark-mode');
            }}

            function searchTable() {{
                let input = document.getElementById("search").value.toUpperCase();
                let table = document.getElementById("socialTable");
                let tr = table.getElementsByTagName("tr");
                for (let i = 1; i < tr.length; i++) {{
                    let tdPlatform = tr[i].getElementsByTagName("td")[0];
                    let tdLink = tr[i].getElementsByTagName("td")[1];
                    if (tdPlatform || tdLink) {{
                        let platformText = tdPlatform.textContent || tdPlatform.innerText;
                        let linkText = tdLink.textContent || tdLink.innerText;
                        if (platformText.toUpperCase().indexOf(input) > -1 || linkText.toUpperCase().indexOf(input) > -1) {{
                            tr[i].style.display = "";
                        }} else {{
                            tr[i].style.display = "none";
                        }}
                    }}
                }}
            }}

            function copyToClipboard(link) {{
                navigator.clipboard.writeText(link).then(() => {{
                    alert("Copied to clipboard: " + link);
                }});
            }}
        </script>
    </head>
    <body>
        <h1>Social Media Links</h1>
        <div class="summary">
            <p>Total Platforms: {len(set(platform for platform, _ in all_social_links))}</p>
            <p>Total Links: {len(all_social_links)}</p>
            <p>Generated on: {timestamp}</p>
        </div>
        <div class="filter-bar">
            <input type="text" id="search" onkeyup="searchTable()" placeholder="Search for platforms or links..." />
            <button onclick="toggleDarkMode()">Toggle Dark Mode</button>
        </div>
        <table id="socialTable">
            <thead>
                <tr>
                    <th>Platform</th>
                    <th>Link</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
    """
    for platform, link in all_social_links:
        html_content += f"""
                <tr>
                    <td class="tooltip">{platform}
                        <span class="tooltiptext">Visit {platform}</span>
                    </td>
                    <td><a href="{link}" target="_blank">{link}</a></td>
                    <td><button onclick="copyToClipboard('{link}')">Copy</button></td>
                </tr>
        """
    html_content += """
            </tbody>
        </table>
        <footer>
            <p>Generated by Social Hunter Tool</p>
        </footer>
    </body>
    </html>
    """

    with open(output_html, 'w') as file:
        file.write(html_content)
    print(Fore.YELLOW + f"HTML report saved to {output_html}")
    webbrowser.open(output_html)

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Social Media Link Extractor")
    parser.add_argument("-i", "--input", required=True, help="Path to the file containing subdomains or a single target domain")
    parser.add_argument("-o", "--output", default="social_links.txt", help="Output file to save the results (default: social_links.txt)")
    parser.add_argument("--html", default="social_links.html", help="HTML file to save the results (default: social_links.html)")

    args = parser.parse_args()
    input_target = args.input
    output_file = args.output
    output_html = args.html

    start_time = time.time()

    # Read subdomains or single target
    if input_target.endswith('.txt'):
        subdomains = read_subdomains(input_target)
    else:
        subdomains = [input_target]

    if not subdomains:
        print(Fore.RED + "No valid targets to process.")
        return

    all_social_links = set()

    # Process subdomains concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(process_subdomain, subdomain): subdomain for subdomain in subdomains}
        for future in concurrent.futures.as_completed(future_to_subdomain):
            try:
                social_links = future.result()
                all_social_links.update(social_links)
            except Exception as e:
                print(Fore.RED + f"Exception occurred: {e}")

    # Save and display results
    end_time = time.time()
    execution_time = end_time - start_time
    print(Fore.YELLOW + f"Execution completed in {execution_time:.2f} seconds.")

    if all_social_links:
        print(Fore.GREEN + "Unique social media links found:")
        for platform, link in all_social_links:
            print(Fore.CYAN + f"{platform}: {link}")
        save_social_links_html(all_social_links, output_html)
    else:
        print(Fore.RED + "No social media links found.")

if __name__ == "__main__":
    main()
