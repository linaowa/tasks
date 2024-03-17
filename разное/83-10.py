import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Создание основного окна
root = tk.Tk()
root.title("калькулятор")

# Настройка цвета фона окна
root.configure(bg='#ffd1dc')

# Виджет для ввода
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
button_bg_color = '#f1829   `d'  # Новый цвет для кнопок

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda b=button: on_button_click(b) if b != '=' else calculate(),
              bg=button_bg_color).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

c_bg_color = '#f1828d'

# Кнопка для очистки ввода
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), bg=c_bg_color, command=clear_entry).grid(
                                                                row=row_val, column=col_val)

# Запуск главного цикла
root.mainloop()
