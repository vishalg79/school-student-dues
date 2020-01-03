import boto3, json

def add_message_insert_item(queueName, tableName, record):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName = queueName
    )

    messageBody = {}
    messageBody['Table'] = 'Students'
    messageBody['Action'] = 'CREATE'
    messageBody['Records'] = [record]

    queue.send_message(
        MessageBody = json.dumps(messageBody),
        MessageAttributes = {
            'body-format' : {
                'DataType': 'String',
                'StringValue': 'JSON'
            },
        }
    )

