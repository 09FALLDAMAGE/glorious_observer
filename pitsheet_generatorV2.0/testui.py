import tkinter as tk

select = tk.Tk()


select.geometry("250x100")


match_var = tk.StringVar()
json_var = tk.StringVar()



def submit():
    matchReq = match_var.get()
    JsonReq = json_var.get()

    match_var.set("")
    root.mainloop()



match_label = tk.Label(select, text='Match', font=('calibre', 10, 'bold'))


match_entry = tk.Entry(select, textvariable=match_var, font=('calibre', 10, 'normal'))


json_label = tk.Label(select, text='Json Path', font=('calibre', 10, 'bold'))


json_entry = tk.Entry(select, textvariable=json_var, font=('calibre', 10, 'normal'))


sub_btn = tk.Button(select, text='generate', command=submit)


match_label.grid(row=0, column=0)
match_entry.grid(row=0, column=1)
json_label.grid(row=1, column=0)
json_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

def pointers():
    def callback(e):
        x = e.x
        y = e.y
        print("Pointer is currently at %d, %d" % (x, y))

    select.bind('<Motion>', callback)


pointers()
select.mainloop()
