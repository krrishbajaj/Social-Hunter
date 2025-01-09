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

## Tool INstalling Guide on Kali Linux, follow these steps:

## 1. Install Required Dependencies
Ensure Python and pip are installed if not run these:

1. sudo apt update
2. sudo apt install python3 python3-pip

# Then Run This Command: 

1. pip3 install -r requirements.txt

# Make the Tool Executable
If your tool is packaged as a Python script, make it executable

1. chmod +x social_hunter
   

# Run the Tool

1. python3 tool.py -i input.txt -o output.html
                       OR

./social_hunter -i input.txt -o output.html

# View the HTML Output
After execution, the tool generates an HTML file (e.g., output.html). Open it using a browser:

1. firefox output.html

## Usage
Run the following command:

Command: python social_hunter.py -i input.txt -o output.html


-i  -->  Single Domain   or  File path containing Subdomains

-o  --> Output Save
