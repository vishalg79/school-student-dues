import add_dues, sqs

# myEvent = {
#     'StudentId': 2,
#     'ItemPurchased': "EDC",
#     'Amount': 100
# }

# add_dues.add_student_dues(myEvent, None)

myTable = "Students"
myAction = "INSERT"
myActionAttributes = {
    'StudentId': 2,
    'ItemPurchased': "EDC",
    'Amount': 100
}

sqs.add_message(myTable, myAction, myActionAttributes)

# myActionAttributes = {
#     'key' : 'StudentId',
#     'keyValue' : 4,
#     'columns' : [
#         {
#             'name' : 'ItemPurchased',
#             'oldValue': None,
#             'newValue' : 'EDC'
#         },
#         {
#             'name' : 'Amount',
#             'oldValue': None,
#             'newValue' : 10
#         }
#     ]
# }
