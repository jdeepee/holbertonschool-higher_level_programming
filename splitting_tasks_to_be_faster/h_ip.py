import requests
from threading import Thread

class IPThread(Thread):
    """docstring for LorIpsumThread"""
    def __init__(self, ip, callback):
        self.ip = ip
        self.callback = callback
        Thread.__init__(self)

    def run(self):
        print "Search: " + str(self.ip)
        response = requests.get("https://api.ip2country.info/ip?" + str(self.ip))

        if response.status_code != 200:
            raise Exception("Failed to retrieve data")
            
        print response.json()["countryName"]
        self.callback(response.json()["countryName"])