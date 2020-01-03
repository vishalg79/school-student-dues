import boto3, json

def add_message_insert_item(tableName, columnNames, columnValues):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName = 'school-db-updates'
    )

    messageBody = {}
    messageBody['table'] = 'Students'
    messageBody['action'] = 'INSERT'
    messageBody['columns'] = [
        {
            'name': 'StudentId',
            'value': 2
        },
        {
            'name': 'ItemPurchased',
            'value': 'EDC'
        },
        {
            'name': 'Amount',
            'value': 50
        },
    ]

    queue.send_message(
        MessageBody = json.dumps(messageBody),
        MessageAttributes = {
            'body-format' : {
                'DataType': 'String',
                'StringValue': 'JSON'
            },
        }
    )

