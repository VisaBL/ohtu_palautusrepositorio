*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kallel
    Set Password  kalle456
    Set Confirmation  kalle456
    Submit Credentials
    Title Should Be    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    Set Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message    Username length should be at least 3 and contain only letters

Register With Valid Username And Invalid Password
    Set Username  kalllel
    Set Password  kalle
    Set Confirmation  kalle
    Submit Credentials
    Register Should Fail With Message    Password length should be min 8 and contain both letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kallelo
    Set Password  kalle456
    Set Confirmation  kalle457
    Submit Credentials
    Register Should Fail With Message    Passwords do not match

Login After Successful Registration
    Set Username  kallebest
    Set Password  kalle456
    Set Confirmation  kalle456
    Submit Credentials
    Go To Login Page
    Set Username  kallebest
    Set Password  kalle456
    Click Button  Login
    Main Page Should Be Open  
Login After Failed Registration
    Set Username  kallefail
    Set Password  kalle456
    Set Confirmation  kalle457
    Submit Credentials
    Go To Login Page
    Set Username  kallefail
    Set Password  kalle456
    Click Button  Login
    Page Should Contain    Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}