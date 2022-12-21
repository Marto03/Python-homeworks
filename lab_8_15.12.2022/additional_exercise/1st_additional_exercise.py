from main_module import *
#import entities -----> Опитах се чрез __init__ да importna грешките , но ми дава някаква грешка.

characters_names = []
characters = []
characters_class = ["Warrior", "Mage", "Priest", "Rogue"]
class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon for existing character")
        print("3. Create an additional weapon for existing character")
        print("4. Print all existing characters")
        print("5. Delete an existing character")


    def command_create_character(self, name, sex, ch_class, weapon=None, additional_weapon=None):
        return name, sex, ch_class


    def command_create_weapon(self, name, weapon):
        durability = 100
        return weapon, "with", durability, "durability"
        #return weapon


    def command_additional_weapon(self, name, add_weapon):
        return add_weapon

    def command_print_characters(self):
        pass

    def command_delete_characters(self):
        pass

    def run(self):
        # infinite menu loop
        while True:
            Menu.print_menu(self)
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:

                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        raise CharacterExists("Character exists")
                    sex = input("Enter the character sex(Male or Female): ")
                    if sex != "Male" and sex != "Female":
                        raise InvalidSex("Invalid sex")
                    ch_class = input("Enter the character class(Warrior, Mage, Priest, Rogue): ")
                    if name.isdigit() or sex.isdigit() or ch_class.isdigit():
                        raise InvalidParameters("Not supporting numbers!")
                    if ch_class not in characters_class:
                        raise InvalidCharacter("Invalid character!")

                    characters_names.append(name)
                    char = self.command_create_character(name, sex, ch_class)
                    characters.append(char)
                    print(char)
                    continue

                if choice == "2":
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        weapon = input("Enter a weapon: ")
                        weap = self.command_create_weapon(name, weapon)
                        print(f"{name} using {weap}\n")
                        continue
                    else:
                        raise CharacterNotFound("Character not found")


                if choice == "3":
                    name = input("Enter the character name (alpha-numeric): ")
                    if name in characters_names:
                        additional_weapon = input("Enter an additional weapon: ")
                        add_weapon = self.command_additional_weapon(name, additional_weapon)
                        print(f"To character named {name} added additional weapon {add_weapon}\n")
                        continue
                    else:
                        raise CharacterNotFound("Character not found")

                if choice == "4":
                    print(f"{characters} \n")
                    continue


                if choice == "5":
                    characters.clear()
                    print(f"{characters} All characters deleted! \n")
                    continue


                if choice == "Exit":
                    break
                else:
                    raise InvalidCommand("Invalid choice")




            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':

    menu = Menu()
    menu.run()
    print()

