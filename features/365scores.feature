Feature: Scores Results

  Scenario: Count 365scores results
    Given launch Chrome browser
    When open google
    Then search 365scores and count results
    When navigate by pages and check titles
    Then close browser