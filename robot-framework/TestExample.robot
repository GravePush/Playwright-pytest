*** Settings ***
Library    BuiltIn
Library    Collections

*** Variables ***
@{NUMBERS}    10    25    7    3    40
@{A}    a    b    c
@{B}    1    2    3

&{USER}    name=Alice    age=22    role=admin
&{ITEM}    id=123    price=50

${VALUE}    10
${STRING}    qwerty

*** Keywords ***
Get Max Value From List
    [Arguments]    @{list}
    ${max_value}=    Evaluate    max([int(x) for x in ${list}])
    RETURN    ${max_value}

Combine Two Lists
    [Arguments]    ${list_1}    ${list_2}
    ${combine_lists}=    Combine Lists     ${list_1}    ${list_2}
    RETURN    ${combine_lists}

Check User Data
    [Arguments]    &{user_data}
    Dictionary Should Contain Key    ${user_data}    role
    Should Be Equal   ${user_data["role"]}    admin
    
Print Name
    [Arguments]    &{user_data}
    ${name}=    Set Variable    ${user_data["name"]}
    Dictionary Should Contain Key    ${user_data}    name
    Should Be Equal    ${name}    Alice
    Log To Console    ${name}

Update Item
    [Arguments]    &{item}
    ${updated_item}=    Set To Dictionary    ${item}    price    75
    Should Be Equal As Numbers    ${item["price"]}    75
    
    
Hello
    [Arguments]    ${name}
    Log To Console    Hello, ${name}
    
Show List Length
    [Arguments]    @{list}
    ${list_length}=    Get Length    ${list}
    Log To Console    ${list_length}

Print Message If Number Greater 10
    [Arguments]    ${number}
    Run Keyword If    ${number} >= 10    Log To Console    OK    ELSE    Log To Console    Too small

Repeat Message
    [Arguments]    ${text}
    Log To Console    ${text}

*** Test Cases ***
Print Numbers
    ${text}=    Catenate    @{NUMBERS}
    Log To Console    ${text}

Check Max Value From List Is 40
    ${max_value}=    Get Max Value From List    @{NUMBERS}
    Should Be Equal As Numbers    ${max_value}    40
Check Lists Combined
    ${list1}=    Create List    @{A}
    ${list2}=    Create List    @{B}
    ${combined_list}=    Combine Two Lists    ${list1}    ${list2}
    Length Should Be    ${combined_list}    6

Check Valid User Data
    Check User Data    &{USER}
    Print Name    &{USER}
    
Try Update Item
    Update Item    &{ITEM}
    
Say Hello
    Hello    Slepen
    
Get List Length
    Show List Length    @{NUMBERS}
    
Should Print When Number Greater Then 10
    Print Message If Number Greater 10    ${VALUE}
    
Should Repeat 3 Times
    Repeat Keyword    3    Repeat Message    ${VALUE}