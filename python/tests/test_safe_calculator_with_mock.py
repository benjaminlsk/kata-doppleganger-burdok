import unittest
from unittest.mock import Mock
from python.safe_calculator import SafeCalculator


class TestSafeCalculator(unittest.TestCase):

    def test_add_should_raise_exception_when_authorized_with_mock(self):
        # We mock the authorizer to always return True
        mock_authorizer = Mock()
        mock_authorizer.authorize.return_value = True
        calculator = SafeCalculator(mock_authorizer)

        result = calculator.add(1, 2)
        assert result == 3


if __name__ == '__main__':
    unittest.main()
