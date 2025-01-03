# Social-Hunter
Social Hunter: A powerful tool to extract and analyze social media links from websites. It automates link detection, saves results in a visually appealing HTML report, and provides unique insights. Fast, user-friendly, and requires no programming knowledge. Ideal for researchers, marketers, and cybersecurity professionals.


# Social Hunter Tool

## Overview
Social Hunter Tool allows users to extract and analyze social media links from websites.

## Features
- Automatically identifies and extracts social media links.
- Provides results in a user-friendly HTML format.
- Works out-of-the-box with minimal setup.

## Installation
1. Download the executable file from the repository.
2. Run the tool directly without needing Python installed.

## Dependencies
The tool automatically installs required dependencies if they are missing.

## Usage
Run the following command:
```bash
social_hunter.exe -i input.txt -o output.html



Tool INstalling Guide on Kali Linux, follow these steps:

1. Install Required Dependencies
Ensure Python and pip are installed:

bash
Copy code
sudo apt update
sudo apt install python3 python3-pip
If the tool includes a requirements.txt file, install the dependencies:

bash
Copy code
pip3 install -r requirements.txt
2. Make the Tool Executable
If your tool is packaged as a Python script, make it executable:

bash
Copy code
chmod +x tool.py
If the tool is compiled (e.g., .sh, .bin, or a standalone executable), ensure it has execute permissions:

bash
Copy code
chmod +x social_hunter
3. Run the Tool
For a Python script:
bash
Copy code
python3 tool.py -i input.txt -o output.html
For a compiled executable:
Run it directly:

bash
Copy code
./social_hunter -i input.txt -o output.html
4. View the HTML Output
After execution, the tool generates an HTML file (e.g., output.html). Open it using a browser:

bash
Copy code
firefox output.html
5. Automate Dependency Installation (Optional)
If the tool automates dependency installation, ensure it runs with sudo permissions to avoid permission issues:

bash
Copy code
sudo python3 tool.py -i input.txt -o output.html
