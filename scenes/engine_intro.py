import pygame

def attach(euKombobulator):
    global euk,logo_img
    euk = euKombobulator

    imgsize = euk.utils.fit_image_retain_aspect_ratio([1920,1920],euk.resolution)
    logo_img = euk.UI.Element.Sprite(pygame.Rect((euk.resolution[0]/2-imgsize[0]/2,0,imgsize[0],imgsize[1])),"./logo.png")
    euk.UI.add_element(logo_img)
    
    euk.UI.add_element(euk.UI.Element.EUK_Watermark(euk.UI.get_box_grid_rect(pygame.Rect(10,9,7,1))))

def update():
    if euk.scene_frame**1.3 < 255:
        logo_img.canvas.set_alpha(255-euk.scene_frame**1.3)
    else:
        euk.load_scene("menu")