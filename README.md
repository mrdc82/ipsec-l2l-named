# IPSec Tunnel Report Generator

## Overview
The **IPSec Tunnel Report Generator** script extracts IPSec site-to-site VPN tunnel IPs, associates them with readable business names, and categorizes security types into a structured report. It automates login to a firewall device, retrieves tunnel information, processes the firewall configuration to identify associated names, and emails the final report.

## Features
- **Automated Data Retrieval**: Connects to a Cisco ASA firewall and extracts site-to-site VPN tunnel data.
- **Business Name Association**: Matches tunnel IPs with names by scanning the firewall configuration.
- **Security Categorization**: Organizes tunnels based on encryption and hashing protocols.
- **Report Generation**: Outputs a structured report with categorized VPN tunnels.
- **Email Integration**: Sends the final report via email.
- **File Cleanup**: Removes temporary files after execution.
- **Exception Handling**: Ensures smooth execution with error handling.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required modules:
  ```sh
  pip install netmiko pathlib2 smtplib
  ```

## Usage
1. Configure your ASA firewall IP and credentials within the script:
   - Update the firewall device IP (`host` in `cisco1` dictionary).
   - Provide login credentials (`username`, `password`, `secret`).
   - Configure email sender and receiver details in `send_mail()`.
2. Ensure you have a copy of the firewall configuration file.
3. Run the script:
   ```sh
   python ipsec_tunnel_report.py
   ```
4. The script will:
   - Retrieve IPSec tunnel data from the firewall.
   - Cross-check the firewall configuration file for business name associations.
   - Generate a structured output report.
   - Email the final report.
   - Cleanup temporary files.

## Example Output
```plaintext
IKEv1
Session Type: LAN-to-LAN

Connection : SOME-CUSTOMER-NAME   Index : 87570   IP Addr : 196.X.X.X  
Protocol : IKEv1  
IPsec Encryption : IKEv1: (1)AES256  IPsec: (2)AES128  
Hashing : IKEv1: (1)SHA1  IPsec: (2)SHA1  
Bytes Tx : 161012989   Bytes Rx : 321043987  
Login Time : 02:34:34 SAST Wed Aug 2 2023  
Duration : 14d 7h:25m:33s
```

## Customization
- Modify `send_mail()` to configure SMTP settings.
- Update `clean_files()` to adjust file handling if needed.

## Notes
- The script is efficient for extracting and formatting VPN tunnel data.
- Works with ASA firewalls that support site-to-site VPN tunnels.
- Basic but effective for organizing VPN configurations.

## License
This project is licensed under the MIT License.

## Author
Constantinos (Dino) Charalambous

