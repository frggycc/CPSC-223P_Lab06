
import json

class Contacts:
    def __init__(self,/,*,filename):
        """Will open and read a file or create a new one"""
        self.filename = filename
        self.contact_list = {}

        try:
            infile = open(filename, 'r')
        except FileNotFoundError:
            print(filename, "not found. Creating new file...")

            # Create empty file if does not exist
            with open(filename, 'w') as outfile:
                json.dump(self.contact_list, outfile)

            print(filename, "created")
        else:
            with infile:
                self.contact_list = json.load(infile)

            infile.close()

    def add_contact(self,/,*, id, first_name, last_name):
        """Will add a contact based on id"""
        # Error if id already exists
        if id in self.contact_list:
            return "error"

        # Adding to our contact_list
        self.contact_list[id] = [first_name, last_name]
        
        # Sort contact_list by last name, then first name
        sorted_list = sorted(self.contact_list.items(), key=lambda x: (x[1][1], x[1][0]))
        self.contact_list = dict(sorted_list)

        # Write new dictionary to the file
        with open(self.filename, 'w') as outfile:
            json.dump(self.contact_list, outfile)

        return first_name + " " + last_name

    def modify_contact(self,/,*, id, first_name, last_name):
        """Will modify a contact based on id"""

        # Error if contact does not exist
        if id not in self.contact_list:
            return "error"
        
        # Modifying in our list
        self.contact_list[id] = [first_name, last_name]

        # Sort contact_list by last name, then first name
        sorted_list = sorted(self.contact_list.items(), key=lambda x: (x[1][1], x[1][0]))
        self.contact_list = dict(sorted_list)

        # Write new dictionary to the file
        with open(self.filename, 'w') as outfile:
            json.dump(self.contact_list, outfile)

        return first_name + " " + last_name
            

    def delete_contact(self,/,*, id):
        """Will delete a contact based on id"""

        # Error if contact does not exist
        if id not in self.contact_list:
            return "error"

        # Deleting from our list
        temp = self.contact_list[id]
        del self.contact_list[id]

        # Write new dictionary to the file
        with open(self.filename, 'w') as outfile:
            json.dump(self.contact_list, outfile)

        return temp[0] + " " + temp[1]

    def print_list(self,/):
        """Will print the current list of contacts"""
    
        # Display
        print("="*20, "CONTACT LIST", "="*20)
        print("Last Name", " "*12, end="")
        print("First Name", " "*10, end=" ")
        print("Phone")
        print("="*20,"","="*20,"","="*10)

        # Iterate through list
        for k, v in self.contact_list.items():
            print(f'{v[1]:22}{v[0]:22}{str(k):10}')
        
