# Tier 1 Help Desk Diagnostic Tool
# Aleck Sejourne 3/19/26

import platform
import socket
import shutil
from datetime import datetime

def run_diagnostics():
    print("Starting diagnostic scan...")
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        computer_name = socket.gethostname()
        ip = socket.gethostbyname(computer_name)
        os_info = platform.system() + " " + platform.release()

        total, used, free = shutil.disk_usage("/")
        gigs = free // (1024 * 1024 * 1024)

        try:
            socket.gethostbyname("google.com")
            internet = "Online"
        except:
            internet = "Offline"

        report = f"""
/  /  /  /  /
IT Diagnostic Report
Generated: {timestamp}
/  /  /  /  /

[System Information]
Computer Name:    {computer_name}
IP Address:       {ip}
OS:               {os_info}

[Disk Space]
Disk Space:       {gigs} GB

[Connectivity Check]
Internet Status:  {internet}
"""

        with open("diagnostic_report.txt", "w") as file:
            file.write(report)

        print("All done. Report saved to diagnostic_report.txt")

    except Exception as error_message:
        print("Something went wrong. Check error_log.txt")
        with open("error_log.txt", "w") as error_file:
            error_file.write("The script failed because: " + str(error_message))

run_diagnostics()