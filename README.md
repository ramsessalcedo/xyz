# xyz

xyz is a Discord bot written in .py that launches Distributed Denial of Service Attacks (DDOS) through an API. It also provides additional web tools.

### Requirements

xyz uses a number of open source projects to work properly:

* Python
* Pip 
* Linux based system

You will also need to register for an API at c99.nl for the web tools and at whatever DDoS host you have. Make sure these are changed in the .py file.

### Installation
xyz requires [Python](https://www.python.org/downloads/) 3.7+ to run.

xyz also uses a number of dependencies which can be installed by running the command below in the bot directory:
```sh
pip install -r requirements.txt
```

Lastly, change the API and webhook info found at the top of the .py file.

![Setup](https://i.imgur.com/wPm4P1Z.png)

### Commands

Below you will find a list of commands available in xyz. New commands are always being added.

*DDoS Commands (Layer 4)*

```sh
$attacktut - Gives the information below in any channel
$attack [host] [port] [time] [method] - Launches DDoS attack
```
> **Note:** This is meant for education purposes only. The methods available depend entirely on your API.

*Web Tools*
```sh
$portscan [ip] - Scans all ports of given host
$ping [ip] - Pings a host 4 times and shows the result
$geoip [ip] - Locates the given host/ip address
$geninfo [sex] - Generates random name address etc. (genders: male/female/all)
$checkweb [url] - Checks if a host is up or down
$ip2domain [ip] - Attempts to find websites hosted on the specific IP address
$phonelookup [areacode] + [number] - Get more information about any phone number
$urlshortener [url] - Shorts every long URL
```

*Misc*
```sh
$misc - Menu with all the misc commands
$rules - Bot usage rules
$tools - Menu with all the tools commands
$changelog - Provides info with recent changes 
$help - Menu with ALL the commands
```
