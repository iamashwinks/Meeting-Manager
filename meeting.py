class MeetingManager(object):

    def __init__(self):
        self.available = {'10-11': "Available", '2-3': "Available", '5-6': "Available", '9-10': "Available"}
        self.allocated = {}
        self.name = ''

    def time_view(self):
        for k,v in self.available.items():
            print(k,v)

    def schedule(self):
        for k, v  in self.available.items():
            print(k, v)

        x = input("Enter the time you want to schedule: ")
        if x in self.available.keys():
            self.allocated[x]=self.name
            self.available.pop(x)
            print("Thanks! Your meeting has been scheduled. \nThank You.")
        elif x not in self.available.keys():
            ("Time slot not available.\n")

    def occupied(self):
        for k,v in self.allocated.items():
            print(k,v)
