import random

class RockPaperScissor:
    def __init__(self, rounds=3):
        self.rounds = rounds
        self.score = {
            'human': 0,
            'computer': 0,
            'tie': 0
        }
    
    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors',
        }
        turn = random.randint(0,2)
        return (turn, choices[turn])
    
    def human_turn(self):
        choice = (input("Please make a selection (R/P/S): ")).upper()

        if choice != "R" and choice != "P" and choice != "S":
            print(choice, "is an invalid choice. Try R, P or S.")
            return self.human_turn(), '\n'

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
        choice = middleware[choice]
        return (choice, choices[choice])
    
    def compare_turns(self, computer, human):
        if human[0] - computer[0] == 1 or human[0] - computer[0] == -2:
            print(human[1].upper(), "(human)", "beats", computer[1].upper(), "(computer)")
            self.score['human'] += 1
            return "Human Wins!!!"
        elif human[0] - computer[0] == -1 or human[0] - computer[0] == 2:
            print(computer[1].upper(), "(computer)", "beats",  human[1].upper(), "(human)")
            self.score['computer'] += 1
            return "Computer Wins!!!"
        else:
            print("You both drew", human[1].upper(), "-play again")
            self.score['tie'] += 1
            return self.run()
    
    def run(self):
        while self.rounds > 0:
            human = self.human_turn()
            computer = self.computers_turn()
            self.compare_turns(computer, human)
            self.rounds -= 1
        return self.score
    
if __name__ == '__main__':
    rps = RockPaperScissor()
    rps.run()