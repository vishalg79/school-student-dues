import boto3

def add_message_insert_item(tableName, columnNames, columnValues):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName = 'school-db-updates'
    )

    queue.send_message(
        MessageBody = 'hello world',
        MessageAttributes = {
            'table' : {
                'DataType': 'String',
                'StringValue': tableName
            },
            'action': {
                'DataType': 'String',
                'StringValue': 'INSERT'        
            },
            'StudentId': {
                'DataType': 'Number',
                'StringValue': '2'
            },
            'ItemPurchased': {
                'DataType': 'String',
                'StringValue': 'EDC'
            },
            'Amount': {
                'DataType': 'Number',
                'StringValue': '50'
            },
            # 'columnNames': {
            #     [
            #         {
            #             'DataType': 'String',
            #             'StringValue': 'StudentId'
            #         },
            #         {
            #             'DataType': 'String',
            #             'StringValue': 'ItemPurchased'
            #         },
            #         {
            #             'DataType': 'String',
            #             'StringValue': 'Amount'
            #         }
            #     ]
            # },
            # 'columnValues': {
            #     'DataType': 'StringList',
            #     'StringListValues' : [
            #         columnValues
            #     ]
            # }
        }
    )

