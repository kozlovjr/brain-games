#!/usr/bin/env python3
from brain_games.games.gcd import game_gcd
from brain_games.games.gcd import description
from brain_games.main import main as main_game

def main():
    main_game(description, game_gcd)

if __name__ == '__main__':
    main()