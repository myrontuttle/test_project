Feature: Test an issue
  As a tester
  I want to have an issue for testing
  So that I can test functions in pycodegen

  Scenario: Issue Testing
    Given I have an issue in GitHub
    When I access that issue
    Then a test is created in code for it.
