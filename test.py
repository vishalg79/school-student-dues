import student_dues, sqs

myEvent = {
    'Records': [
        {
            'StudentId': 1,
            'ItemPurchased': 'EDC',
            'Amount': 15
        },
        {
            'StudentId': 2,
            'ItemPurchased': 'Worksheet',
            'Amount': 20
        }
    ]
}

student_dues.add_student_dues(myEvent, None)

myQueueName = 'school-db-updates'
myTable = 'Students'

# sqs.add_message_insert_item(myQueueName, myTable, myEvent)

