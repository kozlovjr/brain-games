#!/usr/bin/env python3
from brain_games.games.even import even_game
from brain_games.games.even import description
from brain_games.main import main as main_game

def main():
    main_game(description, even_game)

if __name__ == '__main__':
    main(description, even_game)