
import pygame

def attach(euKombobulator):
    global euk,world_segments,world_vertecies,scroll,debugtext,edscale,segmode,firstpoint,segtype
    euk = euKombobulator

    debugtext = euk.UI.add_element(euk.UI.Element.Text(euk.UI.get_box_grid_rect(pygame.Rect(0,0,17,1)),"Debug text",(255,255,255),"./font/Solid-Mono.ttf"))

    watermark = euk.UI.add_element(euk.UI.Element.EUK_Watermark(euk.UI.get_box_grid_rect(pygame.Rect(10,9,7,1))))
    watermark.canvas.set_alpha(128)

    scroll = [0,0]
    world_vertecies = []
    world_segments = []
    edscale = 30
    segmode = False
    firstpoint = False
    segtype = 0
    pygame.mouse.set_visible(False)

def update():
    global edscale,segmode,firstpoint,segtype
    gridpos_local = int(euk.input.mouse_position[0] / edscale), int(euk.input.mouse_position[1] / edscale)
    gridpos_local_smooth = (euk.input.mouse_position[0] / edscale)-0.5, (euk.input.mouse_position[1] / edscale)-0.5

    gridpos_global = gridpos_local[0]+int(scroll[0] / edscale),gridpos_local[1]+int(scroll[1] / edscale)
    debugtext.text = "Debug:"+str(edscale)+","+str(gridpos_local)+","+str(gridpos_global)+","+str(scroll)
    debugtext.reload_text()

    for y in range(0,euk.resolution[1]+edscale,edscale):
        for x in range(0,euk.resolution[0]+edscale,edscale):
            pos = x - (scroll[0]%edscale),y - (scroll[1]%edscale)
            pygame.draw.line(euk.display,(50,50,50),(pos[0],0),(pos[0],euk.resolution[1]))
            pygame.draw.line(euk.display,(50,50,50),(0,pos[1]),(euk.resolution[0],pos[1]))
    
    pos = -scroll[0]+(scroll[0]%edscale),-scroll[1]+(scroll[1]%edscale)
    pygame.draw.line(euk.display,(100,100,100),(pos[0],0),(pos[0],euk.resolution[1]))
    pygame.draw.line(euk.display,(100,100,100),(0,pos[1]),(euk.resolution[0],pos[1]))
    
    if scroll[0] < 0 or scroll[1] < 0:
        pygame.draw.circle(euk.display,(240,120,120),(int((gridpos_local[0]+1)*edscale)-int(scroll[0]%edscale),int((gridpos_local[1]+1)*edscale)-int(scroll[1]%edscale)),4)
    else:
        pygame.draw.circle(euk.display,(240,120,120),(int((gridpos_local[0])*edscale)-int(scroll[0]%edscale),int((gridpos_local[1])*edscale)-int(scroll[1]%edscale)),4)

    for i,s in enumerate(world_segments):
        try:
            p = world_vertecies[s[0]],world_vertecies[s[1]]
        except IndexError:
            world_segments.pop(i)
            break
        type = s[2]
        pos1 = (p[0][0]*edscale)-scroll[0],(p[0][1]*edscale)-scroll[1]
        pos2 = (p[1][0]*edscale)-scroll[0],(p[1][1]*edscale)-scroll[1]
        if type == 0:
            pygame.draw.line(euk.display,(180,180,180),pos1,pos2)
        elif type == 1:
            pygame.draw.line(euk.display,(240,80,80),pos1,pos2)

    for v in world_vertecies:
        pos = (v[0]*edscale)-scroll[0],(v[1]*edscale)-scroll[1]
        pygame.draw.circle(euk.display,(200,200,200),(pos),5)
        pygame.draw.circle(euk.display,(0,0,0),(pos),3)


    pygame.draw.circle(euk.display,(120,120,120),(((gridpos_local_smooth[0])*edscale),((gridpos_local_smooth[1])*edscale)),3)
    
    if euk.input.keyboard[pygame.K_UP]:
        scroll[1] -= 1
    elif euk.input.keyboard[pygame.K_DOWN]:
        scroll[1] += 1
    if euk.input.keyboard[pygame.K_LEFT]:
        scroll[0] -= 1
    elif euk.input.keyboard[pygame.K_RIGHT]:
        scroll[0] += 1
    if euk.input.keyboard[pygame.K_PLUS]:
        edscale = edscale + 1
    elif euk.input.keyboard[pygame.K_MINUS]:
        edscale = edscale - 1    

    for k in euk.input.key_click:
        if k == pygame.K_1:
            segtype = 0
        elif k == pygame.K_2:
            segtype = 1
        elif k == pygame.K_DELETE:
            for i,v in enumerate(world_vertecies):
                if v == gridpos_global:
                    world_vertecies.pop(i)
                    for si,s in enumerate(world_segments):
                        v1 = s[0]
                        v2 = s[1]
                        if v1 == i or v2 == i:
                            world_segments.pop(si)

    # Add vertex
    for b in euk.input.mouse_click:
        if b == 1:
            if len(world_vertecies) > 0:
                nv = False
                for v in world_vertecies:
                    if v == gridpos_global:
                        nv = True
                        break
                if not nv:
                    world_vertecies.append(gridpos_global)
            else:
                world_vertecies.append(gridpos_global)
                        
    # Add segment
    """
    for b in euk.input.mouse_click:
        if b == 3:
            if euk.input.mouse_button[2]:
                for i,v in enumerate(world_vertecies):
                    if v == gridpos_global:
                        if not segmode: 
                            firstpoint = world_vertecies[i]
                            print(firstpoint)
                            segmode = True
                        else:
                            if gridpos_global != firstpoint:
                                secondpoint = world_vertecies[i]
                                world_segments.append((firstpoint,secondpoint))
                                segmode = False
    """              
    for b in euk.input.mouse_click:
        if b == 3:
            if euk.input.mouse_button[2]:
                for i,v in enumerate(world_vertecies):
                    if v == gridpos_global:
                        if not segmode:
                            firstpoint = i
                            segmode = True
                        else:
                            if gridpos_global != world_vertecies[firstpoint]:
                                secondpoint = i
                                world_segments.append((firstpoint,secondpoint,segtype))
                                segmode = False