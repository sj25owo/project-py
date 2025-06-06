import tkinter as tk
from tkinter import messagebox

class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)

        self.default_size = {}

        self.after(0, self.save_size)

    def save_size(self):
        self.default_size['width'] = int(self.cget("width"))
        self.default_size['height'] = int(self.cget("height"))

    def enter(self, event):
        self.config(
            width=self.default_size['width'] + 2,
            height=self.default_size['height'] + 2
        )

    def leave(self, event):
        self.config(**self.default_size)

def start_window() :
    global window
    global result
    window = tk.Tk()
    window.title("테스트 중심 음악 추천 프로그램")
    window.geometry("600x400")
    window.configure(bg="white")
    
    global label
    label = tk.Label(window, text="테스트 중심 음악 추천 프로그램", font=("나눔고딕", 14, "bold"), fg="black", bg="white")
    label.pack(pady=40)

    global start_btn
    start_btn = Button(window, text="시작", font=("나눔고딕", 12), bg="#a8d8ea", width=12, command=start_test)

    start_btn.pack(pady=10)

    window.mainloop()
    return result

def start_test():
    yes_btn = Button(window, text="YES", font=("나눔고딕", 12), bg="#a8d8ea", width=12)
    no_btn = Button(window, text="NO", font=("나눔고딕", 12), bg="#f8a5c2", width=12)

    start_btn.pack_forget()
    yes_btn.place(x=200, y=300, anchor='center')
    no_btn.place(x=400, y=300, anchor='center')

    def q1():
        label.config(text="Q. 밝은 분위기의 노래를 선호하시나요?")
        yes_btn.config(command=q2)
        no_btn.config(command=q7)

    def q2():
        label.config(text="Q. 리듬감 있는 음악을 선호하시나요?")
        yes_btn.config(command=q3)
        no_btn.config(command=q6)

    def q3():
        label.config(text="Q. 아이돌 스타일의 음악을 선호하시나요?")
        yes_btn.config(command=lambda: show_result("K-POP"))
        no_btn.config(command=q4)

    def q4():
        label.config(text="Q. 밴드사운드를 선호하시나요?")
        yes_btn.config(command=q5)
        no_btn.config(command=lambda: show_result("Dance Pop"))

    def q5():
        label.config(text="Q. 랩처럼 리듬감있는 음악을 선호하시나요?")
        yes_btn.config(command=lambda: show_result("Hip-Hop"))
        no_btn.config(command=lambda: show_result("Rock"))

    def q6():
        label.config(text="Q. 부드러운 목소리의 음악을 선호하시나요?")
        yes_btn.config(command=lambda: show_result("Indie Pop"))
        no_btn.config(command=lambda: show_result("Pop"))

    def q7():
        label.config(text="Q. 가사를 중요하게 생각하시나요?")
        yes_btn.config(command=lambda: show_result("Ballad"))
        no_btn.config(command=q8)

    def q8():
        label.config(text="Q. 악기 연주가 중심인 음악을 선호하시나요??")
        yes_btn.config(command=q9)
        no_btn.config(command=lambda: show_result("Acoustic"))

    def q9():
        label.config(text="Q. 클래식 연주를 선호하나요?")
        yes_btn.config(command=lambda: show_result("Classical"))
        no_btn.config(command=lambda: show_result("Jazz"))

    def show_result(x):
        messagebox.showinfo("테스트 결과", f"당신에게 추천하는 장르는 {x}")
        retest = messagebox.askokcancel("테스트 결과", f"{x} 장르의 노래를 추천해드릴까요?\n취소를 선택하시면 테스트를 다시 진행합니다.")
        if not retest:
            q1()
        else:
            global result
            result = x
            window.quit()

    q1()