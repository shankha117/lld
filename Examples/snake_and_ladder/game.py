import uuid


class Snake(object):

    def __init__(self, head, tail):
        self.head_x, self.head_y = head
        self.tail_x, self.tail_y = tail

    def get_head(self):
        return self.head_x, self.head_y

    def get_tail(self):
        return self.tail_x, self.tail_y


class Ladder(object):

    def __init__(self, start, end):
        self.start_x, self.start_y = start
        self.end_x, self.end_y = end

    def get_start(self):
        return self.start_x, self.start_y

    def get_end(self):
        return self.end_x, self.end_y


class Player(object):
    def __init__(self, name):
        self.name = name
        # TODO add a IDgenerator
        self.id = uuid.uuid4().hex
        self.position_x = 0
        self.position_y = 0

    def move(self, unit, dir):
        pass

    def get_name(self):
        pass

    def get_position(self):
        return self.position_x, self.position_y



class Borad(object):
    pass