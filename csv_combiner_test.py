import datatest as dt
import unittest
from mock import patch
from csv_combiner import *
import pandas as pd

accessoriesCsv = pd.read_csv("fixtures/accessories.csv")
clothingCsv = pd.read_csv("fixtures/clothing.csv")

class TestCsvCombiner(dt.DataTestCase):

    def test_GetArgs(self):
        testArgs = ["csv_combiner.py", "fixtures/accessories.csv", "fixtures/clothing.csv"]
        with patch.object(sys, 'argv', testArgs):
            args = GetArgs()
            assert args == ["fixtures/accessories.csv", "fixtures/clothing.csv"]

    def test_GetFiles(self):
        expectedList = [accessoriesCsv, clothingCsv]
        self.assertEqual(len(GetFiles(["fixtures/accessories.csv", "fixtures/clothing.csv"])), len(expectedList))

    def test_CreateNewCsv(self):
        self.assertValid(CreateNewCsv(GetFiles(["fixtures/accessories.csv", "fixtures/clothing.csv"])).columns, {'email_hash','category','filename'})
