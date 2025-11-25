*** Settings ***
Library    BuiltIn

*** Keywords ***
Open App
    Log To Console    Open app...

Close App
    Log To Console    Close app...

Open Page
    [Arguments]    ${page_name}
    Log To Console    Open ${page_name}...
