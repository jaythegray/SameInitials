def estimate_people_with_initials():
    """
    Estimates the number of people with a specific set of initials and calculates the percentage of the global population.
    """
    global_population = 7.9e9  # Global population

    # Defining frequency categories
    common = {'A', 'S', 'T', 'J', 'M'}
    moderately_common = {'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'N', 'O', 'P', 'R', 'U', 'V', 'W'}
    uncommon = {'Q', 'X', 'Z', 'Y'}
    rare = {'Other'}  # This can include initials that are very rare or specific to certain languages

    # Frequencies
    common_freq = 0.05  # 5%
    moderately_common_freq = 0.03  # 3%
    uncommon_freq = 0.01  # 1%
    rare_freq = 0.005  # 0.5%

    # User input for initials
    initials = [input(f"Enter initial {i+1}: ").strip().upper() for i in range(3)]

    # Assign frequencies based on the initials
    frequencies = []
    for initial in initials:
        if initial in common:
            frequencies.append(common_freq)
        elif initial in moderately_common:
            frequencies.append(moderately_common_freq)
        elif initial in uncommon:
            frequencies.append(uncommon_freq)
        else:
            frequencies.append(rare_freq)  # Assign rare frequency to initials not listed

    # Calculating the number of people with the given initials
    estimated_people = global_population
    for freq in frequencies:
        estimated_people *= freq

    # Calculating the percentage of the global population
    percentage = (estimated_people / global_population) * 100

    return f"Approximately {estimated_people:.0f} people, or about {percentage:.4f}% of the global population, might have the initials {''.join(initials)}"

# Running the function and printing the result
print(estimate_people_with_initials())
