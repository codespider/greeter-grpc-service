import logging
import os
from consul import Consul

CONSUL_REGISTRATION_ENABLED = os.environ.get('CONSUL_REGISTRATION_ENABLED', 'FALSE')
CONSUL_SERVICE_NAME = os.environ.get('CONSUL_SERVICE_NAME', 'greeter')
CONSUL_AGENT_HOST = os.environ.get('CONSUL_AGENT_HOST', '127.0.0.1')
CONSUL_AGENT_PORT = os.environ.get('CONSUL_AGENT_PORT', 8500)

if __name__ == '__main__':
    logging.basicConfig()
    if CONSUL_REGISTRATION_ENABLED == 'TRUE':
        print(f"registering with consul agent {CONSUL_AGENT_HOST}:8500")
        consul = Consul(host=CONSUL_AGENT_HOST, port=8500)
        consul.agent.service.register(CONSUL_SERVICE_NAME)
