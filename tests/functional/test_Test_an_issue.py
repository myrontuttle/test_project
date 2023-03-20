"""Test an issue feature tests."""

from pytest_bdd import given, scenario, then, when


@scenario("features\Test_an_issue.feature", "Issue Testing")
def test_issue_testing():
    """Issue Testing."""


@given("I have an issue in GitHub")
def _():
    """I have an issue in GitHub."""
    raise NotImplementedError


@when("I access that issue")
def _():
    """I access that issue."""
    raise NotImplementedError


@then("a test is created in code for it.")
def _():
    """a test is created in code for it.."""
    raise NotImplementedError
