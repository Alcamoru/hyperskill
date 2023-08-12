# write your code here
print("Enter the number of friends joining (including you):")
n_friends = int(input())

if n_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = dict()
    for friend in range(n_friends):
        friends[input()] = 0

    print(friends)
