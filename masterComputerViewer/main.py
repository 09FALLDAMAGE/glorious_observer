import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Canvas, Frame

root = tk.Tk()

geo = [1535, 840]

graphPos = [60, 400]

mode = [
    "Dark",
    "Light"
]

root.geometry(f"{geo[0]}x{geo[1]}")
canvas = Canvas(root, width=geo[0], height=geo[1])
canvas.pack()


data1 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'Total Points': [12, 12, 25, 23, 14, 35, 12, 18, 17, 0]
         }

data2 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'Auto Points': [25, 15, 13, 23, 17, 46, 10, 8, 9, 0]
         }

data3 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'TeleCubes': [17, 13, 11, 5, 15, 32, 5, 8, 6, 0]
         }

data4 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'TeleCones': [25, 15, 13, 23, 17, 46, 10, 8, 6, 0]
         }

data5 = {'Match': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'Endgame': [10, 10, 10, 5, 10, 10, 10, 0, 0, 0]
         }

options = [
    "Total Match Points",
    "Auto Points",
    "TeleCubes",
    "TeleCones",
    "Endgame Points"
]

global totals
global auto
global cubes
global cones
global endGame


def thing(event):
    df1 = pd.DataFrame(data1)

    df2 = pd.DataFrame(data2)

    df3 = pd.DataFrame(data3)

    df4 = pd.DataFrame(data4)

    df5 = pd.DataFrame(data5)

    if (event == options[0]):
        try:
            kill()

            figure1 = plt.Figure(figsize=(5, 4), dpi=100)
            ax1 = figure1.add_subplot(111)
            totals = FigureCanvasTkAgg(figure1, root)
            totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
            df1.plot(kind='line', legend=True, ax=ax1, color='blue', marker='o', fontsize=10)
            ax1.set_title('Total Points')

            totals.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)
        except:
            figure1 = plt.Figure(figsize=(5, 4), dpi=100)
            ax1 = figure1.add_subplot(111)
            totals = FigureCanvasTkAgg(figure1, root)
            totals.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df1 = df1[['Match', 'Total Points']].groupby('Match').sum()
            df1.plot(kind='line', legend=True, ax=ax1, color='red', marker='o', fontsize=10)
            ax1.set_title('Total Points')

            totals.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)


    elif (event == options[1]):
        try:
            kill()

            figure2 = plt.Figure(figsize=(5, 4), dpi=100)
            ax2 = figure2.add_subplot(111)
            auto = FigureCanvasTkAgg(figure2, root)
            auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
            df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
            ax2.set_title('Auton Points Per Match')

            auto.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)
        except:
            figure2 = plt.Figure(figsize=(5, 4), dpi=100)
            ax2 = figure2.add_subplot(111)
            auto = FigureCanvasTkAgg(figure2, root)
            auto.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df2 = df2[['Match', 'Auto Points']].groupby('Match').sum()
            df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
            ax2.set_title('Auton Points Per Match')

            auto.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)


    elif (event == options[2]):
        try:
            kill()

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            cubes = FigureCanvasTkAgg(figure3, root)
            cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
            df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
            ax3.set_title('Teleop Cubes per Match')

            cubes.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)
        except:
            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            cubes = FigureCanvasTkAgg(figure3, root)
            cubes.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df3 = df3[['Match', 'TeleCubes']].groupby('Match').sum()
            df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
            ax3.set_title('Teleop Cubes per Match')

            cubes.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)


    elif (event == options[3]):
        try:
            kill()

            figure4 = plt.Figure(figsize=(5, 4), dpi=100)
            ax4 = figure4.add_subplot(111)
            cones = FigureCanvasTkAgg(figure4, root)
            cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df4 = df4[['Match', 'TeleCubes']].groupby('Match').sum()
            df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
            ax4.set_title('Teleop Cones per Match')

            cones.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)
        except:
            figure4 = plt.Figure(figsize=(5, 4), dpi=100)
            ax4 = figure4.add_subplot(111)
            cones = FigureCanvasTkAgg(figure4, root)
            cones.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df4 = df4[['Match', 'TeleCones']].groupby('Match').sum()
            df4.plot(kind='line', legend=True, ax=ax4, color='r', marker='o', fontsize=10)
            ax4.set_title('Teleop Cones per Match')

            cones.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)


    elif (event == options[4]):
        try:
            kill()

            figure5 = plt.Figure(figsize=(5, 4), dpi=100)
            ax5 = figure5.add_subplot(111)
            endGame = FigureCanvasTkAgg(figure5, root)
            endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
            df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
            ax5.set_title('Endgame Points')

            endGame.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)
        except:
            figure5 = plt.Figure(figsize=(5, 4), dpi=100)
            ax5 = figure5.add_subplot(111)
            endGame = FigureCanvasTkAgg(figure5, root)
            endGame.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df5 = df5[['Match', 'Endgame']].groupby('Match').sum()
            df5.plot(kind='line', legend=True, ax=ax5, color='r', marker='o', fontsize=10)
            ax5.set_title('Endgame Points')

            endGame.get_tk_widget().place(x=graphPos[0], y=graphPos[1], in_=root)


def kill():
    totals.get_tk_widget().destroy()
    auto.get_tk_widget().destroy()
    cubes.get_tk_widget().destroy()
    cones.get_tk_widget().destroy()
    endGame.get_tk_widget().destroy()


def pointers():
    def callback(e):
        x = e.x
        y = e.y
        print("Pointer is currently at %d, %d" % (x, y))

    root.bind('<Motion>', callback)


def teamImage(tM):
    image = Image.open(f"{tM}.jpg")

    # Resize the image using resize() method
    resize_image = image.resize((413, 310))

    img = ImageTk.PhotoImage(resize_image)

    # create label and add resize image
    label1 = tk.Label(image=img)
    label1.image = img
    label1.pack()

    label1.place(x=100, y=30)


def teamtitles(tM):
    canvas.create_text(geo[0] / 2, 40, text=f'Team {tM}', font=('Arial', 25))
    canvas.create_text(geo[0] / 2, 90, text=f'The Monsters', font=('Arial', 25))


def modes(event):
    if (event == mode[0]):
        try:
            canvas.delete('backGround')

            canvas.create_rectangle(0, 0, geo[0], geo[1], tags='backGround', fill='grey')
            canvas.lower('backGround')
        except:
            bg = canvas.create_rectangle(0, 0, geo[0], geo[1], tags='backGround', fill='grey')
            canvas.lower('backGround')


    elif (event == mode[1]):
        try:
            canvas.delete('backGround')

            canvas.create_rectangle(0, 0, geo[0], geo[1], tags='backGround', fill='white')
            canvas.lower('backGround')
        except:
            bg = canvas.create_rectangle(0, 0, geo[0], geo[1], tags='backGround', fill='white')
            canvas.lower('backGround')


def pitDisplay():
    # finals
    canvas.create_text(700, 200, text='Drive Type', font=('Arial', 15))

    canvas.create_text(700, 275, text='Weight', font=('Arial', 15))

    canvas.create_text(700, 350, text='Size', font=('Arial', 15))


    canvas.create_text(700, 225, text='Tank', font=('Arial', 15))

    canvas.create_text(700, 300, text='110 lbs', font=('Arial', 15))

    canvas.create_text(700, 375, text='2ft x 2ft, 25% of Charger', font=('Arial', 15))





variable = tk.StringVar()
variable.set(options[0])
thing(options[0])

drop = tk.OptionMenu(root, variable, *options, command=thing)
drop.pack()
drop.place(x=250, y=360, in_=root)

modeVar = tk.StringVar()
modeVar.set(mode[0])

modeDrop = tk.OptionMenu(root, modeVar, *mode, command=modes)
modeDrop.pack()
modeDrop.place(x=15, y=15, in_=root)

teamImage(308)
teamtitles(308)
pitDisplay()


pointers()

root.mainloop()
