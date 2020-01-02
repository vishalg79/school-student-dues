import boto3

def add_message(action, actionAttributes):
    sqs = boto3.client('sqs')
    queue = sqs.get_queue_by_name(
        QueueName = 'school-db-updates'
    )

    response = queue.send_message(
        MessageBody = 'hello world',
        MessageAttributes = {
            'Table' : 'Students',
            'Action' : action,
            'ActionAttributes' : actionAttributes
        }
    )

    return response
