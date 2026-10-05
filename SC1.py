#Name: Matthew Ward
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
#Name:Owen Gunselman
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game

enemy_database = {
    "Jack The Ripper" : {
        "Hp" : 1000,
        "Damage" : 2,
        "Endurance" : 5
    },

    "Jack Hot" : {
        "Hp" : 100,
        "Damage" : 100000,
        "Endurance" : 25000
    },

    "Jack Link" : {
        "Hp" : 1,
        "Damage" : 50,
        "Endurance" : 115
    },

    "Jack Sparrow" : {
        "Hp" : 100,
        "Damage" : 100,
        "Endurance" : 100
    },

    "Jack Rabbit" : {
        "Hp" : 40,
        "Damage" : 40,
    "Endurance" : 1000}

}
print(enemy_database)

enemy_database["Jack The Ripper"].update({"Damage" : int(input("Jack The Ripper Damage"))})
enemy_database["Jack Hot"].update({"Damage" : int(input("Jack Hot Damage"))})
enemy_database["Jack Link"].update({"Damage" : int(input("Jack Link Damage"))})
enemy_database["Jack Sparrow"].update({"Damage" : int(input("Jack Sparrow Damage"))})
enemy_database["Jack Rabbit"].update({"Damage" : int(input("Jack Rabbit Damage"))})
print(enemy_database)