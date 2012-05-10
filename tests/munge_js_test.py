import os.path
import unittest
import munge_js

class TestCase(unittest.TestCase):
    pass

TestCase.assert_false = TestCase.assertFalse
TestCase.assert_equal = TestCase.assertEqual

fixture_root = os.path.join(os.path.dirname(__file__), 'fixtures')

def get_fixtures():
    dir = os.path.join(fixture_root, 'input')
    files = os.listdir(dir)
    files.sort()
    names = [file[0:len(file)-3] for file in files if file.endswith('.js')]
    return names

class MungeJsTest(TestCase):
    pass

for fixture in get_fixtures():
    def test(self):
        with open(os.path.join(fixture_root, 'input', fixture + '.js')) as f:
            input = f.read()
        with open(os.path.join(fixture_root, 'output', fixture + '.js')) as f:
            expected = f.read()
        actual = munge_js.convert(input)
        self.assert_equal(expected, actual)
    
    setattr(MungeJsTest, 'test_' + fixture, test)

if __name__ == '__main__':
    unittest.main()
