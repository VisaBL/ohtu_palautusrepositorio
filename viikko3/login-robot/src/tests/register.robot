*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  kalle  kalle123
# ...

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

# ...

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username too short


Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  ka$$€  kalle123
    Output Should Contain  Username does not contain valid letters

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  kalle  ka00s
    Output Should Contain  Password must be at least 8 marks long and contain at least one number and letter


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  kalle  kallebois
    Output Should Contain  Password must be at least 8 marks long and contain at least one number and letter

