import grpc

from greeter_grpc import helloworld_pb2_grpc
from greeter_grpc import helloworld_pb2


def run(server_host, port, name):
    with grpc.insecure_channel(f'{server_host}:{port}') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print("Greeter client received: " + response.message)
