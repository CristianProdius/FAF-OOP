class Object:
    def __init__(self, name, is_moving=False, speed=0, color="of FAF"):
        self.name = name
        self.is_moving = is_moving
        self.speed = speed
        self.color = color

    def inform_state(self):
        state = f"Object {self.name} is {'moving' if self.is_moving else 'standing'} "
        if self.is_moving:
            state += f"at a speed of {self.speed} units per second and is colored {self.color}."
        else:
            state += f"and is colored {self.color}."
        print(state)

if __name__ == "__main__":
    obj1 = Object("Trolik", is_moving=True, speed=600, color="blue")

    obj1.inform_state()