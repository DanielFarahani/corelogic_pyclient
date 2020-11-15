import requests
from datetime import datetime
from ..authentication import Authentication


class Details(Authentication):

    def __init__(self, country='au', env=""):
        # Docs: https://developer.corelogic.asia/apis/docs/property-details-au
        super().__init__(config=env)
        self.base += f'/property-details/{country}/properties'


    def property_attributes(self, pid):
        """
            Description: the attributes of the property COMBINED core and additional attribtues
            pid: unique property id in corelogic 
            returns: {"baths": 0,
                    "beds": 0,
                    "carSpaces": 0,
                    "isCalculatedLandArea": true,
                    "landArea": 0,
                    "landAreaSource": "string",
                    "lockUpGarages": 0,
                    "propertySubType": "string",
                    "propertySubTypeShort": "string",
                    "propertyType": "string"
                    "airConditioned": false,
                    "airConditioningFeatures": "string",
                    "decadeBuilt": "string",
                    "deck": "string",
                    "ductedHeating": false,
                    "ensuite": 0,
                    "fireplace": false,
                    "floorArea": 0,
                    "pool": false,
                    "roofMaterial": "string",
                    "salesGroupId": 0,
                    "salesGroupName": "string",
                    "siteCover": 0,
                    "solarPower": false,
                    "tennisCourt": 0,
                    "unitsOfUse": 0,
                    "wallMaterial": "string",
                    "yearBuilt": "string"} 
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

