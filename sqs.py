import boto3

def add_message(tableName, action, actionAttributes):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName = 'school-db-updates'
    )

    queue.send_message(
        MessageBody = 'hello world',
        MessageAttributes = {
            'Table' : {
                'DataType': 'String',
                'StringValue': tableName
            },
            'Action': {
                'DataType': 'String',
                'StringValue': action                
            },
            'ActionAttributes': {
                'DataType': 'String',
                'StringListValues': [
                    
                ]   
            }
        }
    )

