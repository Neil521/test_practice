import pytest
class TestSample:
   @pytest.fixture()
   def count(self):
       print('init count')
       return 10
   def test_answer(self, count):
       print('get count %s' % count)
       assert count == 10