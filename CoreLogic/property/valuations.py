from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime


class Valuations(Authentication):

    def __init__(self):
        super().__init__(False)
        self.base += "/avm"

    def test(self):
        print("testing")
    


if __name__ == "__main__":
    v = Valuations()
    v.test()