from tkinter import *

cua_so = Tk()

cua_so.title("Đây là máy tính ko cầm tay đc")
cua_so.geometry("450x350")

# phần tính toán


# phần hiển thị
label = Label(cua_so, text='', height=2, border=1)
label.grid(column=1)


class NutNhan():
    def __init__(self, text, col, row):
        self.text = text
        self.obj = Button(cua_so, text=text, relief='groove', width=10, command=self.run)
        self.obj.grid(column=col, row=row)

    def run(self):
        current_text = label.cget('text')
        if self.text == '=':
            try:
                kqua = str(eval(current_text))
                label.config(text=kqua)
            except:
                label.config(text='error')
        elif self.text == 'DEL':
            label.config(text=current_text[:-1])
        elif self.text == 'MR':
            label.config(text='')
        else:
            label.config(text=current_text + self.text)


def create_buttons(root):
    # Danh sách các nút với (text, cột, hàng)
    buttons = [
        ('MR', 0, 1), ('DEL', 1, 1), ('(', 2, 1), (')', 3, 1),
        ('1', 0, 2), ('2', 1, 2), ('3', 2, 2), ('+', 3, 2),
        ('4', 0, 3), ('5', 1, 3), ('6', 2, 3), ('-', 3, 3),
        ('7', 0, 4), ('8', 1, 4), ('9', 2, 4), ('*', 3, 4),
        ('.', 0, 5), ('0', 1, 5), ('=', 2, 5), ('/', 3, 5)
    ]

    for (text, col, row) in buttons:
        NutNhan(text, col, row)


create_buttons(cua_so)
cua_so.mainloop()
