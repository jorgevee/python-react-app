import random

class Node(object):
    test = 'test'
    def talk(self):
        return "Hello there, how are you?"

nobody = Node()
nobody.test
print(nobody.test)

Node.name = "Jorge"

print(nobody.name)


