# Running the application using Docker


# Running the application without Docker
## How to Setup Gophish
- Download & extract the release for your system, and run the binary.
- Build the binary with the following command:  ```go build```
- In case of any sqlite3 errors during building use the following command ```go env -w CGO_CFLAGS="-g -O2 -Wno-return-local-addr"``` 
- If you encounter port error use the following command:
    netsh http add iplisten ipaddress=::

- copy the URL to access the web application.
- Look the terminal once it is running to find the login credentials
    *username: admin*
    *password: randomly generated string* example: 0b3f78e370494356jhfdh
## How to setup Mailhog
- In windows OS just run the executable
- 


## How Run the main application