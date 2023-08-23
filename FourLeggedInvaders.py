from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
from ursina.prefabs.animation import Animation
#from ursina.shaders import lit_with_shadows_shader

editor_camera = EditorCamera(enabled=False, ignore_paused=True)
def pause_input(key):
    if key == 'tab': # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled
        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)


#Entity.shader = lit_with_shadows_shader
def input(key):
    if key == 'c':
        Audio('laser.wav')

        #Animation function for displaying a muzzle flash
        Animation('catImage.png', parent= camera.ui, fps=5, scale=.1, position=(.19, .23), loop=False)

        for wasp in wasps:
            if wasp.hovered:
                destroy(wasp)
                Audio('explosion.wav')

        for spider in spiders:
            if spider.hovered:
                destroy(spider)
                Audio('explosion.wav')

        for bat in bats:
            if bat.hovered:
                destroy(bat)
                Audio('explosion.wav')

        #if wasps ==  None and spiders == None:
          #  invoke(success())


        #Trying to play a background audio while the game is being played but to no avail yet
        ''' if key == 'p':
                Audio('backgroundSound.wav')'''


class Wasp(Button):
    def __init__(self, x, y, z):
        super().__init__(parent=scene, model='cube', scale= (.1,.2, .1),position=(x, y, z), rotation=(0, 90, 0),
                         color=color.blue, collider= 'box')

class Spider(Button):
    def __init__(self, x, y, z):
        super().__init__(parent=scene, model='cube', scale= (.1,.2, .1),position=(x, y, z), rotation=(0, 90, 0),
                         color=color.black, collider= 'box')

class Bats(Button):
    def __init__(self, x, y, z):
        super().__init__(parent=scene, model='cube', scale= (.1,.2, .1),position=(x, y, z), rotation=(0, 90, 0),
                         color=color.gold, collider= 'box')


#Text.default_resolution = 1080 * Text.size
#test = Text(text="Mission Accomplished!", origin=(0,0), background=True)

'''
def success():
    Text.default_resolution = 1080 * Text.size
    Text(text="Mission Accomplished!", origin=(0,0), scale = 3, background=True)
'''

'''    
def update():
    if wasps == 0:
        if spiders == 0:
            invoke(success(), delay=1)'''


app = Ursina()

Sky()
player = FirstPersonController(y=2, origin_y = .5, speed = 5)

ground = Entity(model='plane', scale = (100, 1, 100), color = color.lime, texture = 'white_cube',
                texture_scale = (100, 100), collider = 'box')

wall_1 = Entity(model='cube', scale = (8,5,1), position = (-8, 0, 0), color = color.gray,
                collider = 'box', texture = 'brick',texture_scale = (5,5), rotation = (0,2, 0))

wall_2 = duplicate(wall_1, z =5)
wall_3 = duplicate(wall_1, z = 10)
wall_4 = Entity(model='cube', collider = 'box', color = color.gray, position = (-15, 0, 10), rotation=(0,0,0),
                scale=(1,5, 20), texture = 'brick', texture_scale = (5, 5))

gun = Entity(model='cube', parent = camera, color = color.gray, scale = (-0.1,.17, .6), position = (0, -0.15, .1),
            origin_x = -.6, origin_y = 0)

num_of_wasps = 10
wasps =[None]*num_of_wasps
for i in range(num_of_wasps):
    wx = random.uniform(-12, -7)
    wy = random.uniform(.1, 1.8)
    wz = random.uniform(.8, 3.8)
    wasps[i] = Wasp(wx, wy, wz)
    #wasps[i].animate_y(wy +.5, duration= 2, loop=True)
    wasps[i].animate_x(wx + 3, duration= 2, loop=True)
    #wasps[i].animate_z(wz +.5, duration= 2, loop=True)



num_of_spider = 15
spiders=[None] * num_of_spider
for i in range(num_of_spider):
    sx = random.uniform(-12, -7)
    sy = random.uniform(.1, 1.8)
    sz = random.uniform(5.8, 8.8)
    spiders[i] = Spider(sx, sy, sz)
    spiders[i].animate_x(sx + 3, duration= 2, loop=True)


num_of_bats = 15
bats=[None] * num_of_bats
for i in range(num_of_bats):
    bx = random.uniform(-12, -7)
    by = random.uniform(.1, 1.8)
    bz = random.uniform(5.8, 8.8)
    bats[i] = Bats(bx, by, bz)
    bats[i].animate_x(bx + 3, duration=2, loop=True)

#sun = DirectionalLight()
#sun.look_at(Vec3(1, 1, -1))

window.fps_counter.enabled = False
'''
window.fps_counter.enabled = False
window.title = 'Legged Invaders'
window.fullscreen = False
window.borderless = False
window.exit_button.enabled = False
'''

app.run()