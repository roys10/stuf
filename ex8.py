''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################

class Room:
    def _init_(self, floor, number, guests, clean_level, rank, satisfaction=1.0):
        self.floor = floor
        self.number = number
        self.guests = guests
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = satisfaction

        self.convert_guests()
        self.check_value()

        if not isinstance(self.clean_level, int) or not isinstance(self.rank, int) or not isinstance(self.satisfaction,
                                                                                                     float):
            print("The type of one of the attributes is wrong")

    def check_value(self):
        if self.clean_level < 1 or self.clean_level > 10 or self.rank < 1 or self.rank > 3 or self.satisfaction < 1 or self.satisfaction > 5:
            print("The value of one of the attributes is wrong")

    def convert_guests(self):
        for guest in self.guests:
            guest = guest.lower()

    def fix_guests(self):
        if len(self.guests) == 0:
            return "empty"
        guests = self.guests[0]

        for guest in self.guests[1:len(self.guests)]:
            guests += f", {guest}"
        return guests

    def _repr_(self):

        return f"floor: {self.floor} \nnumber: {self.number} \nguests: {self.fix_guests()} \nclean level: {self.clean_level} \nrank: {self.rank} \nsatisfaction: {round(self.satisfaction, 1)}"  # replace this with your implementation

    def is_occupied(self):
        if self.fix_guests() == "empty":
            return
        return False

    def can_clean(self):
        return

    def clean(self):
        if self.can_clean():
            min(10, self.clean_level + self.rank)
        else:
            print("Eat shit")
            return -1

    def better_than(self, other):
        this_stats = (self.rank, self.floor, self.clean_level)
        other_stats = (other.rank, other.floor, other.clean_level)
        if this_stats > other_stats:
            return
        print("Other must be an instance of room")
        return -1

    def check_in(self, guests):
        if self.fix_guests() == "empty":
            print("Cannot check in new guests to an occupied room")
            return -1
        self.guests = guests
        self
        self.satisfaction = 1.0

    def check_out(self):
        pass  # replace this with your implementation

    def move_to(self, other):
        pass  # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def _init_(self, floor, number, guests, clean_level,
               rank=1, satisfaction=1.0, clean_stock=0):
        pass  # replace this with your implementation

    def _repr_(self):
        return ""  # replace this with your implementation

    # Replace this comment with your methods' implementation


class LegacyRoom(Room):
    def _init_(self, floor, number, guests, clean_level,
               rank=2, satisfaction=1.0,
               minibar_drinks=2, minibar_snacks=2):
        pass  # replace this with your implementation

    def _repr_(self):
        return ""  # replace this with your implementation

    # Replace this comment with your methods' implementation


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def _init_(self, name, rooms):
        pass  # replace this with your implementation

    def _repr_(self):
        return ""  # replace this with your implementation

    def check_in(self, guests, rank):
        pass  # replace this with your implementation

    def check_out(self, guest):
        pass  # replace this with your implementation

    def upgrade(self, guest):
        pass  # replace this with your implementation


#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    print(h.upgrade("Liat"))
    print(h.check_out("Ronen"))
    print(h.check_in(["Alice", "Wonder"], 2))
    print(h.check_in(["Alex"], 3))
    print(h)
    print(h.check_in(["Oded", "Shani"], 3))
    print(h.check_in(["Oded", "Shani"], 1))
    print(h.check_out("Liat"))
    print(h.check_out("Liat"))
    print(h)


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "_main_":
    # test_hotel()
    r1 = Room(1, 21, ["bob", "guy"], 3, 2, 5.567)
    print(repr(r1))