import pygame

def attach(euKombobulator):
    global euk,button,button_2,text
    euk = euKombobulator

    b_rect = euk.UI.get_box_grid_rect(pygame.Rect(0,0,3,1))
    button = euk.UI.Element.Button(b_rect)
    button.canvas.fill((255,0,0))
    euk.UI.add_element(button)

    b_rect = euk.UI.get_box_grid_rect(pygame.Rect(4,0,3,1))
    button_2 = euk.UI.Element.Button(b_rect)
    button_2.canvas.fill((255,0,0))
    euk.UI.add_element(button_2)

    b_rect = euk.UI.get_box_grid_rect(pygame.Rect(0,1,6,1))
    text = euk.UI.Element.Text(b_rect,"Hello, world!",(0,255,255),"./font/Solid-Mono.ttf")
    euk.UI.add_element(text)

    euk.UI.add_element(euk.UI.Element.EUK_Watermark(euk.UI.get_box_grid_rect(pygame.Rect(10,9,7,1))))

def update():
    button.canvas.blit(euk.utils.generate_default_button(button.size,button.pressed,button.hover),(0,0))
    button_2.canvas.blit(euk.utils.generate_default_button(button_2.size,button_2.pressed,button_2.hover),(0,0))
    if button.clicked:
        text.text = f"Button was clicked {button.n_clicked} times!"
        text.reload_text()
        #euk.load_scene("engine_intro")
    if button_2.clicked:
        euk.load_scene("engine_intro")