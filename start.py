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
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0
selection = 100
valid_moves = []

# load in game piece images
def load_and_scale(filename, size):
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

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False

background = load_and_scale('wood4.jpg', (WIDTH-100, HEIGHT))

def draw_captured_pieces():
    x = WIDTH - 80  # Starting x position for captured pieces
    y = 20  # Starting y position for captured pieces
    piece_order = ['queen', 'rook', 'bishop', 'knight', 'pawn']

    for piece in piece_order:
        for img, captured in zip(small_white_images, captured_pieces_white):
            if piece in captured:
                screen.blit(img, (x, y))
                y += 50  # Move down for next piece

    x = WIDTH - 50  # Starting x position for captured pieces
    y = 20  # Starting y position for captured pieces

    for piece in piece_order:
        for img, captured in zip(small_black_images, captured_pieces_black):
            if piece in captured:
                screen.blit(img, (x, y))
                y += 50  # Move down for next piece


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 81.5 + 7 , white_locations[i][1] * 81.5 + 7))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 81.5 + 0, white_locations[i][1] * 81.5 + 0))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 75 + 5, white_locations[i][1] * 75 + 5,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 81.5 + 7, black_locations[i][1] *  81.5 + 7))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 81.5 + 0, black_locations[i][1] * 81.5 + 0))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 75 + 5, black_locations[i][1] * 75 + 5,
                                                  100, 100], 2)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))  # Draw the background image
    


    draw_pieces()
    draw_captured_pieces()
    pygame.display.flip()  # Update the display
    timer.tick(fps)  # Control the frame rate

pygame.quit()