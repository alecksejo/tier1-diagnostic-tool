# Tier1-Diagnostic-Tool
A Python script that automates the collection of system and network data to speed up help desk ticket resolution/troubleshooting. Instead of manually gathering system information one by one, you can run this script and get a full diagnostic report instantly.

## Report Contents
- Hostname and IP address
- Operating system version
- Available disk space
- Internet connectivity status
- Timestamp for accurate ticket logging
- Silent error handling so the script never crashes on the user

## Background
As I study for my CompTIA A+, I wanted to build something practical that mirrors what happens in a real help desk environment. Manually collecting system info during a support ticket waste time. I am still early in my Python journey but this script is a good example of what I have been working on. The script script automates that process and saves everything into a clean text file report in seconds. 

## Running The Script
1. Make sure Python is installed on the machine
2. Download diagnostic_tool.py
3. Open Command Prompt and navigate to the file location
4. Run: python diagnostic_tool.py
5. The report will be saved automatically as diagnostic_report.txt 

## Sample Output
![Diagnostic Report Output](diagnostic%20output%20screenshot.png)


(Note: The output shown was generated using the type command in Command Prompt. Ouput data has been sanitized to protect sensitive information.)
