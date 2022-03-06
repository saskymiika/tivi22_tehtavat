"""
Tehtävä 16.1 / kirjaudu.py
Miika Toivanen
miika.toivanen@edu.sasky.fi

Tee graafinen käyttöliittymä tkinter kirjasoa apuna käyttäen.

Ohjelma pyytää käyttäjältä nimen ja salasanan.

Kirjaudu.

Tervetuloa teksti
"""

# For the sake of convenience, I created GUI class which uses the tkinter library, 
# to make to the code slightly more compact.

from gui import GUI


def main():
    # Luodaan itse tehty GUI objekti, joka käyttää Tkinter kirjastoa
    # käyttöliittymän luomisessa.
    app = GUI('Kirjautuminen')

    # Defaults metodilla määritetään ohjelman oletustyyli, jonka määritelmiä kaikki komponentit noudattavat.
    app.defaults({
        'main': {
            'pad': 10, 
        },
        'label': {
            'font': ('Helvetica', 12),
            'pad': 6,
            'width': 14
        },
        'field': {
            'width': 20
        }
    })

    # luodaan frame jolle annetaan classname 'main' tyylimääritelmiä varten.
    app.add_frame(type="grid", classname='main')

    # frame is now == app.frames[0]
    # To add stuff into the frame, refer to the app.frames[0] with each item
    app.label(app.frames[0], 'Käyttäjätunnus', classname='label').grid(column=0, row=0)
    user = app.entry(app.frames[0], classname='field')
    user.grid(column=1, row=0)
    
    app.label(app.frames[0], 'Salasana', classname='label').grid(column=0, row=1)
    app.entry(app.frames[0], type="password", classname='field').grid(column=1, row=1)

    # new_frame korvaa aiemman näkymän, uudella näkymällä.
    def new_frame():
        name = user.get()
        app.remove_frames()
        app.add_frame(classname='main')
        app.label(app.frames[0], f'Tervetuloa {name}!', classname='label').pack()
        app.button(app.frames[0], "poistu", callback=app.end, classname='field').pack()

    app.button(app.frames[0], "Kirjaudu sisään", callback=new_frame, classname='field').grid(column=1, row=2)


    app.run()


if __name__ == "__main__":
    main()