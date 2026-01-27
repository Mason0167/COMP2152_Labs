contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice phone number: ", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("New contact: ", contacts)

del contacts["Charlie"]
print("After delete Charlie's phone: ", contacts)

print("All names: ", contacts.keys())
print("All phone number: ", contacts.values())
print("Total count of numbers: ", len(contacts))