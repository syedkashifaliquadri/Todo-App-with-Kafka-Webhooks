import todo_pb2, todo_pb2_grpc
from db.db_connector import db_connector
from messaging.kafka_producer import KafkaProducer
import json
import psycopg2


class MyServicer(todo_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="kashif",
            host="localhost",
            port="5432",
            database="postgres",
        )

        self.producer = KafkaProducer()

    def CreateData(self, request, context):
        try:
            data = request.data

            task_id = db_connector.create_task(data)[0][0]

            self.producer.send_event("create", "Data created successfully")

            return todo_pb2.Response(reply="Data created successfully")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def ReadData(self, request, context):
        try:
            data = db_connector.get_all_tasks()
            if data:
                dict_data = [{'id': item[0], 'name': item[1]} for item in data]

                json_data = json.dumps(dict_data)

                self.producer.send_event("read", json_data)

                return todo_pb2.Response(reply=json_data)
            else:
                return todo_pb2.Response(reply="Data not found")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def UpdateData(self, request, context):
        try:
            task_id = db_connector.update_task(request)[0][0]

            self.producer.send_event("update", f"Data updated successfully now name: {request.data}")

            return todo_pb2.Response(reply=f"Data updated successfully now name: {request.data}")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def DeleteData(self, request, context):
        try:
            task_id = db_connector.delete_task(request)[0][0]

            self.producer.send_event('delete',
                                     f"Data deleted successfully against: {str(request.id)}")

            return todo_pb2.Response(reply=f"Data deleted successfully against: {str(request.id)}")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")
