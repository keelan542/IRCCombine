# Prompt user for required information --> name of reverse and forward irc log files
ircr_file = input("Enter name of Reverse IRC log file: ")
ircf_file = input("Enter name of Forward IRC log file: ")


def get_energies(filename, is_reverse=False):
    energies = []

    with open(filename) as file:
        for line in file:
            if "Corrected End Point Energy" in line:
                energies.append(float(line.split()[5]))

    if is_reverse:
        return energies.reverse()
    else:
        return energies


# Get reverse energies (reverse order)
reverse_energies = get_energies(ircr_file, is_reverse=True)

# Get forward energies
forward_energies = get_energies(ircf_file)

# Combine reverse and forward energies into total energies

# Create new relative energy list for path (using first point as reference)
