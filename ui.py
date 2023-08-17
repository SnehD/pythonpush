from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.score_labe=Label(text=f"Score:0",fg="white",bg=THEME_COLOR,font=("Arial",20,"bold"))
        self.score_labe.grid(row=0,column=1)
        self.canvas=Canvas(width=400,height=250,bg="white")
        self.question_text=self.canvas.create_text(200,125,width=280,
                                text="Some Question",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_image=PhotoImage(file="images/true.png")
        # self.true_button(image=true_image)
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_click)
        self.true_button.grid(row=2,column=1)
        false_image=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_click)
        self.false_button.grid(row=2,column=0)
        self.get_next_question()


        self.window.mainloop()
    def get_next_question(self):
     self.canvas.config(bg="white")
     if self.quiz.still_has_questions():
       # self.score_labe.config(text=f"Score:{self.quiz.score}")
       question= self.quiz.next_question()
       self.canvas.itemconfig(self.question_text,text=question)
     else:
         self.canvas.itemconfig(self.question_text,text="you have reached end of questions")
         self.true_button.config(state="disabled")
         self.false_button.config(state="disabled")
    def true_click(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_click(self):
       self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_labe.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

