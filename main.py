# with open("Input/Letters/starting_letter.txt") as letter:
#     content = letter.read()
#
# # for each name in invited_names.txt
# with open("Input/Names/invited_names.txt") as names:
#     name = names.read().split("\n")
#
# # Replace the [name] placeholder with the actual name.
# for person in name:
#     letter = content.replace("[name]", person)
#     with open(f"Output/ReadyToSend/{person}", "w") as file:
#         file.write(letter)


# another method using strip() and readlines()
with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    name = names.readlines()

# Replace the [name] placeholder with the actual name.
for person in name:
    person = person.strip()
    letter = content.replace("[name]", person)
    with open(f"Output/ReadyToSend/letter_to_{person}", "w") as file:
        file.write(letter)
