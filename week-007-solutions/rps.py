import random

class Game:
    def __init__(self, rounds=3):
        self.winner = None
        self.rounds = rounds
        self.scoreboard = {
            'Human': 0,
            'Computer': 0, 
            'Tied': 0
        }    
    
    # other methods below
    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors',
        }
        turn = random.randint(0,2)
        return (turn, choices[turn])

    def human_turn(self):
        turn = (input("Please make a selection (R/P/S): ")).upper()

        if turn != "R" and turn != "P" and turn != "S":
            print(choice, "is an invalid choice. Try R, P or S.")
            return human_turn()

        middleware = {
            'R': 0,
            'P': 1,
            'S': 2
        }

        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors',
        }
        turn = middleware[turn]
        return (turn, choices[turn])
    

    def compare_turns(self, computer, human):
        if human[0] - computer[0] == 1 or human[0] - computer[0] == -2:
            print(human[1].upper(), "(human)", "beats", computer[1].upper(), "(computer)")
            return "Human Wins!!!"
        elif human[0] - computer[0] == -1 or human[0] - computer[0] == 2:
            print(computer[1].upper(), "(computer)", "beats",  human[1].upper(), "(human)")
            return "Computer Wins!!!"
        else:
            print("You both drew", human[1].upper(), "-play again")
            return "You tied!!! Play Again."
        
    def play(self):
        while self.rounds > 0:
            human = self.human_turn()
            computer = self.computers_turn()
            winner = self.compare_turns(computer, human)
            if 'Human' in winner:
                self.scoreboard['Human'] += 1
                self.rounds -= 1
            elif 'Computer' in winner:
                self.scoreboard['Computer'] += 1
                self.rounds -= 1
            else:
                self.scoreboard['Tied'] += 1
        return self.scoreboard


if __name__ == '__main__':
    rps = Game(3)
    rps.play()