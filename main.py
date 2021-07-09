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
    print("si corre")


def create_game(game, player, collection):
    players = []
    game_id = str(input('Ingrese el id del juego (Puede contener letras y numeros): '))
    game_track_limit = str(input('Ingrese el límite de la pista en Km: '))
    players_name_string = str(input('Ingrese una lista de los nombres de los jugadores. (Eg: Zack,Brian,Harry,Tina): '))
    game.set_id(game_id)
    game.set_track_limit(game_track_limit)
    players_name_list = players_name_string.split(sep=',')
    for i in range(1,len(players_name_list)):
        player.set_player_name(players_name_list[i])
        player.set_car(i)
        player.set_rail(i)
        players.append(player)
        game.set_players(players)
        collection.insert_one(game)


if __name__ == '__main__':
    run()



