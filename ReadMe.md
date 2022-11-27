# EMAIL SPAMMER DOCS
Before running the email spammer app you need to have python version 3+,  gophish and Mailhog up and running,
follow the instructions below to achieve just that.

# How to Setup Gophish
- Download & extract the release for your system, and run the binary.
- Build the binary with the following command:  ```go build```
- In case of any sqlite3 errors during building use the following command ```go env -w CGO_CFLAGS="-g -O2 -Wno-return-local-addr"``` 
- If you encounter port error use the following command:
    netsh http add iplisten ipaddress=::

- Look the terminal once it is running fine for the login credentials
    *username: admin*
    *password: randomly generated string* example: 0b3f78e370494356jhfdh

# How to setup Mailhog
- Download the correct version for your os and extract
- Run the executable or binary from its location

# Running the commandline application
- Use ```python app.py -h``` for help
- View the web results by running ```python app.py web```
