#pip install tkinter
#run the code either from terminal or IDLE 

import Tkinter as tk
def displaytext():
    global userinput
    text = userinput.get() 
    label_text = tk.Label(root, text=text)
    label_text.pack()  

root = tk.Tk()
root.title('Simple Program')

input_label = tk.Label(root, text="Enter the text")
input_label.pack()

text_box = tk.Entry(root)
text_box.pack()
text_box.focus_set()

submit_button = tk.Button(root,text='submit',command=displaytext)
submit_button.pack(side='bottom') 
root.mainloop()
