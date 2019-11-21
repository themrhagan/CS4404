# CS4404 - Tools and Techniques in Network Security
## Mission 2: Is Multi-Factor a Non-Factor?
## Authors - Team 1036

* **Matthew Hagan** - [SubBassBro](https://github.com/subbassbro)
* **Peter Maida** - [PeterMaidaRobot](https://github.com/PeterMaidaRobot)
* **Tim Winters** - [ArchdukeTim](https://github.com/ArchdukeTim)


## Files
### README.md
A basic README file listing the authors and the associated files.
### bombast folder
This folder holds the files for the Bombast server
#### index.html
This the the basic HTML file that the Bombast ISP hosts
#### server.py
Server.py is a python script resonsible for setting up a basic HTTP server on port 8080
### client
This folder is responsible for holding the client code.
#### client.py
client.py is responsible for making a client api call. to do so, it imports limits and RateLimitException
#### ratelimit.tar.gz
The require library files to make client.py work with ratelimiting
#### requests.tar.gz
The require library files to make client.py work with requests
### competitor folder
This folder holds the files for the competitor server
#### index.html
This the the basic HTML file that the competitor ISP hosts
#### server.py
Server.py is a python script resonsible for setting up a basic HTTP server on port 8080
### isp
the isp folder is responsible for holding the DNS forwarding and intercepting python scripts
#### dns_forward.py
dns_forward.py uses netfilterque and scrapy to forward DNS requests
#### dns_intercept.py
dns_intercept.py uses netfilterque and scrapy to forward DNS requests while also intecepting the files in the process to change them to the bombast ISP.
### mission2_report.pdf
This file is a report documenting the setup infrastructure on the class virtual missions in addition to a detailed description of this mission's implementation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thanks to Craig Shue for setting up a fun (and stressful) Mission 2.
