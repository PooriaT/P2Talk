# P2Talk

It is a simple python messenger which is written with `socket` module. There are two main code routines, one is the server, and the other is a client. First, each client should make a connection with the server. Then they can communicate via the available server.
To establish a socket connection, a pair of host and port should be defined.  
In server code, the host was defined `0.0.0.0`, which means that it is listening from all available interfaces. On the client-side, the port should be the same as the server-side, but the host should be defined based on the location of the server and client codes. For example, if both are located on the same machine, the host will be designated as a `localhost`.

### Data Encryption

Here, we are using `cryptography` module to provide the encryption for sent messages between clients.
First, it requires installing this module on your machine. To do so, you can establish a virtual environment for the directory you are working on:

```
python -m ven <virtualenv_name>
```

Then after activating the virtual environment, you have to install `cryptography` module:
```
pip install cryptography
```

For more information about this module, refer to its [official documents](https://cryptography.io/en/latest/).

## Running the application

To run the application, `server.py` should be run once on the server point, then `client.py` can run on any machine. Just note that if `client.py` is running on the machine where the `server.py` is not located, the `host` variable should change and refer to the public IP of the server-side.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
