# # listA = ["A", "BCD", [1,2,3,[4,5,6]]]

# # for item in listA:
# #     for i in item:
# #         print(i)
# #         for num in i:
# #             print(num)

# listA = ["A", "BCD", [1, 2, 3, [4, 5, 6,["Jorge"]]]]

# for item in listA:
#     if isinstance(item, list):
#         for i in item:
#             if isinstance(i, list):
#                 for num in i:
#                     print(num)
#             else:
#                 print(i)
#     else:
#         for char in item:
#             print(char)
#             for character in char:
#                 print(character)

listA = ['Deus', 'Jesus', 'Espirito Santo']
i = 0

while i < len(listA) :
    i += 1
    print(i)