*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu toistaiseksi pois
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN_URL}

Go to Starting Page
    Go to  ${HOME_URL}

Go to Register Page 
    Go to  ${REGISTER_URL}

Register Page Should Be Open
    Title Should Be  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}