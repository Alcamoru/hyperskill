print("Input the number of cards:")
n_flashcards = int(input())
cards = {}
it = 0
while it < n_flashcards:
    print(f"The term for card #{i}:")
    term = input()
    print(f"The definition for card #{i}:")
    definition = input()
    cards[term] = definition
    n_flashcards += 1

for key, value in cards.items():
    print(f'Print the definition of "{key}":')
    answer = input()
    if answer == value:
        print("Correct!")
    else:
        print(f'Wrong. The right answer is "{value}".')

