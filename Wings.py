from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()


# Makes sure that the code is updated(duh), enabling the enemies on screen to be in a loop(kinda)
# And keeps track of events in the game
def update():
    global bats, monsters, run_bat, run_monster
    if run_bat:
        for b in bats:
            b.z -= .1  # This is to make the monster move
            if b.z <= -20:  # This block of code checks if the monsters are past a certain distance and destroys the
                # characters to free up space in the game environment
                bats.remove(b)
                destroy(b)

        # Removes and destroys the monsters to prevent the enemies from clogging up the screen
        # when the 1 and 2 keys are pressed simultaneously
        for m in monsters:
            monsters.remove(m)
            destroy(m)

    if run_monster:
        for m in monsters:
            m.z -= .2  # This is to make the monster move
            if m.z <= -20:  # This block of code checks if the monsters are past a certain distance and destroys the
                # characters to free up space in the game environment
                monsters.remove(m)
                destroy(m)
        # Removes and destroys the monsters to prevent the enemies from clogging up the screen
        # when the 1 and 2 keys are pressed simultaneously
        for b in bats:
            bats.remove(b)
            destroy(b)


# Responsible for the input
def input(key):
    global bats, monsters, run_bat, run_monster

    # for i in range(10):
    # This generates monsters if a certain key is pressed
    if not run_bat:
        # for i in range(5):
        if key == '1':
            run_bat = True
            run_monster = False
            invoke(new_bat, delay=random.uniform(1, 3))

    if not run_monster:
        if key == '2':
            # for j in range(10):
            run_monster = True
            run_bat = False
            invoke(new_monster, delay=random.uniform(1, 3))

    # This checks for the press of the alt key to fire a gun
    if key == 'alt':
        Audio('laser.wav')

        # If the mouse is hovered over the enemies, and the gun is shot by pressing the alt key, the enemies disappear
        for b in bats:
            if b.hovered:
                b.z = -2000
                Audio('explosion.wav')  # The problem of hearing the explosion sound everytime the gun was shot has been
                # fixed here unlike my other game

        for m in monsters:
            if m.hovered:
                m.z = -2000
                Audio('explosion.wav')


# This is to ensure that the code block below runs and the game enters a 'god-mode'
editor_camera = EditorCamera(enabled=False, ignore_paused=True)


def pause_input(key):
    if key == 'tab':  # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled
        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        gun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        application.paused = editor_camera.enabled


pause_handler = Entity(ignore_paused=True, input=pause_input)


# This handles the creation of the bats in an animated format
def new_bat():
    global bats, run_bat
    new = Animation('enemyship', collider='box', scale=(1.3, .8), position=(-11, 2, 20))
    bats.append(new)
    if run_bat:
        invoke(new_bat, delay=random.uniform(1, 2))


# This handles the creation of the monsters in an animated format
def new_monster():
    global monsters, run_monster
    new = Animation('enemyship', collider='box', scale=(1.3, .8), position=(-5, 2, 20))
    monsters.append(new)
    if run_monster:
        invoke(new_monster, delay=random.uniform(1, 2))


# Creates the sky entity
Sky()

# Responsible for the view of the player in the first person view
player = FirstPersonController(y=2, origin_y=.5, speed=5)

# As the names imply
ground = Entity(model='plane', collider='box', scale=(100, 1, 100), texture_scale=(100, 100),
                color=color.light_gray, texture='grass')

wall_1 = Entity(model='cube', collider='box', position=(-8, 0, 20), scale=(2, 8, 20), color=color.yellow,
                texture='brick', texture_scale=(5, 5), rotation=(0, 2, 0))

wall_2 = duplicate(wall_1, x=-15)

gun = Entity(model='cube', parent=camera, color=color.gold, scale=(-.1, .1, .8), position=(0, -0.15, .1),
             origin_x=-.6, origin_y=0)

bat = Entity(model='circle', scale=.01)
monster = duplicate(bat, scale=.01)

# Creating a list of bats and monsters
bats = [bat]
monsters = [monster]

# Setting the run_bat and run_monster to False is a way of checking for specific conditions to enable execution of the
# new_bat and new_monster functions in the update function
run_bat = False
run_monster = False

window.fps_counter.enabled = False
window.title = 'Wings In Paradise'
window.borderless = False
window.exit_button.enabled = False

app.run()
