#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()

        if option1 == response or option2 == response or option3 == response:
            break

    return response


def valid_number_input(prompt):
    while True:
        try:
            response = input(prompt)

            if response.isdigit():
                break
        except ValueError:
            valid_number_input("How many rounds do you want to play?"
                               "(enter 0 to play until you quit)\n")

    return int(response)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def win(self):
        self.score += 1


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RockPlayer(Player):
    def learn(self, my_move, their_move):
        pass

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        pass

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def learn(self, my_move, their_move):
        pass

    def move(self):
        return valid_input("Rock, paper, scissors? > ",
                           "rock", "paper", "scissors")


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        my_move_index = moves.index(self.my_move)
        next_move_index = my_move_index + 1
        moves_len = len(moves)

        if next_move_index > moves_len - 1:
            next_move_index = 0

        return moves[next_move_index]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def rounds_number(self):
        self.rounds = valid_number_input("How many rounds do you want to play?"
                                         "(enter 0 to play until you quit)\n")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")

        if move1 == move2:
            print("\033[33;21m** ROUND TIE **\033[0m")
        elif beats(move1, move2):
            self.p1.win()
            print("\033[32;21m** PLAYER ONE WINS THIS ROUND **\033[0m")
        else:
            self.p2.win()
            print("\033[31;21m** PLAYER TWO WINS THIS ROUND **\033[0m")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"Score: Player One {self.p1.score}, "
              f"Player Two {self.p2.score}\n")

    def play_game(self):
        print("Game start!")
        print("Rock Paper Scissors, Go!\n")

        if self.rounds == 0:
            round = 0
            while True:
                print(f"Round {round}--:")
                self.play_round()
                round += 1
        else:
            for round in range(self.rounds):
                print(f"Round {round}--:")
                self.play_round()

            if self.p1.score > self.p2.score:
                print("\033[32;1m** PLAYER ONE WINS THE GAME!!! **\033[0m")
            elif self.p1.score < self.p2.score:
                print("\033[31;1m** PLAYER TWO WINS THE GAME!!! **\033[0m")
            else:
                print("\033[33;1m** ITS' A TIE!!! **\033[0m")

            print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.rounds_number()
    game.play_game()
