
def main():

    def get_data():
        num = int(input("enter the number of guides selling cookies: "))
        names = []
        boxes = []
        for i in range(num):
            name = input("enter the name of guide #" + str(i + 1) + ": ")
            sold = int(input("enter the number of boxes sold by " + name + ": "))
            names.append(name)
            boxes.append(sold)
        return names, boxes


    names, boxes = get_data()
    total = sum(boxes)
    average = total / len(boxes)
    highest = max(boxes)


    print("the average number of boxes sold by each guide was " + str(round(average, 1)))
    print()
    print("guide           prizes won:")
    print("========================================")

    for i in range(len(names)):
        prize = ""
        if boxes[i] == highest and boxes[i] > 0:
            prize = "trip to girl guide jamboree in aruba!"
        elif boxes[i] > average:
            prize = "super seller badge"
        elif boxes[i] >= 1:
            prize = "left over cookies"

        if prize == "":
            print(names[i] + " –")
        else:
            print(names[i] + " – " + prize)



main()