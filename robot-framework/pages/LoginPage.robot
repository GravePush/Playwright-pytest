*** Settings ***
Resource   ../keywords/BaseKeywords.resource
Library    BuiltIn

*** Variables ***
${PAGE_NAME}   Login page
${USERNAME}    admin
${PASSWORD}    12345
    
*** Keywords ***
Open Login Page
    Open Page    ${PAGE_NAME}

Enter Username
    Log To Console    Enter username: ${USERNAME}
    
Enter Password
    Log To Console    Enter password: ${PASSWORD}
    
Click Submit
    Log To Console    Click on submit...

Login As Valid User
    Open Login Page
    Enter Username
    Enter Password
    Click Submit