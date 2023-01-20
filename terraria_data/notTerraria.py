#level editor
from engine import game_engine_130123 as engine
import pygame, os, random
file_dir = os.getcwd()

#create window
w, h = 640, 480
window = engine.window.define("Editor", w, h)

#textures
up_grass_texture = pygame.image.load(f"{file_dir}/textures/grass_up.png")
dirt_texture = pygame.image.load(f"{file_dir}/textures/dirt.png")

#variables
run = True
clock = pygame.time.Clock()
scale = 4
playerSpeed = 3
direction = "right"

#lists
display = []
for x in range(-2, 2):
    background = engine.properties_object("bg", f"{file_dir}/textures/background.webp", x * 640, 0, w, h - 24 * scale, False)
    display += [background]

#display_sprite
display_sprite = []
billy = engine.properties_object("billy", f"{file_dir}/textures/billy/5.png", (w / 2) - 24 * scale, h - (96 * scale), 48 * scale, 48 * scale, True)
display_sprite += [billy]

#animation list
playerAnimate = [pygame.image.load(f"{file_dir}/textures/billy/1.png"), pygame.image.load(f"{file_dir}/textures/billy/2.png"), pygame.image.load(f"{file_dir}/textures/billy/3.png"), pygame.image.load(f"{file_dir}/textures/billy/4.png"), pygame.image.load(f"{file_dir}/textures/billy/5.png"), pygame.image.load(f"{file_dir}/textures/billy/6.png"), pygame.image.load(f"{file_dir}/textures/billy/7.png"), pygame.image.load(f"{file_dir}/textures/billy/8.png"), pygame.image.load(f"{file_dir}/textures/billy/9.png"), pygame.image.load(f"{file_dir}/textures/billy/10.png"), pygame.image.load(f"{file_dir}/textures/billy/11.png"), pygame.image.load(f"{file_dir}/textures/billy/12.png")]

#foreground
foreground = []

#sub program
def create_chunk():
    #create ground
    global foreground
    global up_grass_texture, dirt_texture
    for x in range(-30, 30):
        #create grass - flip texture and add it to the foreground
        horizontal = random.randint(0, 1)
        up_grass_texture = pygame.transform.flip(up_grass_texture, horizontal, 0)

        horizontal = random.randint(0, 1)
        vertical = random.randint(0, 1)
        dirt_texture = pygame.transform.flip(dirt_texture, horizontal, vertical)

        up_grass = engine.properties_object(f"grass_{x}{h - (48 * scale)}", up_grass_texture, x * 24 * scale, h - (48 * scale), 24 * scale, 24 * scale, True)
        dirt = engine.properties_object(f"dirt_{x}{h - (24 * scale)}", dirt_texture, x * 24 * scale, h - (24 * scale), 24 * scale, 24 * scale, False)
        foreground += [up_grass, dirt]

create_chunk()
def main():
    global direction
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if engine.player.left(billy, playerSpeed, -40):
            engine.camera.moveCamera(-playerSpeed, 0)
            #create scrolling background
            for v in range(len(display)):
                display[v].x -= 2
            #offset the player
            engine.player.left(billy, playerSpeed, -40)

        engine.player.animate(billy, playerAnimate, 4)     #animate the speed
        direction = "left"

    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if engine.player.right(billy, playerSpeed, w - (-40 + 48 * scale)):
            engine.camera.moveCamera(playerSpeed, 0)
            for v in range(len(display)):
                display[v].x += 2
            engine.player.right(billy, playerSpeed, w - (-40 + 48 * scale))

        engine.player.animate(billy, playerAnimate, 4, 1)
        direction = "right"

    if engine.frames >= billy.animationTime and direction == "left": 
        billy.texture = engine.properties_object.reload_texture(f"{file_dir}/textures/billy/5.png", 48 * scale, 48 * scale)
    elif engine.frames >= billy.animationTime and direction == "right": 
        billy.texture = engine.properties_object.reload_texture(f"{file_dir}/textures/billy/5.png", 48 * scale, 48 * scale)
        billy.texture = pygame.transform.flip(billy.texture, 1, 0)

while run:
    #keyboard and exit button, main code -----------------------------
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    main()
    engine.window.update(window, display, display_sprite, foreground)
    engine.counter.update()
    clock.tick(60)
pygame.quit()