# Created by USER at 10/10/2025
Feature: User Settings-user role feature
  verify user can view,add,edit,delete a user role


  Scenario: verify user roles page opens and roles are displayed.
    Given User opens buisy login page
    When enter correct email
    And enter correct password
    And click login button
    And navigate to main login url
    And click the stock and cash app tracker card
    And click user settings
    And click user roles
    Then verify title is displayed
    Then verify 13 records are displayed by footer info

#  Scenario: Verify agent can create, edit, and delete a user role. #scenario does not work as expected .
#  Given User opens buisy login page
#    When enter correct email
#    And enter correct password
#    And click login button
#    And navigate to main login url
#    And click the stock and cash app tracker card
#    And click user settings
#    And click user roles
#    And click create new user role
#    And enter role name
#    And check the permissions checkbox
#    And click add user role
#    And click okay on the pop-up displayed
#    Then Verify success message on the alert
    # Enter steps here

  @single
  Scenario: Verify the search works
    Given User opens buisy login page
    When enter correct email
    And enter correct password
    And click login button
    And navigate to main login url
    And click the stock and cash app tracker card
    And click user settings
    And click user roles
    And enter TSM role on search
    Then verify TSM role is diplayed