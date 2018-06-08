from tkinter import *
import json

NO_VOTE_STRING = 'N\A'
root = Tk()
root.title('REDUX')
votes = []
text_boxes = []
string_vars = []
# voters = ['Kaylyn', 'Alex', 'Josh', 'Kay', 'Dan', 'Max', 'Kate', 'John', 'AJ', 'Mike']
voters = ['Kaylyn', 'Alex', 'Josh']
number_of_voters = len(voters)
scores = []
results = {}

def create_frame(number):

    f = Frame(root)
    r = StringVar()
    r.set('1')
    entry = Entry(f, width=15, textvariable=r, state='disabled')

    def increment():
        value = entry.get()
        try:
            int_value = int(value)
            if int_value < 10:
                int_value = int_value + 1
                r.set(str(int_value))
        except ValueError:
            if value == NO_VOTE_STRING:
                r.set(str(1))

    def excrement():
        value = entry.get()
        try:
            int_value = int(value)
            if int_value > 1:
                int_value = int_value - 1
                r.set(str(int_value))
            elif int_value == 1:
                r.set(NO_VOTE_STRING)
        except ValueError:
            pass

    def reset():
        r.set('1')

    label = Label(text=f'Item #{number}')
    label.pack()
    b1 = Button(f, text='/\\', command=increment)
    b2 = Button(f, text='\\/', command=excrement)
    b1.pack(side=LEFT, padx=3, pady=3)
    b2.pack(side=RIGHT, padx=3, pady=3)
    entry.pack(side=LEFT)
    f.pack()

    text_boxes.append(entry)
    string_vars.append(r)


def enter_votes():

    print('Votes Counted')

    individual_votes = []

    for textbox in text_boxes:
        if textbox.get() == NO_VOTE_STRING:
            individual_votes.append(0)
        else:
            individual_votes.append(int(textbox.get()))

    print(individual_votes)
    votes.append(individual_votes)

    for string_var in string_vars:
        string_var.set('1')

    if len(voters) > 1:
        voters.pop(0)
        name_variable.set(f'CURRENT VOTER: {voters[0]}')
    else:
        print('Last votes cast, calculating results')
        calculate_scores()


def calculate_scores():

    for x in range(0, int(num_items)):
        total = 0
        num_voters = 0
        for y in range(0, number_of_voters):
            print(f'Pie {x + 1} received vote: {votes[y][x]}')
            vote = votes[y][x]
            if vote != 0:
                total += vote
                num_voters += 1

        results[x+1] = total / num_voters

        print(f'Pie {x + 1} got a FINAL SCORE of {total} / {num_voters} = {total / num_voters}')

    print('\n\n')

    for key, value in results.items():
        print(f'Pie {key} got a final score of {value}')

    with open('results.txt', 'w') as output_file:
        json.dump(results, output_file)


num_items = input('How many pies enter the ring?')

name_variable = StringVar()
name_variable.set(f'CURRENT VOTER: {voters[0]}')
name_label = Label(textvariable=name_variable)
name_label.pack()

for item in range(1, int(num_items) + 1):
    create_frame(item)

enter_button = Button(text='Vote', command=enter_votes)
enter_button.pack()

root.mainloop()