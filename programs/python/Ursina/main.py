from ursina import *

app = Ursina()

player = Entity(model='playerDumy.obj') #color=color.orange, scale_y=2
testDumyX = Entity(model="test1.obj", color=color.orange, x=2, y=-5, z=3)


def update():
    player.x += held_keys['d'] * 5 * time.dt
    player.x -= held_keys['a'] * 5 * time.dt

    player.z += held_keys["w"] * 5 * time.dt
    player.z -= held_keys["s"] * 5 * time.dt


    player.rotation()


def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

EditorCamera()


# start running the game
app.run()