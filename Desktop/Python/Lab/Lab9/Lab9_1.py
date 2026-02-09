class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.state = "stopped"

    def move(self):
        print(self.make, self.model, "is moving")
        self.state = "moving"

    def stop(self):
        print(self.make, self.model, "has stopped")
        self.state = "stopped"

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_state(self):
        return self.state

    def __str__(self):
        return self.make + " " + self.model + " is " + self.state


class Car(Vehicle):

    def __init__(self, make, model, doors):
        Vehicle.__init__(self, make, model)

        self.doors_no = doors

    def set_doors_no(self, number):
        self.doors_no = number

    def get_doors_no(self):
        return self.doors_no

    def __str__(self):
        return self.make + " " + self.model + " with " + str(self.doors_no) + " doors is " + self.state


class Bus(Vehicle):

    def __init__(self, make, model, decks):
        Vehicle.__init__(self, make, model)

        self.decks_no = decks

        self.route = []
        self.route.append("New Street")
        self.route.append("Bullring")
        self.route.append("Moor Street")
        self.route.append("BCU")

        self.current_stop_index = 0
        self.state = "Not in use"

    def get_route(self):
        return "New Street - Bullring - Moor Street - BCU"

    def set_decks_no(self, deck):
        self.decks_no = deck

    def get_decks_no(self):
        return self.decks_no

    def move(self):
        if self.current_stop_index == len(self.route) - 1:
            print("I am finished for today!")
            return

        current_stop = self.route[self.current_stop_index]
        next_stop = self.route[self.current_stop_index + 1]

        print("The", self.make, self.model, "was at", current_stop, "and is moving to", next_stop)

        self.current_stop_index = self.current_stop_index + 1
        self.state = next_stop

    def stop(self):
        print("I am a non-stop bus.")
