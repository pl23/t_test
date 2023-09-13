
import getpass
import json
import pygame
import random



#content 
system_name = getpass.getuser()

#loads files in to memory
game_board_filename = "game_board.json"
pieces_filename = "pieces.json"
with open(game_board_filename, 'r') as data:
    new_game_board = json.load(data)
with open(pieces_filename, 'r') as data:
    game_pieces = json.load(data)

#board = new_game_board


def copy_board(board):
    output = []
    for row in board:
        new_row = []
        for pixel in row:
            new_row.append(pixel)
        output.append(new_row)
    return output


pygame.init()
clock = pygame.time.Clock()

# Set up display
window_titel = "My Pygame"
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(window_titel)
FPS = 60
board_height = 20
board_width = 10
cell_height = 10
cell_width = 10


def update():
    screen.fill((0, 0, 0))
    draw(new_game_board, 30, 30)


def draw(board, x_off, y_off, coller=[255, 255, 255]):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            cell_y = y * cell_height + y_off
            cell_x = x * cell_width + x_off
            if cell == 1:
                pygame.draw.rect(screen, coller,
                                 (cell_x, cell_y, cell_width, cell_height))


tetris_board = new_game_board['board']

# Update a specific cell (e.g., row 2, column 3) to indicate a block
row = 2
column = 3
new_value = 1
tetris_board[row][column] = new_value

# Print the updated board (optional)
#print(tetris_board)
# Main game loop


def run():
    running = True
    x = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()

        clock.tick(FPS)
        pygame.display.flip()
        x += 1
    pygame.quit()

def test():
    get_key()

#run()
test()