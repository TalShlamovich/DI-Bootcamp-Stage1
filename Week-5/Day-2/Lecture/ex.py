class Door:
    def __init__(self) -> None:
        self.is_opened = True
    
    def open_door(self):
        self.is_opened = True
        print("the door is open")
    def close_door(self):
        self.is_opened = False
        print("the door is closed")


class BlockedDoor(Door):
    def __init__(self) -> None:
        self.is_opened = False
        
    def open_door(self):
        raise Exception("Cannot open blocked door")

    def close_door(self):
        raise Exception("It's already blocked")

door = Door()

door.open_door()
door.close_door()

blocke_door = BlockedDoor()

blocke_door.open_door()
blocke_door.close_door()