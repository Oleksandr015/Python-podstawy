
person = 'Leonardo DiCaprio'
guest_list = []
guest_list.append(person)
print(guest_list)



class GuestList:
    def __init__(self):
        self.guest_list = []

    def add_guest(self, person):
        self.guest_list.append(person)

if __name__ == '__main__':
    guest_1 = GuestList()
    print(guest_1.add_guest('Leonardo DiCaprio'))