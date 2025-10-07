# Created by USER at 06/10/2025
Feature: Login feature
  confirm that that the login functionality and any other feature on the login page works as expected.

  Scenario: Verify user can login successfully with correct credentials
    Given User opens buisy login page
    When enter correct email
    And enter correct password
#    And click login button
    And navigate to main login url
    Then confirm welcome is displayed

#  Scenario: Verify user cannot login with incorrect credentials
#    Given User opens buisy login page
#    When enter incorrect email
#    And enter incorrect password
#    Then Invalid credentials error message is displayed
#
#    Scenario Outline: Verify that changing language works
#      Given User opens buisy login page
#      When Click from the dropdown <Language>
#      Then confirm <welcome message> is displayed
#
#      Examples:
#        |Language   |welcome message                  |
#        |Swahili    |Tafadhali Ingiza Habari yako     |
#        |French     |Veuillez saisir vos informations |
#        |Portuguese |Insira suas informações          |


