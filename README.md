This example was based on this well crafted article - https://testdriven.io/blog/fastapi-jwt-auth/

# Securing FastAPI with JWT Token-based Authentication

by Abdulazeez Abdulazeez Adeshina

# Set Secret

As an example:

```
>>> import os
>>> import binascii
>>> binascii.hexlify(os.urandom(24))
b'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'
```

Add to .env in root folder of proejct

As with PyCharm put the requirements.txt file in the root folder of the project/repo.


To Build:

```
plh@Arcturus fastapi-api-jwt % make local-build
docker build -t fastapi-app .
[+] Building 2.8s (11/11) FINISHED                                                                                           
 ...
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

To Run:

```
% make local-run
docker run -it --rm -p 127.0.0.1:8000:8000 fastapi-app
/usr/local/bin/python
INFO:     Started server process [9]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     172.17.0.1:55962 - "POST /login HTTP/1.1" 200 OK
INFO:     172.17.0.1:55966 - "GET /users HTTP/1.1" 200 OK
INFO:     172.17.0.1:55968 - "GET /posts HTTP/1.1" 200 OK
```

