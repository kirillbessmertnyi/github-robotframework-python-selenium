*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.saucedemo.com
${BROWSER}        headlesschrome

*** Test Cases ***
Valid Login
    [Tags]    270
    Init
    Open Browser To Login Page
    Input Username    standard_user
    Input Password    secret_sauce
    Submit Credentials
    Welcome Page Should Be Open    
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Swag Labs

Input Username
    [Arguments]    ${username}
    Input Text    user-name    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    login-button

Welcome Page Should Be Open
    Title Should Be    Swag Labs

Init
    Register Keyword To Run On Failure  Capture Page Screenshot With Unique Name

Capture Page Screenshot With Unique Name
    Capture Page Screenshot  Failure_${TestName}.png