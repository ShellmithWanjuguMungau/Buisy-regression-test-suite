# Created by USER at 10/10/2025
Feature: User Settings-user role feature
  verify user can view,add,edit,delete a user role

  @single
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




    # Enter steps here