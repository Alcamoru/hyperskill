inp = str(input())
a = "scissors"
b = "paper"
c = "rock"
if inp != a and inp != b and inp != c:
    print("You don't chose a good word")
if inp == "scissors":
    print("Sorry, but computer chose rock")
if inp == "paper":
    print("Sorry, but computer chose scissors")
if inp == "rock":
    print("Sorry, but computer chose paper")
