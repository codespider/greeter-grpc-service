import logging

from greeter_grpc import greeter

if __name__ == '__main__':
    logging.basicConfig()
    greeter.serve()
