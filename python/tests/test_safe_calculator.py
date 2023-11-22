from safe_calculator import SafeCalculator


class SimpleAuthorizer:
    def authorize(self):
        return True


def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add
    calculator = SafeCalculator(authorizer=SimpleAuthorizer())
    result = calculator.add(1, 2)
    assert result == 3
