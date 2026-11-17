
def main():

    def get_hours():
        hours = []
        for day in range(1, 6):
            value = float(input("Enter hours worked on Day #" + str(day) + ": "))
            hours.append(value)
        return hours

    def find_max(hours_list):
        highest = max(hours_list)
        days = []
        for i in range(len(hours_list)):
            if hours_list[i] == highest:
                days.append(i + 1)  # fixed: now correct day number
        return days, highest


    def low_days(hours_list):
        low = []
        for i in range(len(hours_list)):
            if hours_list[i] < 7:
                low.append((i + 1, hours_list[i]))
        return low


    hours = get_hours()
    max_days, highest = find_max(hours)
    print("The most hours worked was on:")
    for d in max_days:
        print("Day #" + str(d) + " when you worked " + str(highest) + " hours.")



    total = sum(hours)
    average = total / 5
    print("The total number of hours worked was: " + str(total))
    print("The average number of hours worked each day was: " + str(average))

    print("Days you slacked off (i.e. worked less than 7 hours):")
    for item in low_days(hours):
        print("Day #" + str(item[0]) + ": " + str(item[1]) + " hours")





main()