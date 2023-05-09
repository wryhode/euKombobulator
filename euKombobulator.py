# euKombobulator
# 2022-2023
# wryhode
# 
# !! Uses several eval() !!
# Please check any project's scene names to determine if they pose a security risk!!

class euKombobulator():
    def __init__(self):
        self.settings = self.Settings().settings
        self.input = self.Input()

        self.resolution = self.settings["screen"]["resolution"]
        self.display = pygame.display.set_mode(self.resolution,pygame.SRCALPHA|pygame.RESIZABLE)
        pygame.display.set_caption("euKombobulator (preview version)")
        self.clock = pygame.time.Clock()
        self.target_framerate = self.settings["screen"]["target_framerate"]

        self.UI = self.UserInterface(self.resolution,self.settings["screen"]["box_size"])
        self.utils = self.Utilities()
        self.main_run_loop()

    class Settings():
        def __init__(self):
            self.file = open("./euk_settings.toml","r")
            self.settings = tomllib.loads(self.file.read())
            self.file.close()
    
    class Input():
        def __init__(self):
            self.mouse_position = [0,0]
            self.mouse_button = [False,False,False]
            self.keyboard = [None]

        def update(self):
            self.mouse_position = pygame.mouse.get_pos()
            self.mouse_button = pygame.mouse.get_pressed()
            self.keyboard = pygame.key.get_pressed()

    class Utilities():
        def fit_image_retain_aspect_ratio(self,image_resolution,target_resolution):
            image_aspect_ratio = image_resolution[0] / image_resolution[1]
            print(image_aspect_ratio)
            target_aspect_ratio = target_resolution[0] / target_resolution[1]
            if target_resolution[0] > target_resolution[1]:
                if image_resolution[0] > image_resolution[1]:
                    n_size = target_resolution[0],target_resolution[1]/target_aspect_ratio
                else:
                    n_size = target_resolution[0]/target_aspect_ratio,target_resolution[1]
            else:
                if image_resolution[0] > image_resolution[1]:
                    n_size = target_resolution[0],target_resolution[1]/target_aspect_ratio
                else:
                    n_size = target_resolution[0]/target_aspect_ratio,target_resolution[1]
            return n_size

        def generate_default_button(self,resolution,pressed = False,hover = False):
            btn_canvas = pygame.Surface(resolution)
            if pressed:
                pygame.draw.rect(btn_canvas,(150,150,150),(0,0,resolution[0],resolution[1]))
                pygame.draw.rect(btn_canvas,(50,50,50),(0,0,resolution[0],resolution[1]),5)
            elif hover:
                pygame.draw.rect(btn_canvas,(200,200,200),(0,0,resolution[0],resolution[1]))
                pygame.draw.rect(btn_canvas,(100,100,100),(0,0,resolution[0],resolution[1]),5)
            else:
                pygame.draw.rect(btn_canvas,(220,220,220),(0,0,resolution[0],resolution[1]))
                pygame.draw.rect(btn_canvas,(120,120,120),(0,0,resolution[0],resolution[1]),5)
            return btn_canvas

    class UserInterface():
        def __init__(self,resolution,box_size):
            self.box_grid = box_size
            self.elements = []
            self.size_box_grid(resolution)
        
        class Element():
            class Button():
                def __init__(self,rect):
                    self.rect = rect
                    self.size = self.rect[2],self.rect[3]
                    self.canvas = pygame.Surface(self.size)

                    self.hovered = False
                    self.pressed = False
                    self.clicked = False
                    self.n_clicked = 0

                def update(self,inputregister):
                    if self.rect.collidepoint(inputregister.mouse_position):
                        self.hover = True
                        if inputregister.mouse_button[0]:
                            if not self.pressed:
                                self.clicked = True
                                self.n_clicked += 1
                            else:
                                self.clicked = False
                            self.pressed = True
                        else:
                            self.pressed = False
                    else:
                        self.hover = False
                        self.pressed = False
                        self.clicked = False

            class Text():
                def __init__(self,rect,text,color,font_path,size=16):
                    self.rect = rect
                    self.size = self.rect[2],self.rect[3]
                    self.canvas = pygame.Surface(self.size)
                    self.font = pygame.font.Font(font_path,size)
                    self.text = text
                    self.color = color
                    self.canvas.blit(self.font.render(self.text,True,self.color),(0,0))

                def update(self,input):
                    pass

                def reload_text(self):
                    self.canvas = pygame.Surface(self.size)
                    self.canvas.blit(self.font.render(self.text,True,self.color),(0,0))

            class Sprite():
                def __init__(self,rect,image_path):
                    self.rect = rect
                    self.size = self.rect[2],self.rect[3]
                    self.imagepath = image_path
                    self.image_original = pygame.image.load(self.imagepath)
                    self.canvas = pygame.Surface(self.size)
                    self.canvas.blit(pygame.transform.scale(self.image_original,self.size),(0,0))

                def update(self,input):
                    pass
            
                def reload(self):
                    self.image_original = pygame.image.load(self.imagepath)
                    self.canvas = pygame.Surface(self.size)
                    self.canvas.blit(pygame.transform.scale(self.image_original,self.size),(0,0))

            class EUK_Watermark():
                def __init__(self,rect):
                    self.rect = rect
                    self.size = self.rect[2],self.rect[3]
                    self.canvas = pygame.Surface(self.size,pygame.SRCALPHA)
                    self.font = pygame.font.Font("./font/Solid-Mono.ttf",21)
                    self.canvas.blit(self.font.render("euKombobulator (preview version)",True,(255,255,255,100)),(0,0))

                def update(self,input):
                    pass

        def test_box_grid(self,canvas):
            cs = canvas.get_size()
            for y in range(self.box_grid[1]):
                for x in range(self.box_grid[0]):
                    pygame.draw.line(canvas,(100,128,100),(x*self.box_size[0],0),(x*self.box_size[0],cs[1]))
                    pygame.draw.line(canvas,(100,128,100),(0,y*self.box_size[1]),(cs[0],y*self.box_size[1]))
        
        def size_box_grid(self,resolution):
            self.box_size = [int(resolution[0]/self.box_grid[0]),int(resolution[1]/self.box_grid[1])]
        
        def get_box_grid_rect(self,rect):
            return pygame.Rect((self.box_size[0]*rect[0],self.box_size[1]*rect[1],self.box_size[0]*rect[2],self.box_size[1]*rect[3]))

        def add_element(self,element):
            self.elements.append(element)
            return element

        def update(self):
            for e in self.elements:
                e.update()
                
    def main_run_loop(self):
        self.scene = self.settings["scenes"]["startscene"]
        self.scenes = []
        self.scenes_str = []
        for s in os.listdir("./scenes"):
            if s.endswith(".py") and s != "__init__.py":
                self.scenes_str.append(s[:-3])
                self.scenes.append(eval(s[:-3]))
                #eval(s[:-3]+".attach(self)")
        self.running = True
        self.frame = 0
        self.scene_frame = 0

        self.load_scene(self.scene)

        while self.running:
            self.events = pygame.event.get()
            self.input.update()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.clock.tick(self.target_framerate)
            self.frame += 1
            self.scene_frame += 1
            self.display.fill((0,0,0))

            for e in self.UI.elements:
                e.update(self.input)
                self.display.blit(e.canvas,e.rect)
            
            self.scenes[self.scenes_str.index(self.scene)].update()

            #self.UI.test_box_grid(self.display)

            pygame.display.update()

        print("stopping euKombobulator")
        pygame.quit()
        exit()

    def attach_eukombobulator(self):
        return self

    def load_scene(self,scene_name):
        print(f"Loading scene: {scene_name}")
        self.scene = scene_name
        self.scene_frame = 0
        self.UI.elements.clear()
        self.scenes[self.scenes_str.index(self.scene)].attach(self)

print("starting euKombobulator")

try:
    import pygame
    import os
    import tomllib
    from pygame.locals import *
    pygame.init()
except ImportError:
    print("Error! Could not import modules")

try:
    from scenes import *
except Exception as e:
    print(f"Error! {e}")

euk = euKombobulator()