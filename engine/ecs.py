class Entity:
    _id = 0

    def __init__(self):
        self.id = Entity._id
        Entity._id += 1
        self.components = {}

    def add_component(self, component):
        component_name = type(component).__name__
        self.components[component_name] = component

    def get_component(self, component_name):
        return self.components.get(component_name, None)

    def remove_component(self, component_name):
        if component_name in self.components:
            del self.components[component_name]

class EntityManager:
    def __init__(self):
        self.entities = []

    def create_entity(self):
        entity = Entity()
        self.entities.append(entity)
        return entity

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def update(self, dt):
        for entity in self.entities:
            for component in entity.components.values():
                component.update(dt)
