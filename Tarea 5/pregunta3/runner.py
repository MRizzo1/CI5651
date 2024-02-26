import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.SysFont('Comic Sans MS', 28)
largeFont = pygame.font.SysFont('Comic Sans MS', 40)
moveFont = pygame.font.SysFont('Comic Sans MS', 60)

user = None
state = ttt.initial_state()
ai_turn = False
only_ai = False
board = state["board"]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe Mostro", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as -", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as |", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        playAIButton = pygame.Rect((width / 4), (height / 1.5), width / 2, 50)
        playAI = mediumFont.render("Watch AI vs AI", True, black)
        playAIRect = playAI.get_rect()
        playAIRect.center = playAIButton.center
        pygame.draw.rect(screen, white, playAIButton)
        screen.blit(playAI, playAIRect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O
            elif playAIButton.collidepoint(mouse):
                subtitle = mediumFont.render("Please wait...", True, white)
                subtitleRect = subtitle.get_rect()
                subtitleRect.center = ((width / 2), 100)
                screen.blit(subtitle, subtitleRect)

                time.sleep(0.2)
                user = ttt.X
                only_ai = True
    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(state)
        player = ttt.player(state)

        # Show title
        if game_over:
            winner = ttt.winner(state)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif only_ai:
            title = f"{ttt.player(state)} Playing"
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        if not only_ai:
            # Check for AI move
            if user != player and not game_over:
                if ai_turn:
                    time.sleep(0.5)
                    move = ttt.minimax(state)
                    state = ttt.result(state, move)
                    board = state["board"]
                    ai_turn = False
                else:
                    ai_turn = True

            # Check for a user move

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1 and user == player and not game_over:
                mouse = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if (ttt.valid_action(state, (i, j)) and tiles[i][j].collidepoint(mouse)):
                            state = ttt.result(state, (i, j))
                            board = state["board"]
        else:
            if not game_over:
                time.sleep(0.5)
                move = ttt.minimax(state)
                state = ttt.result(state, move)
                board = state["board"]

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    state = ttt.initial_state()
                    board = state["board"]
                    ai_turn = False

    pygame.display.flip()
