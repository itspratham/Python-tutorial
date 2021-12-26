# How is a binary search tree implemented?

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self, root):
#         self.root = Node(root)
#
#     def pre_order(self, start, traversal):
#         if start:
#             traversal += str(start.value) + "-"
#             traversal = self.pre_order(start.left, traversal)
#             traversal = self.pre_order(start.right, traversal)
#         return traversal
#
#
#
# bt = BinaryTree(1)
# bt.root.left = Node(2)
# bt.root.right = Node(3)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
#
# print(bt.pre_order(bt.root, ""))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class BT:
#     def __init__(self, root):
#         self.root = Node(root)
#
#     def preorder(self, start, traversal):
#         if start:
#             traversal += str(start.value) + "-->"
#             traversal = self.preorder(start.left, traversal)
#             traversal = self.preorder(start.right, traversal)
#         return traversal
#
#
# bt = BT(1)
# bt.root.left = Node(2)
# bt.root.right = Node(3)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
#
# print(bt.preorder(bt.root, ""))
# rsult = {'Document_Type': 'DL', 'Status': 'success',
#          'Info': {'Name': ' U  ANKUSH KHURANA', 'Validity': '09/04/2035', 'Licence_number': 'DL0320150502057',
#                   'Address': ' ddn 15/90 BLOCK-15 VIKRAM VIHAR LAJPAT NAGAR-IV,DELHI 110024', 'Gender': ' ',
#                   'Issue_date': '10/04/2015', 'DOB': '14/07/1988', 'Pincode': '110024'}}
# maapp = {"Aadhar": "aadhar", "Passport": "passport", "VoterID": "voter", "DL": "license"}
# Doc_type_to_uniqeID_map = {"Pan": "Pan_number",
#                            "Aadhar": "Aadhaar_number",
#                            "Passport": "Passport_number",
#                            "DL": "Licence_number",
#                            "VoterID": "Voter_ID"}
#
# ekyc_sql = "insert into ekyc_response_table(kyc_key, type, response, uniqueId) values ('{}', '{}' , '{}', '{}')".format(
#     str(rsult["Info"][Doc_type_to_uniqeID_map[rsult['Document_Type']]]), maapp[rsult["Document_Type"]], str(
#         rsult["Info"]), str(rsult["Info"][Doc_type_to_uniqeID_map[rsult['Document_Type']]]))

# print(ekyc_sql)



