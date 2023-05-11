import pygame

def attach(euKombobulator):
    global euk,player_pos,player_img
    euk = euKombobulator

    player_pos = [0,0]
    player_img = euk.UI.add_element(euk.UI.Element.Sprite(pygame.Rect((0,0,32,32)),"./ball.png"))


def update():
    keys = euk.input.keyboard

    player_img.rect[0] = player_pos[0]
    player_img.rect[1] = player_pos[1]

    if keys[pygame.K_UP]:
        player_pos[1] -= 1
    elif keys[pygame.K_DOWN]:
        player_pos[1] += 1
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 1
    elif keys[pygame.K_RIGHT]:
        player_pos[0] += 1
    
    