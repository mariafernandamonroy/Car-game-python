import json

import database
from Game import Game
from Player import Player


def run():
    db = database
    game = Game()
    player = Player()
    db = db.get_database()
    collection = db.Car_Game_Players
    create_game(game, player, collection)
    start_game()


def create_game(game, player, collection):
    print("Creating the game ...")
    game_initialization(game)
    player_initialization(game, player, collection)


def game_initialization(game):
    game_id = str(input('Ingrese el id del juego (Puede contener letras y numeros): '))
    game_track_limit = str(input('Ingrese el límite de la pista en Km: '))
    game.set_id(game_id)
    game_track_limit_meters = game_track_limit * 1000
    game.set_track_limit(game_track_limit_meters)


def player_initialization(game, player, collection):
    players = []
    players_name_string = str(input('Ingrese una lista de los nombres de los jugadores. (Eg: Zack,Brian,Harry,Tina): '))
    players_name_list = players_name_string.split(sep=',')
    for i in range(len(players_name_list)):
        player.set_player_name(players_name_list[i])
        player.set_car(i)
        player.set_rail(i)
        players.append(player.to_db_collection())
        game.set_players(players)
    collection.insert_one(game.to_db_collection())


if __name__ == '__main__':
    run()



