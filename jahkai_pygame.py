import pygame

class Game:
    def __init__(self,screen_width: int,screen_height: int,frame_rate: int = 60):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.frame_rate = frame_rate
        self.screen = pygame.display.set_mode([screen_width,screen_height])
        self.clock = pygame.time.Clock()
        self.r = 0
        self.g = 0
        self.b = 0
        self.is_running = True
    def update(self):
        pygame.display.update()
        self.clock.tick(self.frame_rate)
    def set_color(self, color_value: pygame.Color):
        self.screen.fill(color_value)
    def set_rgb(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Player:
    def __init__(self, width, height, position_x, position_y, thickness = 0, border_radius = 0, velocity = 5, color="red"):
        self.self = pygame.Rect(width,height,position_x, position_y)
        self.color = color
        self.thickness = thickness
        self.border_radius = border_radius
        self.velocity = velocity
    def create(self, game_obj: Game):
        pygame.draw.rect(game_obj.screen,self.color,self.self,self.thickness, self.border_radius)

def event_handler(game_obj: Game,):
    QUIT = pygame.QUIT
    
    for event in pygame.event.get():
        # one clicks
        if event.type == QUIT:
            game_obj.is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_obj.is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("SPACE")

def key_handler(game_obj: Game, player_obj = None):
    # continuous clicks
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    RIGHT = pygame.K_RIGHT
    LEFT = pygame.K_LEFT
    SPACE = pygame.K_SPACE
    ESCAPE = pygame.K_ESCAPE
    keys = pygame.key.get_pressed()
    
    if keys[UP]:
        player_obj.self.bottom -= player_obj.velocity
    if keys[DOWN]:
        player_obj.self.bottom += player_obj.velocity
    if keys[RIGHT]:
        player_obj.self.left += player_obj.velocity
    if keys[LEFT]:
        player_obj.self.left -= player_obj.velocity
    if keys[SPACE]:
        pass
    if keys[ESCAPE]:
        game_obj.is_running = False

    if player_obj.self.bottom > game_obj.screen.get_height():
        player_obj.self.bottom = game_obj.screen.get_height()

    if player_obj.self.top < 0:
        player_obj.self.top = 0

    if player_obj.self.right > game_obj.screen.get_width():
        player_obj.self.right = game_obj.screen.get_width()

    if player_obj.self.left < 0:
        player_obj.self.left = 0

class Tool:
    def __init__(self, tool_type: str):
        self.counter = 0
        self.tool_type = tool_type
    
    def count_up(self):
        if self.tool_type.lower() == "counter":
            self.counter += 1
            return self.counter
    def reset(self):
        if self.tool_type.lower() == "counter":
            self.counter = 0
            return self.counter

class Effect:
    def __init__(self, change_at=None, reset_at=None):
        self.change_at = change_at
        self.reset_at = reset_at
 
    def flicker(self, color1:pygame.Color, color2:pygame.Color, tool: Tool, game_obj: Game):    
        if tool.counter < self.change_at:
            game_obj.set_color(color1)
            tool.count_up()
        elif tool.counter >= self.change_at and tool.counter < self.reset_at:
            game_obj.set_color(color2)
            tool.count_up()
        else:
            tool.reset()

    def fade(self, fade_limit: int,fade_limit2: int,fade_limit3: int, game_obj: Game, reset_flag: bool = False):
        phase = "first"
        if game_obj.r < fade_limit and phase == "first":
            game_obj.r += 1
        if game_obj.r >= fade_limit:
            phase = "second"
        if game_obj.g < fade_limit2 and phase == "second":
            game_obj.g += 1
        if game_obj.g >= fade_limit2:
            phase = "third"
        if game_obj.b < fade_limit3 and phase == "third":
            game_obj.b += 1
        if game_obj.b >= fade_limit3 and reset_flag == False:
            phase = "done"
            return phase
        if game_obj.b >= fade_limit3 and reset_flag == True:
            game_obj.r -= fade_limit - 1
            game_obj.g -= fade_limit2 - 1
            game_obj.b -= fade_limit3 - 1
            phase = "first"
        
        

  
