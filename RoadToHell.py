from ursina import *
import random
#from ursina.shaders import lit_with_shadows_shader



app = Ursina()

#There is a problem with this code that I don't understand. The update function stops working prematurely

def update():
    global tread, run
    if run:
        tread += time.dt * .4
        setattr(road, 'texture_offset', (0, tread))

        #Entity.default_shader = lit_with_shadows_shader

        #Controls
        car.x += held_keys['d'] * time.dt * .7
        car.x -= held_keys['a'] * time.dt * .7
        #car.y += held_keys['w'] * time.dt * .2
        #print(car.x) for testing

        #Setting borders on the road
        if car.x >= .24:
            car.x = .24

        if car.x <= -.28:
            car.x = -.28


        #Getting the speed of appearance of the pumpkins
        for pumpkin in pumpkins:
            pumpkin.z -= time.dt * 1
            #print(pumpkin.z) for testing

            #Cleaning up the memory after passing each pumpkin
            if pumpkin.z <= -20:
                pumpkins.remove(pumpkin)
                destroy(pumpkin)

                # Getting the position of the car and pumpkin to determine if there is a crash
                # And calling the crash function
            if abs(car.x - pumpkin.x) < .13:
                if abs(car.z - pumpkin.z) < .05:
                    invoke(crash, delay=1)
                    run = False



def crash():
    #Text.default_resolution = 1080 * Text.size
    Text(text="Game Over! Please reload the game by pressing Ctrl + F5", color = color.green,
         scale = 2, origin=(0,0), background = True)


def NewPumpkins():
    scale = (1,0.5,1)
    factor = random.uniform(.02, .2)
    s = [ele * factor for ele in scale]
    x = random.uniform(-.24, .14)
    z = random.uniform(.5, .6)
    new = duplicate(pumpkin, scale=s, x=x, z=z, texture = random.choice(textures))
    pumpkins.append(new)
    invoke(NewPumpkins, delay=random.uniform(1,3))
    if car.z == .5:      #To prevent the car from crashing immediately into the game but it seems not to work
        pumpkins.append = None

    if run == False:  #To prevent the pumpkins from appearing on the screen after a crash
        destroy(new)



road = Entity(model = 'cube', color = color.blue, scale = (10, .5, 70), position = (0,0,0), texture = 'road.png',
              texture_scale = (1, 2))

car = Entity(parent = road, model='cube', texture = 'car.png', scale=(.15, 0.001, 0.06),
             position=(-.1, 1, -.12), collider = 'box')

#Wanna change all pumpkins to cars in future review
#car2 = duplicate(car, position=(-.5,.9, -.15))
textures = ["pumpkin_Color", "pumpkin_Normal", "pumpkin_Roughness"]
textures = ["/" + s for s in textures]

pumpkin = Entity(parent=road, rotation_x = 45, model = "pumpkin.obj", scale=(.07, .05, .0006),
                 position = (0, .90, .5), texture = textures, collider = 'box')

pumpkins = []

NewPumpkins()
tread = 0
run = True

window.color = color.dark_gray
window.fps_counter.enabled = False
window.borderless = False
window.title = 'Road To Hell'
window.exit_button.enabled = False

camera.position = (0, 10, -35)
camera.rotation_x = 20
#camera.rotation_y = 0.5

#sun = DirectionalLight()
#sun.look_at(Vec3(4,-3, -2))
Sky()

app.run()


'''
            def track_credit():
                global score
                score += 1
                print(score)

            track_credit()
'''

            #Wanna write a cheat
            #def input(key):
                #if key == 'p':
                    #run = False

                #if held_keys['c']:
                    #run = True



            #Getting the position of the car and pumpkin to determine if there is a crash
            # And calling the crash function
            #if abs(car.x - pumpkin.x) < .1:
               #if abs(car.z - pumpkin.z) < .05:
                    #invoke(crash, delay=1)
                    #run = False

    #else:
        #print(a)
        #return "Total track credit is ", score
        # print("Total track credit is ", score)


         #@update
        #def track_credit():
            #global  score
            #score += 1
            #print(score)




#track_credit()
'''
    elif run == False:
        return "Total track credit is ", score
        #print("Total track credit is ", score)
'''

#score = 0
'''
#Wanna write a cheat
def input(key):
    if key == 'p':
        run = False

    if held_keys['c']:
        run = True
'''
"""
def crash():
    Text(text="Game Over! Please reload the game", color = color.green, scale = 3, origin=(0,0), background = True)

def NewPumpkins():
    scale = (1,0.5,1)
    factor = random.uniform(.02, .2)
    s = [ele * factor for ele in scale]
    x = random.uniform(-.12, .14)
    z = random.uniform(.46, .6)
    new = duplicate(pumpkin, scale=s, x=x, z=z, texture = random.choice(textures))
    pumpkins.append(new)
    invoke(NewPumpkins, delay=random.uniform(1,1))

app = Ursina()

road = Entity(model = 'cube', color = color.blue, scale = (10, .5, 70), position = (0,0,0), texture = 'road.png',
              texture_scale = (1, 2))

car = Entity(parent = road, model='cube', texture = 'car.png', scale=(.15, 0.001, 0.06),
             position=(-.1, .9, -.12), collider = 'box')

#Wanna change all pumpkins to cars in future review
#car2 = duplicate(car, position=(-.5,.9, -.15))
textures = ["pumpkin_Color", "pumpkin_Normal", "pumpkin_Roughness"]
textures = ["/" + s for s in textures]

pumpkin = Entity(parent=road, rotation_x = 45, model = "pumpkin.obj", scale=(.02, .05, .0006),
                 position = (0, .90, .5), texture = textures, collider = 'box')

pumpkins = []

NewPumpkins()
offset = 0
run = True

window.color = color.dark_gray
window.fps_counter.enabled = False
window.borderless = False
window.title = 'Hell Ride'
window.exit_button.enabled = False

camera.position = (0, 8, -26)
camera.rotation_x = 20
#camera.rotation_y = 0.5

#sun = DirectionalLight()
#sun.look_at(Vec3(4,-3, -2))
Sky()

app.run()
"""