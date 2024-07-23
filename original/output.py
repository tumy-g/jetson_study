import tkinter as tk

# グルーバル変数たち
parameter_name = ['人差し指', "中指", "小指"]
w, h = 400, 300
angle = 90
t = 0

class FeedBackSystem(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=w, height=h)
        self.lasso = 0
        self.frame_count = 0
        self.scale_values = [10,20,30]

        self.view()
    def update_scale(self):
        print("hello")

    def view(self):
        #
        self.labelframe_parameter = tk.LabelFrame(self.master, text="パラメータ", width=w-50, height=h-10, font=("MS Pゴシック", 10, "bold"))
        self.labelframe_parameter.propagate(False)

        print(self.frame_count)
        
        #
        for i in range(3):
            scale_value = tk.IntVar()
            try:
                scale_value.set(angle)
            except:
                scale_value.set(0)

            #ラベル(一番左)
            label = tk.Label(text=parameter_name[i])
            label.grid(row=i+1, column=0, padx=10, pady=10)

            #バー(真ん中)
            scale = tk.Scale(to=180, variable=self.scale_values[i], orient=tk.HORIZONTAL, width=10, showvalue=False, length=150)
            scale.grid(row=i+1, column=1, padx=10, pady=10)

            #なす角
            entry = tk.Entry(textvariable=self.scale_values[i], width=3, state=tk.DISABLED)

            entry.grid(row=i+1,column=3,padx=10)

if __name__=="__main__":
    root = tk.Tk()
    root.title("Slider GUI")
    app = FeedBackSystem(master=root)
    root.mainloop()