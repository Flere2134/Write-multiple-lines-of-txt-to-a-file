#write line to file function
def write_line_to_file():
#create a list for lines
    lines = []
#ask user to write a line of text
    while True:
        text = input('Write something you want to say or ask: ')
#add line of text to list
        lines.append(text)
#ask user if wants to write another line
        add_line = input('Do you want to add more lines of text? ')
#if yes write and add another line of text
        if add_line in ["Y", "YES", "yes", "Yes", "y"]:
            continue
#if no break out of loop
        elif add_line in ["N", "NO", "no", "No", "n"]:
            break
        else:
            print("Invalid input! Please answer either YES or NO")
#open mylife.txt for writing
    with open("mylife.txt", "w") as my_file:
        my_file.write("\n".join(lines))