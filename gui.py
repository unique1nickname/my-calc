import customtkinter
import calculate_module as calc


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("My Calc")
        self.geometry("400x440")
        self.minsize(400, 440)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)


        self.entry_frame = EntryFrame(self)
        self.entry_frame.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nswe")

        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nswe")

    def get_result_button(self):
        self.entry_frame.get_answer()

    def add_symbol_button(self, num):
        self.entry_frame.add_symbol(num)

    def c_button(self):
        self.entry_frame.clear()

    def ac_button(self):
        self.entry_frame.all_clear()

class EntryFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.entry = customtkinter.CTkEntry(self, height=50)
        self.entry.grid(row=0, column=0, padx=0, pady=0, sticky="nswe")
        self.entry.focus()

    def get_answer(self):
        value = self.entry.get()
        answer = calc.calc(value)
        self.entry.delete(0, customtkinter.END)
        self.entry.insert(0, answer)

    def add_symbol(self, symbol):
        self.entry.insert(customtkinter.END, symbol)
    
    def clear(self):
        self.entry.delete(len(self.entry.get())-1, customtkinter.END)

    def all_clear(self):
        self.entry.delete(0, customtkinter.END)

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(tuple(i for i in range(4)), weight=1)
        self.grid_rowconfigure(tuple(i for i in range(6)), weight=1)

        self.buttons_names = [
            ["ac", "c", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "^", "+"],
            ["="]
        ]
        self.buttons_list = list()
        for i, row in enumerate(self.buttons_names):
            for j, column in enumerate(row):
                button = customtkinter.CTkButton(
                    self,
                    text=f"{column}",
                    command=lambda name=column: master.add_symbol_button(name)
                )
                button.grid(row=i, column=j, padx=5, pady=5, stick="nswe")
                self.buttons_list.append(button)
        
        self.buttons_list[-1].configure(command=master.get_result_button, fg_color="#B4A834", hover_color="#6D651D")
        self.buttons_list[0].configure(command=master.ac_button, fg_color="#A82A2A", hover_color="#771C1C")
        self.buttons_list[1].configure(command=master.c_button, fg_color="#A82A2A", hover_color="#771C1C")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()