import unittest
from Search import SearchTest
from HomePage import HomePageTest

#This is to combine both testcases classes into one test suite.

# get all tests from HomePageTest class and SearchTest using testloader
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

# create a test suite combining search_test and home_page_test
all_tests = unittest.TestSuite([home_page_tests, search_tests])
# run the suite
unittest.TextTestRunner(verbosity=2).run(all_tests)


