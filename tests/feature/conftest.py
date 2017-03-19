from pytest_bdd import given, then


@given('I have a bar')
def bar():
    return 'bar'


@given('I have a repeatable bar', repeatable=True)
def repeatable_bar():
    # Maybe write 'bar' in some database for initialization, instead of creating a fixture object
    return None


@then('bar should have value "bar"')
def bar_is_bar(bar):
    assert bar == 'bar'
