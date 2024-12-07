import pgzrun, random, time

TITLE= "WELCOME TO QUESTIONAIRE!"

WIDTH= 900
HEIGHT= 700

marquee_box= Rect(0,0,WIDTH,80)
question_box= Rect(0,0,710,150)
answer_box1= Rect(0,0,310,150)
answer_box2= Rect(0,0,310,150)
answer_box3= Rect(0,0,310,150)
answer_box4= Rect(0,0,310,150)
timer_box= Rect(0,0,150,150)
skip_box= Rect(0,0,150,300)

score= 0
time_left=10
question_file= "questions.txt"
game_over= False

marquee_message= ""
questions= []
answer_boxes= [answer_box1 ,answer_box2, answer_box3, answer_box4]
question_count= 0
question_index= 0
marquee_box.move_ip(0, 0)
question_box.move_ip(20,100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
timer_box.move_ip(750, 100)
skip_box.move_ip(750, 270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(timer_box,"orange")
    screen.draw.filled_rect(skip_box,"dark green")  
    for i in answer_boxes:
        screen.draw.filled_rect(i,"light blue")
    marquee_message= TITLE+ f"{question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color= "white")
    screen.draw.textbox(str(time_left), timer_box, color= "white")
    screen.draw.textbox("skip", skip_box, color= "white", angle= 90)
    screen.draw.textbox(questions[0].strip(), question_box, color= "white")
    index= 1
    for i in answer_boxes:
        screen.draw.textbox(questions[index].strip(), i, color= "white")
    index= index+ 1

def



def



def



def



