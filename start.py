import pygame

pygame.init()
WIDTH = 750
HEIGHT = 650
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Szachy Wikora Żabka')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# load in game piece images
def load_and_scale(filename, size):
    img = pygame.image.load(f'assets/{filename}')
    return pygame.transform.scale(img, size)

def load_and_scale2(filename, size):
    img = pygame.image.load(f'assets/{filename}')
    return pygame.transform.scale(img, size)


black_queen = load_and_scale('bQ.png', (80, 80))
black_queen_small = load_and_scale('bQ.png', (45, 45))
black_king = load_and_scale('bK.png', (80, 80))
black_king_small = load_and_scale('bK.png', (45, 45))
black_rook = load_and_scale('bR.png', (80, 80))
black_rook_small = load_and_scale('bR.png', (45, 45))
black_bishop = load_and_scale('bB.png', (80, 80))
black_bishop_small = load_and_scale('bB.png', (45, 45))
black_knight = load_and_scale('bN.png', (80, 80))
black_knight_small = load_and_scale('bN.png', (45, 45))
black_pawn = load_and_scale('bP.png', (65, 65))
black_pawn_small = load_and_scale('bP.png', (45, 45))

white_queen = load_and_scale('wQ.png', (80, 80))
white_queen_small = load_and_scale('wQ.png', (45, 45))
white_king = load_and_scale('wK.png', (80, 80))
white_king_small = load_and_scale('wK.png', (45, 45))
white_rook = load_and_scale('wR.png', (80, 80))
white_rook_small = load_and_scale('wR.png', (45, 45))
white_bishop = load_and_scale('wB.png', (80, 80))
white_bishop_small = load_and_scale('wB.png', (45, 45))
white_knight = load_and_scale('wN.png', (80, 80))
white_knight_small = load_and_scale('wN.png', (45, 45))
white_pawn = load_and_scale('wP.png', (65, 65))
white_pawn_small = load_and_scale('wP.png', (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

captured_pieces_white = ['pawn', 'pawn']
captured_pieces_black = ['pawn', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
turn_step = 0
selection = 100
valid_moves = []

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False






background = load_and_scale('wood4.jpg', (WIDTH-100, HEIGHT))
tlo = load_and_scale('tlo.jpeg', (100, HEIGHT))
def draw_captured_pieces():
    piece_order = ['queen', 'rook', 'bishop', 'knight', 'pawn']
    
    # Draw captured white pieces
    x_white = WIDTH - 100  # Starting x position for captured white pieces
    y_white = 20  # Starting y position for captured white pieces
    for piece in piece_order:
        count = captured_pieces_white.count(piece)
        for i in range(count):
            index = piece_list.index(piece)
            screen.blit(small_white_images[index], (x_white, y_white))
            y_white += 42  # Move down for the next piece
        y_white = 0  # Reset y position for the next type of piece

    # Draw captured black pieces
    x_black = WIDTH - 50  # Starting x position for captured black pieces
    y_black = 20  # Starting y position for captured black pieces
    for piece in piece_order:
        count = captured_pieces_black.count(piece)
        for i in range(count):
            index = piece_list.index(piece)
            screen.blit(small_black_images[index], (x_black, y_black))
            y_black += 42  # Move down for the next piece
        y_black = 0  # Reset y position for the next type of piece
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 81.5 + 7 , white_locations[i][1] * 81.5 + 7))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 81.5 + 0, white_locations[i][1] * 81.5 + 0))
        # if turn_step < 2:
        #     if selection == i:
        #         pygame.draw.rect(screen, 'red', [white_locations[i][0] * 75 + 5, white_locations[i][1] * 75 + 5,
        #                                          81.5, 81.5], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 81.5 + 7, black_locations[i][1] *  81.5 + 7))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 81.5 + 0, black_locations[i][1] * 81.5 + 0))
        # if turn_step >= 2:
        #     if selection == i:
        #         pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 81.5, black_locations[i][1] * 81.5,
        #                                           81.5, 81.5], 2)
        ################################# RYSOWANIE CZERWONEGO PROSTOKATA
    # if selection != 100:
    #     if turn_step < 2:
    #         x, y = white_locations[selection]
    #         pygame.draw.rect(screen, 'red', [x * 81.5, y * 81.5, 81.5, 81.5], 2)
    #     else:
    #         x, y = black_locations[selection]
    #         pygame.draw.rect(screen, 'blue', [x * 81.5, y * 81.5, 81.5, 81.5], 2)

 # ['queen', 'rook', 'bishop', 'knight', 'pawn']
def check_options(pieces, locations, turn):
    for i in pieces:
        if i ==  'queen':
            valid_moves = check_queen(locations, turn)
        if i ==  'rook':
            valid_moves = check_rook(locations, turn)
        if i ==  'bishop':
            valid_moves = check_bishop(locations, turn)
        if i ==  'knight':
            valid_moves = check_knight(locations, turn)
        if i ==  'pawn':
            valid_moves = check_pawn(locations, turn)
        if i ==  'king':
            valid_moves = check_king(locations, turn)
    return valid_moves




def friend_or_enemy(turn, locations, pieces):
    friends_list = white_pieces if turn == 'white' else black_pieces
    enemy_list = black_pieces if turn == 'white' else white_pieces



running = True
while running:
    timer.tick(fps)  # Control the frame rate 
    screen.blit(background, (0, 0))  # Draw the background image
    screen.blit(tlo, (650, 0))
    draw_pieces()
    draw_captured_pieces()
   
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0]
            y_coord = event.pos[1]
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                # przemieszczanie bialego na inna pozycje i bicie czarnego
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_black.append(black_pieces[black_piece])
                        draw_captured_pieces()
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'white')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step >= 2:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                # przemieszczanie czarnego na inna pozycje i bicie bialego
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[white_piece])
                        draw_captured_pieces()
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'black')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
     

    
    pygame.display.flip()  # Update the display

pygame.quit()