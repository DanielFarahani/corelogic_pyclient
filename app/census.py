from authentication import Authentication
import requests
from requests.exceptions import HTTPError


# under censusServices/ in future
class Census(Authentication):

    def __init__(self):
        super().__init__(False)
        self.url += "/statistics"

    def summary(self, location_id=12606, location_type_id=8):
        #TODO just push this to census as kwargs
        params = {
            'locationId': location_id,
            'locationTypeid': location_type_id
        }
        try:
            res = requests.get(self.url + "/census/summary", params=params, headers=self.headers).json().__dict__()
            
        except HTTPError as err:
            print(err)


# size, parks (#, %), age group, household, repayment (range/m), occupation type, median salary

    def census(
        self, 
        from_date="", 
        to_date="", 
        location_id=12606, 
        location_id_type=8, 
        metric_type_group_id=120, 
        metric_type_id=0
        ):

        payload = {
            'censusRequestList': [
                {
                    "fromDate": from_date,
                    "locationId": location_id,
                    "locationTypeId": location_id_type,
                    "metricTypeGroupId": metric_type_group_id,
                    "metricTypeId": metric_type_id,
                    "toDate": to_date
                }
            ]
        }

        try:
            res = requests.post(self.url + "/census", data=payload, headers=self.headers).json().__dict__()
            
        except HTTPError as err:
            print(err)