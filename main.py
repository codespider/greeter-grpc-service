import logging
import os

PORT = os.environ.get('GREETING_SERVICE_PORT', 50051)

from greeter_grpc import greeter

if __name__ == '__main__':
    logging.basicConfig()
    greeter.serve(PORT)
