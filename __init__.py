ircr_file = input("Enter name of Reverse IRC log file: ")
ircf_file = input("Enter name of Forward IRC log file: ")
correction = float(input("Enter optional correction to relative energies:  "))


# Function to get list of energies from IRC file
def get_energies(filename, is_reverse=False):
    energies = []

    with open(filename) as file:
        for line in file:
            if "Corrected End Point Energy" in line:
                energies.append(float(line.split()[5]))

    if is_reverse:
        energies.reverse()

    return energies


# Function to return a relative energies list
def get_relative_energies(energies):
    relative_energies = []
    for energy in energies:
        relative_energies.append(((energy - energies[0]) * 627.51) + correction)

    return relative_energies


# Get reverse energies (reverse order)
reverse_energies = get_energies(ircr_file, is_reverse=True)

# Get forward energies
forward_energies = get_energies(ircf_file)

# Combine reverse and forward energies into total energies
total_energies = reverse_energies + forward_energies

# Create new relative energy list for path (using first point as reference)
relative_energies = get_relative_energies(total_energies)

# Print out relative energies
for energy in relative_energies:
    print(energy)
