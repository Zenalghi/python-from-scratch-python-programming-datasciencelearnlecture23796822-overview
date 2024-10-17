#Card and Deck Game playing
import itertools,random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
# print("="*50,"\n")
# # print(deck)
# # print("="*50,"\n")
# print("You got:")
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])
# print("="*50,"\n")
# print("You got:")