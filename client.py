import logging
import sys
import os
from greeter_grpc import greeter_client

HOST = os.environ.get('GREETING_SERVICE_HOST', 'localhost')
PORT = os.environ.get('GREETING_SERVICE_PORT', 50051)

if __name__ == '__main__':
    logging.basicConfig()
    greeter_client.run(HOST, PORT, sys.argv[1])
