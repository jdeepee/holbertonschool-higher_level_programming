import requests, sys
from threading import Thread

class LoripsumThread(Thread):
    """docstring for LorIpsumThread"""
    def __init__(self, filename):
        self.filename = filename
        Thread.__init__(self)

    def run(self):
        reload(sys)
        sys.setdefaultencoding("latin-1")
        response = requests.get('http://loripsum.net/api/1/short')
        if response.status_code != 200:
            raise Exception("Failed to retrieve data")

        with open(self.filename, 'ab') as f:
            f.write(unicode(bytes(response.text)))
