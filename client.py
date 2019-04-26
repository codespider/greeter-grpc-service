import logging
import sys

from greeter_grpc import greeter_client

if __name__ == '__main__':
    logging.basicConfig()
    greeter_client.run(sys.argv[1])
