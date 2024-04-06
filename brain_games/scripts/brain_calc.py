#!/usr/bin/env python3
from brain_games.games.calc import calc_game 
from brain_games.games.calc import description
from brain_games.main import main as main_game

def main():
    main_game(description, calc_game)

if __name__ == '__main__':
    main()