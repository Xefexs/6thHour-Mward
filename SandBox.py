import random

# Fixed dictionary keys and missing quotes from the original string declarations
enemy_database = {
    "Jack The Ripper": {"Hp": 300, "Damage": 160, "Endurance": 5},
    "Jack Hot": {"Hp": 450, "Damage": 150, "Endurance": 25000},
    "Jack Link": {"Hp": 250, "Damage": 50, "Endurance": 115},
    "Jack Sparrow": {"Hp": 350, "Damage": 100, "Endurance": 100},
    "Dead shot": {"Hp": 800, "Damage": 35, "Endurance": 5},
    "Holy Knight": {"Hp": 900, "Damage": 80, "Endurance": 1000},
    "Crimson Shield": {"Hp": 1500, "Damage": 175, "Endurance": 1000000},
    "Heather": {"Hp": 100, "Damage": 250, "Endurance": 1},
    "Will Smith": {"Hp": 910, "Damage": 100, "Endurance": 10},
    "Chris Rock": {"Hp": 10, "Damage": 5, "Endurance": 5},
    "Faded Prince": {"Hp": 420, "Damage": 420, "Endurance": 1000},
}

fighters = list(enemy_database.keys())

print("Available Fighters:")
for index, name in enumerate(fighters, start=1):
    print(f"{index}. {name}")

x = int(input("\nChoose Your Fighter (Enter number): "))
player_name = fighters[x - 1]
player_hp = enemy_database[player_name]["Hp"]
player_dmg = enemy_database[player_name]["Damage"]

enemy_name = random.choice(fighters)
enemy_hp = enemy_database[enemy_name]["Hp"]
enemy_dmg = enemy_database[enemy_name]["Damage"]

print(f"\nMATCH START: {player_name} (HP: {player_hp}) vs {enemy_name} (HP: {enemy_hp})")
print("-" * 50)

round_num = 1
while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Round {round_num} ---")

    # NEW: Prompts the player to choose their action each round
    while True:
        choice = input("Do you want to (A)ttack or (B)lock? ").strip().lower()
        if choice in ["a", "attack"]:
            player_action = "attack"
            break
        elif choice in ["b", "block"]:
            player_action = "block"
            break
        else:
            print("Invalid choice. Please enter 'A' or 'B'.")

    enemy_action = random.choice(["attack", "block"])

    print(f"{player_name} prepares to {player_action.upper()}!")
    print(f"{enemy_name} prepares to {enemy_action.upper()}!")
    print("." * 20)

    # Scenario 1: Both characters attack each other
    if player_action == "attack" and enemy_action == "attack":
        enemy_hp -= player_dmg
        player_hp -= enemy_dmg
        print(
            f"⚔️ Both fight aggressively! {player_name} deals {player_dmg} damage, {enemy_name} deals {enemy_dmg} damage!")
        print(f"{player_name}: {max(0, player_hp)} HP | {enemy_name}: {max(0, enemy_hp)} HP")

    # Scenario 2: Player attacks, Enemy blocks
    elif player_action == "attack" and enemy_action == "block":
        if random.random() < 0.25:  # 25% chance to break block
            enemy_hp -= player_dmg
            print(f"💥 BLOCK BREAK! {player_name} shatters {enemy_name}'s guard and hits for {player_dmg} damage!")
        else:
            print(f"🛡️ {enemy_name} successfully BLOCKED {player_name}'s attack!")
            if random.random() < 0.15:  # 15% counter chance
                player_hp -= enemy_dmg
                print(f"⚡ COUNTER! {enemy_name} strikes back for {enemy_dmg} damage!")
        print(f"{player_name}: {max(0, player_hp)} HP | {enemy_name}: {max(0, enemy_hp)} HP")

    # Scenario 3: Enemy attacks, Player blocks
    elif enemy_action == "attack" and player_action == "block":
        if random.random() < 0.25:  # 25% chance to break block
            player_hp -= enemy_dmg
            print(f"💥 BLOCK BREAK! {enemy_name} shatters {player_name}'s guard and hits for {enemy_dmg} damage!")
        else:
            print(f"🛡️ {player_name} successfully BLOCKED {enemy_name}'s attack!")
            if random.random() < 0.30:  # 30% counter chance
                enemy_hp -= player_dmg
                print(f"⚡ COUNTER! {player_name} strikes back for {player_dmg} damage!")
        print(f"{player_name}: {max(0, player_hp)} HP | {enemy_name}: {max(0, enemy_hp)} HP")

    # Scenario 4: Both block
    elif player_action == "block" and enemy_action == "block":
        print("🛡️ Both fighters take a defensive stance. Nothing happens!")

    if enemy_hp <= 0 or player_hp <= 0:
        break

    round_num += 1
    print("-" * 50)

print("-" * 50)
if player_hp > 0 and enemy_hp <= 0:
    print(f"🏆 VICTORY! {player_name} has defeated {enemy_name}!")
elif enemy_hp > 0 and player_hp <= 0:
    print(f"💀 DEFEAT! {enemy_name} has crushed {player_name}!")
else:
    print("🤝 DRAW! Both fighters knocked each other out!")