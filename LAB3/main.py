import unittest
from scenarioOne import TestScenarioOne
from scenarioTwo import TestScenarioTwo
from scenarioThree import TestScenarioThree

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestScenarioOne('test_page_load'))
    suite.addTest(TestScenarioTwo('testValidLogin'))
    suite.addTest(TestScenarioTwo('testInvalidLogin'))
    suite.addTest(TestScenarioTwo('testEmptyUsername'))
    suite.addTest(TestScenarioTwo('testEmptyPassword'))
    suite.addTest(TestScenarioTwo('testSpecialCharactersInUsername'))
    suite.addTest(TestScenarioTwo('testSpecialCharactersInPassword'))
    suite.addTest(TestScenarioTwo('testCaseUppercaseUsername'))
    suite.addTest(TestScenarioTwo('testCaseUppercasePassword'))
    suite.addTest(TestScenarioThree('test_additional_feature'))

    unittest.TextTestRunner(verbosity=2).run(suite)
