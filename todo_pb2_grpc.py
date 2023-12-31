# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateData = channel.unary_unary(
                '/todo.MyService/CreateData',
                request_serializer=todo__pb2.CreateRequest.SerializeToString,
                response_deserializer=todo__pb2.Response.FromString,
                )
        self.ReadData = channel.unary_unary(
                '/todo.MyService/ReadData',
                request_serializer=todo__pb2.ReadRequest.SerializeToString,
                response_deserializer=todo__pb2.Response.FromString,
                )
        self.UpdateData = channel.unary_unary(
                '/todo.MyService/UpdateData',
                request_serializer=todo__pb2.UpdateRequest.SerializeToString,
                response_deserializer=todo__pb2.Response.FromString,
                )
        self.DeleteData = channel.unary_unary(
                '/todo.MyService/DeleteData',
                request_serializer=todo__pb2.DeleteRequest.SerializeToString,
                response_deserializer=todo__pb2.Response.FromString,
                )


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateData': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateData,
                    request_deserializer=todo__pb2.CreateRequest.FromString,
                    response_serializer=todo__pb2.Response.SerializeToString,
            ),
            'ReadData': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadData,
                    request_deserializer=todo__pb2.ReadRequest.FromString,
                    response_serializer=todo__pb2.Response.SerializeToString,
            ),
            'UpdateData': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateData,
                    request_deserializer=todo__pb2.UpdateRequest.FromString,
                    response_serializer=todo__pb2.Response.SerializeToString,
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteData,
                    request_deserializer=todo__pb2.DeleteRequest.FromString,
                    response_serializer=todo__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.MyService/CreateData',
            todo__pb2.CreateRequest.SerializeToString,
            todo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.MyService/ReadData',
            todo__pb2.ReadRequest.SerializeToString,
            todo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.MyService/UpdateData',
            todo__pb2.UpdateRequest.SerializeToString,
            todo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.MyService/DeleteData',
            todo__pb2.DeleteRequest.SerializeToString,
            todo__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
