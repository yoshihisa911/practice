class HotelRoom:
    def __init__(self, room_number, room_type='single'):
        self.room_number = room_number
        self.room_type = room_type
        self.guest_name = None

    def check_in(self, guest_name):
        self.guest_name = guest_name
　
    def check_out(self):
        self.guest_name = None

    def is_empty(self):
        return self.guest_name is None

    def __str__(self):
        if self.guest_name is None:
            return f'Room {self.room_number} ({self.room_type}) is empty'
        else:
            return f'Room {self.room_number} ({self.room_type}) is occupied by {self.guest_name}'


class Hotel:
    def __init__(self, room_info):
        self.rooms = [HotelRoom(num, rtype) for num, rtype in room_info]

    def show_all_rooms(self):
        for room in self.rooms:
            print(room)

    def check_in_on_room(self, room_number, guest_name):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_empty():
                    room.check_in(guest_name)
                    return
                else:
                    raise Exception(f'Room {room_number} is not empty')
        raise Exception(f'Invalid room number: {room_number}')

    def check_out_from_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_empty():
                    room.check_out()
                    return
                else:
                    raise Exception(f'Room {room_number} is already empty')
        raise Exception(f'Invalid room number: {room_number}')

    def find_room_by_guest(self, guest_name):
        for room in self.rooms:
            if room.guest_name == guest_name:
                return room.room_number
        return None

    def check_in_auto(self, guest_name, preferred_type='single'):
        for room in self.rooms:
            if room.is_empty() and room.room_type == preferred_type:
                room.check_in(guest_name)
                return room.room_number
        raise Exception(f'No available {preferred_type} room for {guest_name}')

# --- テスト ---
rooms_info = [
    (101, 'single'),
    (102, 'single'),
    (201, 'double'),
    (202, 'double'),
    (301, 'suite')
]

hotel = Hotel(rooms_info)

hotel.show_all_rooms()
print("---")

hotel.check_in_auto("Alice", preferred_type='single')
hotel.check_in_auto("Bob", preferred_type='double')
hotel.check_in_on_room(301, "Charlie")

print("--- 状態確認 ---")
hotel.show_all_rooms()



print("--- チェックアウト ---")
hotel.check_out_from_room(101)
hotel.show_all_rooms()

print(hotel.find_room_by_guest('Charlie'))
