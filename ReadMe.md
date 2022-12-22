# EMAIL SPAMMER DOCS

# Breaking Down the App

## gophish_linux /gophish_windows
- Has the gophish linux/windows binaries, extract one of them, depending on the OS version you are running and run before running the main application

## Mailhog
- Has mailhog binary for windows and linux. Depening on the OS version you are running, execute the corresponding.

## SRC
- This folder has the contents of the main application. In order to run the application, change directory to this folder and run the commands as instructed below:

# Steps to Running the Application.
Before running the email spammer app you need to have python version 3+,  gophish and Mailhog up and running,
follow the instructions below to achieve just that.

Additionally, you need to setup the Atlas mongodb database. Replace the given connection sting in `database` file, existing in the helpers folder.
Alternatively, edit the configuration file, with correct key-value pair, used when creating database instance.

# How to Setup Gophish
- Download & extract the release for your system, and run the binary.
- Build the binary with the following command:  ```go build```
- In case of any sqlite3 errors during building use the following command ```go env -w CGO_CFLAGS="-g -O2 -Wno-return-local-addr"``` 
- If you encounter port error use the following command:
    netsh http add iplisten ipaddress=::

- copy the URL to access the web application.
- Look the terminal once it is running to find the login credentials
    *username: admin*
    *password: randomly generated string* example: 0b3f78e370494356jhfdh

# How to setup Mailhog
- Download the correct version for your os and extract
- Run the executable or binary from its location

# Running the commandline application
- Use ```python app.py -h``` for help, this will list all the commads you need to interact with the application.
- View the web results by running ```python app.py web```



# Quick Steps to Interacting with the Application:
1. Start by creating a `Profile`
2. A `Landing page` should follow
3. Third, an `Email Template.`
4. Fourth create `Users & Groups`
5. Lastly, put together everything done and assemble the `Campaign`

- Note: Prepare needed information for each section, because you will need to make reference at each proceding stages.