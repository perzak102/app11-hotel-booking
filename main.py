import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df.index = range(1, len(df) + 1)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def available(self):
        """Checks if the hotel is available"""
        avaiability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if avaiability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book the hotel by changing availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def view_hotels(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
