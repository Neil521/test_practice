import unittest2 as unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./tests', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='.')
