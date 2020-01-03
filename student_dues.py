import boto3, printCreds as creds

# creds.printCurrCreds()

def add_student_dues(event, context) :
    ddb = boto3.resource('dynamodb')
    # assert isinstance(ddb, boto3.dynamodb)

    students = ddb.Table('Students')
    # assert isinstance(students, boto3.dynamodb.table.TableResource)

    # print(students.creation_date_time)

    # read values from event dictionary
    assert isinstance(event, dict)
    studentId = event.get('StudentId')
    itemPurchased = event.get('ItemPurchased')
    amount = event.get('Amount')

    students.put_item(
        Item = {
            'StudentId' : studentId,
            'ItemPurchased' : itemPurchased,
            'Amount' : amount,
        }
    )

    

