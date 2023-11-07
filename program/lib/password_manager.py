# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

class PasswordManager():
    def __init__(self):
        self.password_dict = dict()


    def add(self, service, password):
        # Check password is 8 characters long
        # Check password contains `!@$%&`
        # Add password if passes above criteria
        self.service = service
        self.password = password

        if len(self.password) >= 8 and any (char in "!@$%&" for char in self.password):
            self.password_dict[self.service] = self.password
            #print(self.password_dict)
            return self.password_dict
        else:
            #print(self.password_dict)
            return self.password_dict
 


    def get_for_service(self, service):
        # check dictionary for service
        # if service requested exists, give password
        self.service = service
        if self.service in self.password_dict.keys():
            #print(self.password_dict[self.service])
            return self.password_dict[self.service]
        else:
            return None
          
            
    def list_services(self):
        # Append keys to a list for services
        #print(list(self.password_dict.keys()))
        return list(self.password_dict.keys())
        

password_manager = PasswordManager()
password_manager.add('gmail', '12ab5!678')   # Valid password
password_manager.add('facebook', '$abc1234') # Valid password
password_manager.add('twitter', '12345678')  # Invalid password, so ignored
password_manager.get_for_service('facebook')
#   '$abc1234'
password_manager.get_for_service('not_real')
#   None
password_manager.get_for_service('twitter')
#   None
#password_manager.list_services()
#   ['gmail', 'facebook']
#        




