import re
from urllib.request import urlopen
import chess
from chessboard import display


#txt = urlopen("https://api.chess.com/pub/player/jakeBeans/games/2023/05/pgn")

board = chess.Board()
text = str(board)

def cleanfile(filename):
    file = open(filename, "r+")
    txt = file.readlines()
    # file.truncate()
    clean = []
    for t in txt:
        # print(t[0])
        if t[0] == "1":
            clean.append(t)
    return clean

games = cleanfile("Games.pgn")
cleanedgames = []

for game in games:
    cleangame = re.sub(r' {[^}]*}', '', game) #found from google generative AI tool
    cleanedgames.append(cleangame)

for game in cleanedgames:

    moves = game.split()
    trash = []

    for move in moves:
        if "." in move:
            trash.append(move)
        elif "-" in move:
            trash.append(move)

    for t in trash:
        moves.remove(t)

    i = cleanedgames.index(game)
    cleanedgames.insert(i, moves)
    cleanedgames.remove(game)

# print(cleanedgames)
