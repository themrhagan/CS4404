# CS4404 - Tools and Techniques in Network Security
## Mission 1: Is Multi-Factor a Non-Factor?
## Authors - Team 10

* **Matthew Hagan** - [SubBassBro](https://github.com/subbassbro)
* **Peter Maida** - [PeterMaidaRobot](https://github.com/PeterMaidaRobot)
* **Tim Winters** - [ArchdukeTim](https://github.com/ArchdukeTim)


## Files
### README.md
A basic README file listing the authors and the associated files.
### network_intercept.py
This script is used to intercept the authentication code being sent from the server to the client. It will modify any authentication codes passing through the middlebox by the defined algorithm. It requires the NetfilterQueue and Scapy packages and can be run with "python network_intercept.py".
### sms\_client_secure.py
This script is a secure client that receives, verifies, and decrypts an SMS authentication code. It requires the Pycrypto package and can be run with "python3 sms\_client_secure.py".
### sms\_client_unsecure.py
This script is an unsecure client that receives an SMS authentication code in plain text. It has no dependencies and can be run with "python3 sms\_client_unsecure.py".
### sms\_server_secure.py
This script is a secure server that encrypts, signs, and sends an SMS authentication code. It requires the Pycrypto package and can be run with "python3 sms\_server_secure.py".
### sms\_server_unsecure.py
This script is an unsecure server that sends an SMS authentication code in plain text. It has no dependencies and can be run with "python3 sms\_server_unsecure.py".
### mission1_report.pdf
This file is a report documenting the setup infrastructure on the class virtual missions in addition to a detailed description of this mission's implementation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thanks to Craig Shue for setting up a fun Mission 1.
