# Created by USER at 06/10/2025
Feature: Login feature
  confirm that that the login functionality and any other feature on the login page works as expected.


  Scenario: Verify user can login successfully with correct credentials
    Given User opens buisy login page
    When enter correct email
    And enter correct password
    And click login button
    And navigate to main login url
    Then confirm welcome is displayed
    When click the stock and cash app traccker card


  Scenario: Verify user cannot login with incorrect credentials
    Given User opens buisy login page
    When enter incorrect email
    And enter incorrect password
    And click login button
    Then Invalid credentials error message is displayed


    Scenario Outline: Verify that changing language works
      Given User opens buisy login page
      When Click from the dropdown <Language>
      Then confirm <welcome message> is displayed

      Examples:
        |Language |welcome message                  |
        |SW       |Tafadhali Ingiza Habari yako     |
        |FR       |Veuillez saisir vos informations |
        |PT       |Insira suas informações          |

    @single
    Scenario: Verify that agent can access dashboard on login
    Given User opens buisy login page
    When enter correct email
    And enter correct password
    And click login button
    And navigate to main login url
    And click the stock and cash app tracker card
    Then Confirm that 9 cards are displayed


