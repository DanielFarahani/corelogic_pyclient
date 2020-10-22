from CoreLogic.property import (suggest, search, valuations)
import os, sys
import requests
import unittest
from . import UnitTest

class TestProperty(UnitTest):

    # gather some propertyIDs through suggestoin and search service to use in AVM service
    def suggestion_test(self):
        sug = suggest.Suggest()
        res = sug.suggest_places(suburbs[0])
        for info in res['suggestions']:
            sandbox_areas = info['postcodeId']

    def search_test(self):
        pass

    # Automated Valuation Model
    def avm_test(self):
        pass
