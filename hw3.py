# ******** HW3 ******** #
## part A Warm-up
def sequence_is_legal(sequence):  # checks if a sequence of 9 values contains the numbers 1 to 9.
    for i in range(len(sequence)):
        if (i + 1) not in sequence:
            return False
    return True


def sudoku_is_legal(board):
    for i in range(9):
        if not sequence_is_legal(board[i]):  # checks if line is legal.
            return False
        column = []
        for j in range(9):
            column.append(board[j][i])  # creates a list from a column.
        if not sequence_is_legal(column):  # checks if column is legal.
            return False
    for l in range(3):
        for k in range(3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(board[i + (l * 3)][j + (k * 3)])  # creates a list from third of the matrix (a box in sudoku).
            if not sequence_is_legal(box):  # checks if box is legal.
                return False
    return True  # if all lines, rows and boxes are legal, the sudoku is legal.


def soduko_is_legal(board):
    for i in range(9):
        if not sequence_is_legal(board[i]):  # checks if line is legal.
            return False
        column = []
        for j in range(9):
            column.append(board[j][i])  # creates a list from a column.
        if not sequence_is_legal(column):  # checks if column is legal.
            return False
    for l in range(3):
        for k in range(3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(board[i + (l * 3)][j + (k * 3)])  # creates a list from third of the matrix (a box in sudoku).
            if not sequence_is_legal(box):  # checks if box is legal.
                return False
    return True  # if all lines, rows and boxes are legal, the sudoku is legal.


## part B string manipulation
# function 1 change_tone
def change_tone(phrase, new_tone):
    if not new_tone:  # no need to change the tone.
        if phrase[len(phrase)-1:len(phrase)] == '?':  # checks if last index of the string is a question mark.
            return phrase[:len(phrase)-1]  # "deletes" last char
        elif phrase[len(phrase)-1:len(phrase)] == '!':  # checks if the last index of the string is a exclamation mark.
            return phrase + '?'  # adds a question mark in the end of the string.
        else:  # in case that last index is any other char.
            return phrase + '?'  # adds a question mark in the end of the string.
    else:  # tone need to be changes.
        if phrase[len(phrase)-2:len(phrase)] == '!?':  # checks the two last indexes of the string.
            return phrase[:len(phrase)-2]  # "deletes" two last chars
        elif phrase[len(phrase)-1:len(phrase)] == '!':  # checks the last index of the string.
            return phrase[:len(phrase)-1] + '?'  # "replaces" last char with a question mark.
        elif phrase[len(phrase)-1:len(phrase)] == '?':  # checks the last index of the string.
            return phrase[:len(phrase)-1] + '!' # "replaces" last char with a exclamation mark.
        else: # in case that last index is any other char.
            return phrase + '!?'  # adds question mark in the end of the string.


# function 2 be_polite
def be_polite(paragraph):
    phrases = paragraph.split(".")  # separates the paragraph into small phrases divided by ".".
    for i in range(len(phrases)):
        phrases[i] = change_tone(phrases[i], True)  # handles each phrase using previous function.
    return '.'.join(phrases)  # connects the phrases into a paragraph with "." between them.


## part C data structures
# function 1 print_chars(phrase, repeat)
def print_chars(phrase, repeat):
    chars = list(phrase)  # turns the phrase into a list of chars.
    if not repeat:  # means that chars should not repeat themselves.
        chars = list(set(phrase))  # turns it to a set to prevent duplicates, then turns it to a list again.
    for i in range(len(chars)):  # buuble sorts the chars by their ascii value.
        for j in range(len(chars) - i - 1):
            if ord(chars[j]) > ord(chars[j+1]):
                chars[j], chars[j+1] = chars[j+1], chars[j]
    return chars


# function a1 - orientation_day_registery
def orientation_day_registery(all_listed_students):
    students_dict = {}  # creates empty dictionary.
    for student in all_listed_students:
        first_name = student.split(' ')[0][0].upper() + student.split(' ')[0][1:len(student.split(' ')[0])].lower()  # upper the first char in the first name and lower all the others.
        last_name = student.split(' ')[1][0].upper() + student.split(' ')[1][1:len(student.split(' ')[1])].lower()  # upper the first char in the last name and lower all the others.
        grade_str = student.split(' ')[2]  # points the grade's string.
        if not grade_str.replace('.', '', 1).isdigit() or int(float(grade_str)) < 200 or int(float(grade_str)) > 800:  # checks if grade is a number and if it is between 200 and 800.
            grade_str = 200  # fixes invalid grades.
        students_dict[first_name + ' ' + last_name] = int(float(grade_str))  # inserts the valid students details into the dictionary.
    return students_dict


# function b1 - get_number_of_honorary
def get_number_of_honors(students):
    counter = 0  # counts the honors.
    for student_name in students:
        if students[student_name] >= 750:  # checks students grade.
            counter += 1
    return counter


# function b2 - get_with_honors
def get_honors(students, min_grade):
    above_min_grade = {}  # creates a new dictionary.
    for student_name in students:  # iterates over the valid students dictionary.
        if students[student_name] >= min_grade:  # checks if student is honor.
            above_min_grade[student_name] = students[student_name]  # enters the student to the honors dictionary.
    return sorted(above_min_grade, key=above_min_grade.get, reverse=True)  # sorts the honors by their grades (from big to small)


# function b3 - get_with_honors_by_avg
def get_with_honors_by_avg(students_list):
    arranged_dict = orientation_day_registery(students_list)  # creates valid values students dictionary.
    avg = sum(arranged_dict.values()) / len(arranged_dict.values())  # calculates the average of the grades.
    return avg, get_honors(arranged_dict, avg)  # returns the students that passed the average grade (using previous function).


# ******** GOOD LUCK ******** #
