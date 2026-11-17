
def main():

    def get_letters():
        text = input("type a comma-separated list of letters to redact: ")
        letters = text.split(",")
        clean = []
        for l in letters:
            clean.append(l.strip().lower())
        return clean



    def redact(phrase, letters):
        result = ""
        count = 0
        for c in phrase:
            if c.lower() in letters:
                result = result + "_"
                count = count + 1
            else:
                result = result + c
        return result, count


    while True:
        phrase = input("type a phrase (or quit to exit program): ")
        if phrase.strip().lower() == "quit":
            break
        letters = get_letters()
        redacted, count = redact(phrase, letters)
        print("number of letters redacted: " + str(count))
        print("redacted phrase: " + redacted)
        print()


main()