import os, sys
import requests
import unittest

sys.path.append('../')
from corelogic.property import (suggest, search, valuations)
from api_env_info import sandbox_env


class TestProperty(unittest.TestCase):
    def setup(self):
        """Setup runs before all test cases."""       
        self.suburbs_dict = dict()
        self.propertyIds_dict = dict()

    # Get suburb ids based on Sandbox data
    def suggestion_test(self):
        sug = suggest.Suggest()
        for states in sandbox_env['Australia']:
            for suburbs in sandbox_env['Australia'][states]:
                suggestions = sug.suggest_places(suburbs)['suggestions']

                if suggestions:
                    for suggestion in suggestions:
                        try:
                            self.suburbs_dict[suburbs].append(suggestion['localityId'])
                        except:
                            self.suburbs_dict[suburbs] = [suggestion['localityId']]

    # Get unique propertyIds for the Sandbox data
    def search_test(self):
        s = search.Search()
        for suburbs, codes in self.suburbs_dict.items():
            for code in codes:
                prop_list = s.property_search('locality', code)['_embedded']['propertySummaryList']
                for prop in prop_list:
                    prop = prop['propertySummary']
                    self.propertyIds_dict[prop['address']['singleLineAddress']] = prop['id']


    # Get valuation for peropertyIds
    def avm_test(self):
        v = valuations()


if __name__ == "__main__":
    unittest.main()