
person = input("Enter the person's name: ")
country = input("Enter the country name: ")
missile = input("Enter the missile name: ")

print("\nEnter the facts (yes/no):")

american = input("Is the person an American? ").lower()
has_missile = input("Does the country have the missile? ").lower()
enemy = input("Is the country an enemy of America? ").lower()

KB = []

if american == "yes":
    KB.append(("American", person))

if has_missile == "yes":
    KB.append(("Missile", missile))
    KB.append(("Owns", country, missile))

if enemy == "yes":
    KB.append(("Enemy", country, "America"))

print("\nInitial Knowledge Base:")
for fact in KB:
    print(fact)

new_facts = []

for fact in KB:
    if fact[0] == "Missile":
        new_facts.append(("Weapon", fact[1]))

for fact in KB:
    if fact[0] == "Enemy":
        new_facts.append(("Hostile", fact[1]))

for f1 in KB:
    for f2 in KB:
        if f1[0] == "Missile" and f2[0] == "Owns":
            if f1[1] == f2[2]:
                new_facts.append(("Sells", person, f1[1], f2[1]))

KB.extend(new_facts)


for f1 in KB:
    for f2 in KB:
        for f3 in KB:
            for f4 in KB:

                if (f1[0] == "American" and
                    f2[0] == "Weapon" and
                    f3[0] == "Sells" and
                    f4[0] == "Hostile"):

                    if (f1[1] == f3[1] and
                        f2[1] == f3[2] and
                        f3[3] == f4[1]):

                        KB.append(("Criminal", f1[1]))

                        break
                else:
                    continue
            else:
                continue
            break
        else:
            continue
        break

print("\nFinal Knowledge Base:")
for fact in KB:
    print(fact)

query = ("Criminal", person)

print("\nQuery:", query)

if query in KB:
    print("Goal Proved:", person, "is a Criminal")
else:
    print("Goal Not Proved")
