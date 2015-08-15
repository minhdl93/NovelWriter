#!/usr/bin/env python
# took this from here:
# http://codereview.stackexchange.com/questions/56864/text-based-terrain-generator-part-2
from random import choice
from os import system, name
from itertools import chain


class Tiles(object):
    tree = 't' #'\033[7;1;32m  \033[0m'
    land = 'l' #'\033[7;32m  \033[0m'
    sand = 's' #'\033[7;1;33m  \033[0m'
    water = 'w'# '\033[7;1;34m  \033[0m'


class Sizes(object):
    small = 10
    med1 = 20
    med2 = 30
    large = 40

sizes = (
    Sizes.small, Sizes.med1, Sizes.med2, Sizes.large)

tiles = (
    Tiles.land, Tiles.sand, Tiles.tree, Tiles.water)


transitions = {Tiles.land: [Tiles.sand] +
               [Tiles.tree] * 2 +
               [Tiles.land] * 15,
               Tiles.sand: [Tiles.water, Tiles.sand],
               Tiles.tree: [Tiles.tree, Tiles.land],
               Tiles.water: [Tiles.water] * 10
               }


def pick_tile_for(world, x, y):
    surrounding = []
    if x > 0:
        surrounding.append(world[x - 1][y])
    if y < len(world) - 1:
        surrounding.append(world[x][y + 1])
    if y > 0:
        surrounding.append(world[x][y - 1])
    if x < len(world) - 1:
        surrounding.append(world[x + 1][y])
    surrounding = [tile for tile in surrounding if tile is not None]
    if len(surrounding) == 0:
        return None
    excluded = set(surrounding[0])
    for tile in surrounding:
        excluded = excluded - set(transitions[tile])
    next = list(chain(*[[t for t in transitions[tile] if t not in excluded]
                        for tile in surrounding]))
    return choice(next)


def generate(world_size):
    system('cls' if name == 'nt' else 'clear')
    world = []
    for x in range(world_size):
        world.append([None for _ in range(world_size)])
    world[choice(range(world_size))][choice(range(world_size))] = Tiles.land
    for x in range(world_size):
        for y in range(world_size):
            if world[x][y] is None:
                world[x][y] = pick_tile_for(world, x, y)
    for x in range(world_size - 1, -1, -1):
        for y in range(world_size - 1, -1, -1):
            if world[x][y] is None:
                world[x][y] = pick_tile_for(world, x, y)
    for line in world:
        print ''.join(line)


if __name__ == "__main__":
    generate(50)
