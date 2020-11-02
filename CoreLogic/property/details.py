from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from authentication import Authentication



class Details(Authentication):

    def __init__(self, country='au'):
        # variations: search, property, places, Location
        super().__init__()
        self.base += f'/property-details/{country}/properties'


    def property_attributes(self, pid):
        """
        Description: the attributes of the property COMBINED core and additional attribtues
        pid: unique property id in corelogic 
        returns: {
                    "propertyType": "HOUSE",
                    "propertySubType": "House",
                    "beds": 4,
                    "baths": 2,
                    "carSpaces": 2,
                    "lockUpGarages": 2,
                    "landArea": 860,
                    "isCalculatedLandArea": false,
                    "landAreaSource": "VG"
                    "airConditioned": true,
                    "airConditioningFeatures": "Ducted Gas Heating",
                    "ensuite": 1,
                    "floorArea": 156,
                    "roofMaterial": "Concrete Tile",
                    "wallMaterial": "Brick Veneer",
                    "yearBuilt": "1981"
                } 
        """
        
        core_endpoint = f'/{pid}/attributes/core'
        additional_endpoint = f'/{pid}/attributes/additional'

        try:
            core = requests.get(self.base + core_endpoint, headers=self.headers).json()
            additional = requests.get(self.base + additional_endpoint, headers=self.headers).json()
            res = {**core, **additional}

        except HTTPError as err:
            return err
        
        return res




if __name__ == "__main__":
    s = Search()

