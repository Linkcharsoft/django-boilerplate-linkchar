# General information

Pre-config Django with django-rest-framework,corsheaders, user-profile model and autentication process (Login, Signup, Password reset, password, recovery...)
 
## Installation

Use the git clone command:

```bash
git clone https://github.com/Linkcharsoft/django-boilerplate-linkchar
cd django_base
```

It is highly recommended to use a [VirtualEnv](https://towardsdatascience.com/virtual-environments-104c62d48c54)

Create and complete a .env file with your app info (there is already a .env.example file).
In order to complete the "SECRET_KEY" field, you can use the default on .env.example but then you must run the following command and copy the given value on the .env file:
```bash
python manage.py get_secret_key
```

```bash
pip install -r requirements.txt
python manage.py migrate
```

### Other configurations

- On django admin site, on "sites" section, change "example.com" to your domain name (something like "google.com").

- Config Facebook/Google login on their respective sites and django admin. Here there is a [Tutorial](https://djangokatya.com/2020/08/12/another-django-all-auth-tutorial/):
 


## Available endpoints

- *Login*: require a username o email and a password as body params. It retrive a Token to identify the user on the system.

- *Signup*: require a email, username, password1, password2, first_name, last_name as body params. If everything is ok, it sent an email (pre-config to show it on console output), with a link to finish the signup process.

- *Resend email confirmation*: require a "email" as body params. Send a new email with a new link to finish the signup process.

- *Reset password*: require "new_password1" and "new_password2" as body params. If passwords are secure enough, the system save the input as a password for logged user.

- *Password recovery*: require a "email" as body params. It send a email with a six digit code to use in following endpoints.

- *Check token*: require a "email" and a six digit "token". It said if the token expired or is not valid for the user.

- *Password recovery confirm*: require a "email", "token", and "password". If token is valid for the user,  it save the new password. 

- *Get my user profile*: retrieve all user logged info.

- *Update user profile*: save the user and user profile new fields. You cannot modified some of them like "email o username".

## Contributing
- [Juan Ignacio Borrelli](https://www.linkedin.com/in/juan-ignacio-borrelli/)
- [Luca Cittá Guiordano](https://www.linkedin.com/in/lucacittagiordano/)
- [Matias Girardi](https://www.linkedin.com/in/matiasgirardi)

Both working on [Linkchar Software Development](https://linkchar.com/)


## License
[MIT](https://choosealicense.com/licenses/mit/)
