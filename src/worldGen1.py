from random import choice


class WorldGenerator(object):
    def __init__(self, tiles='#*~o', x_length=1000, y_length=1000):
        self.world = []
        self.tiles = tiles
        self.x_length = x_length
        self.y_length = y_length

    def create_row(self):
        for _ in range(self.x_length):
            self.world.append(choice(self.tiles))

    def create(self):
        self.world = []
        for _ in range(self.y_length):
            self.create_row()


class WorldRenderer(object):
    def __init__(self, generator):
        self.gen = generator

    def render(self):
        for tile in self.gen.world:
            print tile,
            # sleep(0.05)


def main():
    gen = WorldGenerator(x_length=30, y_length=10)
    gen.create()
    renderer = WorldRenderer(gen)
    renderer.render()


if __name__ == "__main__":
    main()
