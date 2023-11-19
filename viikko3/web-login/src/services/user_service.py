from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
              
        elif not re.match("^[a-zA-Z]{3,}$", username):
            raise UserInputError("Username length should be at least 3 and contain only letters")
        
        elif password != password_confirmation:
            raise UserInputError("Passwords do not match")
    
        elif not re.match("^(?=.*[a-zA-Z])(?=.*\d).{8,}$", password):
            raise UserInputError("Password length should be min 8 and contain both letters and numbers")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

       #Käyttäjätunnuksen on oltava merkeistä a-z koostuva vähintään 3 merkin pituinen merkkijono, joka ei ole vielä käytössä  
       #Salasanan on oltava pituudeltaan vähintään 8 merkkiä ja se ei saa koostua pelkästään kirjaimista

user_service = UserService()
