
# Render chat window
# ignore input
inputMessages = [["1", "Hello how r u"],
            ["2", "good ty"],
            ["2", "u"],
            ["1", "me too bro"]]
# code starts here
def render(messages, width, userWidth):
    hr = "+" + "".join(["*" for _ in range(width)]) + "+"
    vr = "|"
    result = []
    result.append(hr)
    for pair in messages:
        user, msg = pair
        lines = []
        words = msg.split(" ")
        i = 1
        line = words[0]
        while i < len(words):
            if len(line + " " + words[i]) < userWidth:
                line = line + " " + words[i]
            else:
                lines.append(line)
                line = words[i]
            i += 1
        lines.append(line)
        #print("lines : ", [i for i in lines])
        for linemsg in lines:
            spaces = "".join([" " for _ in range(width - len(linemsg))])
            if user == "1":
                result.append(vr + linemsg + spaces + vr)
            elif user == "2":
                result.append(vr + spaces + linemsg + vr)

    result.append(hr)
    return result


# Ignore below output
output = render(inputMessages, 15, 5)
for line in output:
    print(line)
