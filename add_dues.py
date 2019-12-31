import boto3, printCreds as creds

creds.printCurrCreds()

ddb = boto3.resource('dynamodb')
# assert isinstance(ddb, boto3.dynamodb)

students = ddb.Table('Students')
# assert isinstance(students, boto3.dynamodb.table.TableResource)

print(students.creation_date_time)

students.put_item(
    Item = {
        'StudentId' : 1,
        'ItemPurchased' : 'EDC',
        'Amount' : 10,
    }
)