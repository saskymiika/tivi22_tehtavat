"""
Viikko 16 Vaativa / nelilaskin.py
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from gui import GUI


values = ['']
v_index = 0

app = GUI('Nelilaskin')
app.defaults({
    'expression': {
        'pad': 6
    },
    'label': {
        'font': ('Courier', 16)
    },
    'result': {
        'font': ('Courier', 16, 'bold')
    },
    'buttons': {
        'pad': 10
    },
    'number': {
        'pad': (0, 12)
    }
})

app.add_frame(classname='expression').grid(sticky='W')
c_expression = app.label(app.frames[0], '', classname='label')
c_expression.grid(column=0, row=0)

app.add_frame(classname='buttons').grid()

total = app.label(app.frames[0], '', classname='result')
total.grid(column=2, row=0)

def update_expression():
    global c_expression
    exp_text = ' '.join(values)
    c_expression.config(text=exp_text)

def add_to_cv(value: str):
    values[v_index] += value
    update_expression()


def del_cv():
    global v_index
    if len(values[v_index]) > 0:
        values[v_index] = values[v_index][0:len(values[v_index])-1]
        if len(values[v_index]) == 0:
            if v_index > 0:
                values.pop(len(values)-1)
                values.pop(len(values)-1)
                v_index = len(values)-1

    update_expression()

def set_operation(char: str):
    global v_index
    values.append(char)
    values.append('')
    v_index = len(values)-1
    update_expression()

def calculate():
    result = eval(' '.join(values))  
    total.config(text=f' = {result}')

def reset():
    global v_index
    global values
    values = ['']
    v_index = 0
    total.config(text='')
    update_expression()


app.button(app.frames[1], '7', classname='number', callback=lambda: add_to_cv('7')).grid(column=0, row=0)
app.button(app.frames[1], '8', classname='number', callback=lambda: add_to_cv('8')).grid(column=1, row=0)
app.button(app.frames[1], '9', classname='number', callback=lambda: add_to_cv('9')).grid(column=2, row=0)

app.button(app.frames[1], '4', classname='number', callback=lambda: add_to_cv('4')).grid(column=0, row=1)
app.button(app.frames[1], '5', classname='number', callback=lambda: add_to_cv('5')).grid(column=1, row=1)
app.button(app.frames[1], '6', classname='number', callback=lambda: add_to_cv('6')).grid(column=2, row=1)

app.button(app.frames[1], '1', classname='number', callback=lambda: add_to_cv('1')).grid(column=0, row=2)
app.button(app.frames[1], '2', classname='number', callback=lambda: add_to_cv('2')).grid(column=1, row=2)
app.button(app.frames[1], '3', classname='number', callback=lambda: add_to_cv('3')).grid(column=2, row=2)
app.button(app.frames[1], '0', classname='number', callback=lambda: add_to_cv('0')).grid(column=0, row=3)
app.button(app.frames[1], 'reset', classname='number', callback=reset).grid(column=1, row=3)
app.button(app.frames[1], '=', classname='number', callback=calculate).grid(column=0, row=4)
app.button(app.frames[1], 'del', classname='number', callback=lambda: del_cv()).grid(column=2, row=3)

app.button(app.frames[1], '+', classname='number', callback=lambda: set_operation('+')).grid(column=4, row=0)
app.button(app.frames[1], '-', classname='number', callback=lambda: set_operation('-')).grid(column=4, row=1)
app.button(app.frames[1], '/', classname='number', callback=lambda: set_operation('/')).grid(column=4, row=2)
app.button(app.frames[1], '*', classname='number', callback=lambda: set_operation('*')).grid(column=4, row=3)



def main():

    app.run()


if __name__ == "__main__":
    main()