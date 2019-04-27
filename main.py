import logging
import os
from consul import Consul
from greeter_grpc import greeter

PORT = os.environ.get('GREETING_SERVICE_PORT', 50051)
CONSUL_REGISTRATION_ENABLED = os.environ.get('CONSUL_REGISTRATION_ENABLED', 'FALSE')
CONSUL_SERVICE_NAME = os.environ.get('CONSUL_SERVICE_NAME', 'greeter')
CONSUL_AGENT_HOST = os.environ.get('CONSUL_AGENT_HOST', '127.0.0.1')
CONSUL_AGENT_PORT = os.environ.get('CONSUL_AGENT_PORT', 8500)

if __name__ == '__main__':
    logging.basicConfig()
    greeter.serve(PORT)
    if CONSUL_REGISTRATION_ENABLED == 'TRUE':
        consul = Consul(host=CONSUL_AGENT_HOST, port=CONSUL_AGENT_PORT)
        consul.Agent.Service.register(CONSUL_SERVICE_NAME)
