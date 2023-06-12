class ControlTower:
    def __init__(self):
        self.airplanes = []
    
    def register_airplane(self, airplane):
        self.airplanes.append(airplane)
    
    def request_landing_permission(self, airplane):
        if airplane in self.airplanes:
            print(f"Control tower granting landing permission to {airplane.name}")
            self.notify_landing_permission(airplane)
        else:
            print(f"Control tower: {airplane.name} is not registered. Please register the airplane first.")
    
    def notify_landing_permission(self, airplane):
        for other_airplane in self.airplanes:
            if other_airplane != airplane:
                other_airplane.receive_landing_permission(airplane)


class Airplane:
    def __init__(self, name, control_tower):
        self.name = name
        control_tower.register_airplane(self)
    
    def request_landing_permission(self):
        control_tower.request_landing_permission(self)
    
    def receive_landing_permission(self, requesting_airplane):
        print(f"{self.name} received landing permission from {requesting_airplane.name}")


control_tower = ControlTower()

airplane1 = Airplane("Boeing 747", control_tower)
airplane2 = Airplane("Airbus A320", control_tower)
airplane3 = Airplane("Cessna 172", control_tower)

airplane1.request_landing_permission()
airplane2.request_landing_permission()
airplane3.request_landing_permission()