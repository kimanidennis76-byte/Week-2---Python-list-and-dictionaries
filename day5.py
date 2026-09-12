# Day 5
contacts = [
    
    {"name": "Dennis Kimani", "phone": "0003648886","skill": "Farmer", "city": "Nairobi"},
    {"name": "Josphine Mwende", "phone": "0062284083", "skill": "Graphics Designer", "city": "Kitui"},
    {"name": "Nicholus Mujina", "phone": "0022887665", "skill": "Welding", "city": "Nairobi"},
    {"name": "Majanja Marisa", "phone": "0003646789", "skill": "Plumber", "city": "Mombasa"},
    {"name": "Mogaka Chesire", "phone": "0021165054", "skill": "Lawyer", "city": "Kisii"},

]
#Build contact book structre

print("stored contacts:",len(contacts))

print(contacts[2])

# Display all contact
print("=======CONTACT BOOK======")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"  Phone : {contact['phone']}")
    print(f"  Skill : {contact['skill']}")
    print(f"  city: {contact['phone']}")

# search for a contact
print("========CONTACT SEARCH=====")
search_name= "Dennis Kimani"
found= False
for contact in contacts:
    if contact["name"] == search_name:
        print(f"  Name : {contact['name']}")
        print(f"  Phone : {contact['phone']}")
        print(f"  Skill : {contact['skill']}")
        print(f"  City : {contact['city']}")
        found = True
        break
    if not found:
        print("No conatct found with name:", search_name)

# search by city
print("======NAIROBI CONTACTS======")

search_city = "Nairobi"
print(f"Contacts in {search_city} ")

for contact in contacts:
    if contact['city'] == search_city:
      print(f" {contact['name']} | {contact['skill']} | {contact['phone']}")

#Adding new contact

print("Before:", len(contacts), "contacts")

# Add new contact
new_contact = {
    "name": "James Mwangi",
    "phone": "0721829292",
    "skill": "Upholstery",
    "city": "Kanduyi"
}
contacts.append(new_contact)

print("After:", len(contacts), "contacts")
print("Last contact:", contacts[-1])

print("=======SUMMARY==========")
print(f"Total contacts: {len(contacts)}")

              

#Phone cntacts
phonebook = {"Eric" :"0721234433", "Joaz": "0993383838", "Matamba": "0456787339"}
print("============ CONTACTS ============")
for name,number in phonebook.items():
    print(f"{name} :{number}")