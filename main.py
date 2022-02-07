with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("./Input/Names/invited_names.txt") as names:
    current_name = names.readlines()
    for name in current_name:
        person_name = name.strip()
        new_letter = letter.replace("[name]", person_name)
        with open(f"./Output/ReadyToSend/letter_for_{person_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
