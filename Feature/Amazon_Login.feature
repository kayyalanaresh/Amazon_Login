Feature: Working with Amazon login
  Scenario: Login into Amazon
    Given Launch the browser
    When Open Amazon Home Page
    Then Click First Accounts
    Then Enter the Email 07435592711
    And Click on Continue
    Then Enter the Password Chinna@767665
    Then Click on Login
    Then Click Second Accounts
    Then Click the Orders
    # Then Click Third Account
    Then Sign Out
    Then Browser Closing
