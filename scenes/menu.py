import pygame

def attach(euKombobulator):
    global euk,button,button_2,text,text_xpos,text_ypos,text_global,button_start_game
    euk = euKombobulator

    button = euk.UI.add_element(euk.UI.Element.Button(euk.UI.get_box_grid_rect(pygame.Rect(1,1,1,1))))
    button_2 = euk.UI.add_element(euk.UI.Element.Button(euk.UI.get_box_grid_rect(pygame.Rect(4,0,3,1))))
    button_start_game = euk.UI.add_element(euk.UI.Element.Button(euk.UI.get_box_grid_rect(pygame.Rect(5,4,5,1))))
    text = euk.UI.add_element(euk.UI.Element.Text(euk.UI.get_box_grid_rect(pygame.Rect(0,2,6,1)),"Hello, world!",(0,255,255),"./font/Solid-Mono.ttf"))
    text_xpos = euk.UI.add_element(euk.UI.Element.Text(euk.UI.get_box_grid_rect(pygame.Rect(0,3,2,1)),"0.00",(255,255,255),"./font/Solid-Mono.ttf"))
    text_ypos = euk.UI.add_element(euk.UI.Element.Text(euk.UI.get_box_grid_rect(pygame.Rect(0,4,2,1)),"0.00",(255,255,255),"./font/Solid-Mono.ttf"))
    text_global = euk.UI.add_element(euk.UI.Element.Text(euk.UI.get_box_grid_rect(pygame.Rect(0,5,10,1)),"Message here",(255,255,255),"./font/Solid-Mono.ttf"))
    watermark = euk.UI.add_element(euk.UI.Element.EUK_Watermark(euk.UI.get_box_grid_rect(pygame.Rect(10,9,7,1))))
    watermark.canvas.set_alpha(128)

    if euk.get_global("button_clicks") > 0:
        text.text = f"Button was clicked {euk.get_global('button_clicks')-1} times!"
        text.reload_text()

def update():
    button.canvas.blit(euk.utils.generate_default_button(button.size,button.pressed,button.hovered),(0,0))
    button_2.canvas.blit(euk.utils.generate_default_button(button_2.size,button_2.pressed,button_2.hovered),(0,0))
    button_start_game.canvas.blit(euk.utils.generate_default_button(button_start_game.size,button_start_game.pressed,button_start_game.hovered),(0,0))

    if button.hovered:
        text_xpos.text = button.norm_cursor_position[0]
        text_xpos.reload_text()
        text_ypos.text = button.norm_cursor_position[1]
        text_ypos.reload_text()
    if button.clicked:
        text.text = f"Button was clicked {euk.get_global('button_clicks')} times!"
        text.reload_text()
        euk.set_global("button_clicks",euk.get_global("button_clicks")+1)
        #euk.load_scene("engine_intro")
    if button_2.clicked:
        euk.load_scene("engine_intro")

    if button_start_game.clicked:
        euk.load_scene("game")

    if euk.scene_frame > 60:
        text_global.text = euk.get_global("message")
        text_global.reload_text()