*** Settings ***
Library    BuiltIn
Resource   ../pages/LoginPage.robot

Suite Setup    Open App
Suite Teardown    Close App

*** Test Cases ***
Valid User Login
    Login As Valid User