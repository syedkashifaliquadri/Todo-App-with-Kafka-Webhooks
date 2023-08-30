from concurrent import futures
import grpc
import todo_pb2_grpc
from app import todo_service
import config


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_MyServiceServicer_to_server(todo_service.MyServicer(), server)
    server.add_insecure_port('[::]:' + str(config.PORT))
    server.start()
    print("Server Start")
    server.wait_for_termination()
    print("Server terminat")


if __name__ == '__main__':
    serve()
