from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)


if __name__ == '__main__':
    API_KEY = '75ucap9az7urp8'
    API_SECRET = 'ZfyZ2nA1SEc8RIow'
    RETURN_URL = 'http://localhost:3000'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
                                            PERMISSIONS.enums.values())
    print authentication.authorization_url
    application = LinkedInApplication(authentication)
    
    authentication.authorization_code = 'AQSQ2RNtXTzC4r7NiV85HSE7Z1ouHrgLuErZatSIzliu2VzHjE7tPZ9f1dztSbQXCIYYyKWWH9mqzyGsJvvYHUVSOjTYFJiwd_vAe-zZ8MNNQf9Tkr8'
    token_info = authentication.get_access_token()

    print token_info
    
    application = LinkedInApplication(token=token_info)
    profile_data = application.get_profile()
    print profile_data


