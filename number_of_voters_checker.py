
# initialization step where the candidates doesnt have votes
# it will store the values for the candidates votes
tinubu = 0
obi = 0
atiku = 0

# for loop, it loop the lgs form 1 to 3, and allow the user to inputs the values
for i in range(1, 3):
    print(f"votes for lg {i}: \n")
    tinubu = int(input("tinubu votes: \n"))
    obi = int(input("obi votes: \n"))
    atiku = int(input("Atiku votes: \n"))

# here its a dictionary  that will stor the vote count for each candidate
    candidate = {
        'Tinubu' :  tinubu,
        'Obi' : obi,
        'Atiku' : atiku
        }

# this blocks checks if the winner has  atleast for lgs and if winner has the highest votes 
    # if both conditions are met it will print the winner else it will print

    winner = max (candidate, key=candidate.get)

    if candidate[winner] >= 4 and all(candidate[winner] >= vote for vote in candidate.values()):
        
        print(f"{winner} is the winner with {candidate[winner]} votes.")
    else:
        print("\n no candidates meet the condition")