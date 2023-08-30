import grpc
import todo_pb2, todo_pb2_grpc
import config


def create_data(stub, data):
    response = stub.CreateData(todo_pb2.CreateRequest(data=data))
    print("Create:", response.reply)


def read_data(stub, id):
    response = stub.ReadData(todo_pb2.ReadRequest(id=id))
    print("Read:", response.reply)


def update_data(stub, id, data):
    response = stub.UpdateData(todo_pb2.UpdateRequest(id=id, data=data))
    print("Update:", response.reply)


def delete_data(stub, id):
    response = stub.DeleteData(todo_pb2.DeleteRequest(id=id))
    print("Delete:", response.reply)


def run():
    try:
        channel = grpc.insecure_channel('localhost:' + str(config.PORT))
        stub = todo_pb2_grpc.MyServiceStub(channel)
        print("1. create_data")
        print("2. read_data")
        print("3. update_data")
        print("4. delete_data")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            data = input("Enter the Name: ")
            create_data(stub, data=data)
        elif rpc_call == "2":
            read_data(stub, id='1')
        elif rpc_call == "3":
            id = input("Enter the id: ")
            data = input("Enter the new name: ")
            update_data(stub, id=id, data=data)
        elif rpc_call == "4":
            id = input("Enter the id: ")
            delete_data(stub, id=id)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    run()
