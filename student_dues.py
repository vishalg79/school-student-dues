import boto3, sqs, printCreds as creds

# creds.printCurrCreds()

def add_student_dues(event, context):
    assert isinstance(event, dict)

    records = event.get("Records")

    ddb = boto3.resource('dynamodb')
    students = ddb.Table('Students')

    for record in records:
        assert isinstance(record, dict)
        students.put_item(
            Item = record
        )
        
        sqs.add_message_insert_item('school-db-updates', 'Students', record)
