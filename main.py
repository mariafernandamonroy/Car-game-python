import random
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
    #while(True):
    play_game(game, collection)
    #question = str(input(
    # "Quiere volver a jugar?
    #      [Si] o [No])
    #if question == "No": break
    #Borrar datos (set initial values (0))

def create_game(game, player, collection):
    print("Creando el juego ...")
    game_initialization(game)
    player_initialization(game, player, collection)


def game_initialization(game):
    game_id = str(input('Ingrese el id del juego (Puede contener letras y/o numeros): '))
    game_track_limit = float(input('Ingrese el límite de la pista en Km: '))
    game.set_id(game_id)
    game_track_limit_meters = game_track_limit * 1000
    game.set_track_limit(game_track_limit_meters)


def player_initialization(game, player, collection):
    players_name_string = str(input('Ingrese una lista de los nombres de los jugadores. (Eg: Zack,Brian,Harry,Tina): '))
    players_name_list = players_name_string.split(sep=',')
    for i in range(len(players_name_list)):
        player.set_player_name(players_name_list[i])
        player.set_car(i)
        player.set_rail(i)
        game.set_players(player.to_db_collection())
        collection.insert_one(game.to_db_collection())


def play_game(game, collection):

    winners = []
    winner_cont = 0
    print("Empezando el juego...")
    flag = True
    while flag:
        player_name, query_player_name, won_games, old_position_distance = star_game(collection)
        actual_position, game_track_limit = moving_forward(game, collection, query_player_name, old_position_distance)
        winners,winner_cont = end_game(player_name, actual_position, game_track_limit, winners, winner_cont)
        winners_positions(collection, query_player_name, winners, winner_cont)

def star_game(collection):
    global won_games, old_position_distance
    player_name = str(input('Ingrese el nombre del jugador que va a tirar el dado: '))
    query_player_name = {"players.player_name": player_name}
    game_by_player_name = collection.find(query_player_name)
    # print(game_by_player_name)
    for game_found in game_by_player_name:
        player_attributes = game_found['players']
        print(player_attributes)
        won_games = player_attributes.get("won_games")
        old_position_distance = player_attributes.get("position_distance")
        print("Tu carro es el número: ", player_attributes.get("car"))
    return player_name, query_player_name, won_games, old_position_distance

def moving_forward(game, collection, query_player_name, old_position_distance):
    print("***Tirando el dado...***")
    number_dice = random.randint(1, 6)
    print("El resultado del dado es: ", number_dice)
    distance = number_dice * 100
    actual_position = old_position_distance + distance
    game_track_limit = game.get_track_limit()
    if actual_position > game_track_limit:
        actual_position = game_track_limit
    update_position_distance = {"$set": {"players.position_distance": actual_position}}
    collection.update_many(query_player_name, update_position_distance)
    print("Tu posición actual es: ", actual_position)
    return actual_position, game_track_limit

def end_game(player_name, actual_position, game_track_limit, winners, winner_cont):
    if actual_position == game_track_limit:
        print("¡¡Ganaste!!")
        winners.append(player_name)
        print(winners)
        winner_cont = winner_cont + 1
    return winners,winner_cont

def winners_positions(collection, query_player_name, winners, winner_cont):
    if winner_cont == 1:
        update_won_games = {"$set": {"players.won_games": won_games+1}}
        collection.update_many(query_player_name, update_won_games)
        update_podium_position = {"$set": {"players.podium_position": 1}}
        collection.update_many(query_player_name, update_podium_position)
    elif winner_cont == 2:
        update_podium_position = {"$set": {"players.podium_position": 2}}
        collection.update_many(query_player_name, update_podium_position)
    elif winner_cont == 3:
        update_podium_position = {"$set": {"players.podium_position": 3}}
        collection.update_many(query_player_name, update_podium_position)
        print("El juego ha terminado: ")
        print("Primer puesto: ", winners[0],
              " Segundo puesto: ", winners[1],
              " Tercer puesto: ", winners[2])
        flag = False







if __name__ == '__main__':
    run()



