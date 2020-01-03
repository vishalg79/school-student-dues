import add_dues, sqs

# myEvent = {
#     'StudentId': 2,
#     'ItemPurchased': "EDC",
#     'Amount': 100
# }

# add_dues.add_student_dues(myEvent, None)

myTable = "Students"
myColumnNames = ['StudentId', 'ItemPurchased', 'Amount']
myColumnValues = ['2', 'EDC', '100']
# myActionAttributes = {
#     'StudentId': 2,
#     'ItemPurchased': "EDC",
#     'Amount': 100
# }

sqs.add_message_insert_item(myTable, myColumnNames, myColumnValues)

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
