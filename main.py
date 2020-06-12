# Made by Krishnan Shankar and Shivam Suri
# Enjoy!
# Shivam presents this part.
import random

import pygame

from classes import Player, Bowler, Ball

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

W = 800
H = 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Cricket Game")
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (W, H))
PITCH = pygame.transform.scale(pygame.image.load("pitch.png"), (300, 200))
TIME_SINCE_BALL_DISPLAYED = 0
TOTAL_SCORE = 0


# Krishna presents this part.
def choose_random(player_status):
    if player_status == "swing1":
        return random.choice([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 6])
    elif player_status == "swing2":
        return random.choice([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6])


# Shivam presents this part
def redraw(win, player, bowler, ball):
    win.blit(BG, (0, 0))
    win.blit(PITCH, (250, 400))
    player.draw(win)
    bowler.draw(win)
    if ball:
        ball.draw(win)
    pygame.draw.line(win, (0, 0, 0), (379, 555), (379, 597), 6)
    pygame.draw.line(win, (0, 0, 0), (399, 550), (399, 597), 6)
    pygame.draw.line(win, (0, 0, 0), (419, 555), (419, 597), 6)
    pygame.draw.line(win, (0, 0, 0), (380, 550), (398, 550), 4)
    pygame.draw.line(win, (0, 0, 0), (400, 550), (418, 550), 4)
    pygame.display.flip()


# Krishna presents this part.
def main():
    global TIME_SINCE_BALL_DISPLAYED, TOTAL_SCORE
    player = Player(290, 460)
    bowler = Bowler(370, 330)
    ball = Ball(420, 340)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.swing()
                if event.key == pygame.K_p:
                    bowler.bowl()
        player.update()
        bowling = bowler.update()
        player_status = None
        if ball.y == 540:
            if player.swinging and player.swing_cnt < player.swing_time // 2:
                player_status = "swing1"
            elif player.swinging:
                player_status = "swing2"
        score = choose_random(player_status)
        if score:
            TOTAL_SCORE += score
            print(
                f"You hit a {'single' if score == 1 else ('double' if score == 2 else score)}! Your total score is {TOTAL_SCORE}")
        if bowling == "balldisp":
            TIME_SINCE_BALL_DISPLAYED = 1
            ball.start_move()
        ball_displayed = False
        if TIME_SINCE_BALL_DISPLAYED and TIME_SINCE_BALL_DISPLAYED > 0:
            keep_moving = ball.continue_move()
            if keep_moving:
                TIME_SINCE_BALL_DISPLAYED += 1
                ball_displayed = True
                redraw(win, player, bowler, ball)
            else:
                TIME_SINCE_BALL_DISPLAYED = 0
        if not ball_displayed:
            redraw(win, player, bowler, None)
        clock.tick(30)


if __name__ == "__main__":
    main()
