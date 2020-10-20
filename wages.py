def weeklyDosh(hours, wage):
    if hours > 40:
        return 40 * wage + (hours - 40) * wage * 1.5
    else:
        return hours * wage


def getInput(usrinput):
        return float(input(usrinput))


hours = getInput("How many hours did you work this week? ")
wage = getInput("What is your hourly rate? ")

pay = weeklyDosh(hours, wage)

print(f"Total pay: ${pay:.2f} ")

if hours > 41:
    print('and you did {} hours overtime.'.format(int(hours -40)))
elif hours == 41:
    print('and you did 1 hour of overtime.')



