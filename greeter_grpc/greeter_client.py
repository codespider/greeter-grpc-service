import grpc

from greeter_grpc import helloworld_pb2_grpc
from greeter_grpc import helloworld_pb2


def run(name):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print("Greeter client received: " + response.message)
