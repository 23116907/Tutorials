class Planet:

    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting the {self.system}'

