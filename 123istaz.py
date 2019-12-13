#   a123_apple_1.py
import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)


apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

#new code

screen_width = 400
screen_height = 400
letter_list =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#


active_letter = []
apple_list = []
number_of_apples = 5

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

wn.bgpic("background.gif")
apple = trtl.turtle()
apple.penup()
wn.tracer(False)



apple = trtl.Turtle()
drawer = trtl.Turtle()
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

draw_apple(apple)

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  #new
  reset_apple(apple)


def reset_apple(active_apple,):
  global current_letter
  length_of_list = len(letter_list)
  if(length_of_list !=0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2), rand.randit(-(screen_height)/2, (screen_height)/2))
    draw_apple(active_apple, length_of_list.pop(index))

def draw_letter(active_apple, letter):
  active_apple.color("white")
  remeber_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.setpos(remeber_position)


draw_apple(apple, "A")
wn.onkeypress(drop_apple, "A")

wn.listen()
trtl.mainloop()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 




active_apple.setpos(remeber_positions)



# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
wn.onkeypress(draw_an_A, "a")

def check_letter_A():
  drop_apple()
  if (current_letter == "A")
  drop_apple()
def check_letter_B():
  drop_apple()
  if (current_letter == "B")
  drop_apple()
def check_letter_C():
  drop_apple()
  if (current_letter == "C")
  drop_apple()
def check_letter_D():
  drop_apple()
  if (current_letter == "D")
  drop_apple()
def check_letter_E():
  drop_apple()
  if (current_letter == "E")
  drop_apple()
def check_letter_F():
  drop_apple()
  if (current_letter == "F")
  drop_apple()
def check_letter_G():
  drop_apple()
  if (current_letter == "G")
  drop_apple()
def check_letter_H():
  drop_apple()
  if (current_letter == "H")
  drop_apple()
def check_letter_I():
  drop_apple()
  if (current_letter == "I")
  drop_apple()
def check_letter_J():
  drop_apple()
  if (current_letter == "J")
  drop_apple()
def check_letter_K():
  drop_apple()
  if (current_letter == "K")
  drop_apple()
def check_letter_L():
  drop_apple()
  if (current_letter == "L")
  drop_apple()
def check_letter_M():
  drop_apple()
  if (current_letter == "M")
  drop_apple()
def check_letter_N():
  drop_apple()
  if (current_letter == "N")
  drop_apple()
def check_letter_O():
  drop_apple()
  if (current_letter == "O")
  drop_apple()
def check_letter_P():
  drop_apple()
  if (current_letter == "P")
  drop_apple()
def check_letter_Q():
  drop_apple()
  if (current_letter == "Q")
  drop_apple()
def check_letter_R():
  drop_apple()
  if (current_letter == "R")
  drop_apple()
def check_letter_S():
  drop_apple()
  if (current_letter == "S")
  drop_apple()
def check_letter_T():
  drop_apple()
  if (current_letter == "T")
  drop_apple()
def check_letter_U():
  drop_apple()
  if (current_letter == "U")
  drop_apple()
def check_letter_V():
  drop_apple()
  if (current_letter == "V")
  drop_apple()
def check_letter_W():
  drop_apple()
  if (current_letter == "W")
  drop_apple()
def check_letter_X():
  drop_apple()
  if (current_letter == "X")
  drop_apple()
def check_letter_Y():
  drop_apple()
  if (current_letter == "Y")
  drop_apple()
def check_letter_Z():
  drop_apple()
  if (current_letter == "Z")
  drop_apple()

draw_apple(apple, "A")
wn.onkeypress(check_letter_A, "a")
wn.onkeypress(check_letter_B, "b")
wn.onkeypress(check_letter_C, "c")
wn.onkeypress(check_letter_D, "d")
wn.onkeypress(check_letter_E, "e")
wn.onkeypress(check_letter_F, "f")
wn.onkeypress(check_letter_G, "g")
wn.onkeypress(check_letter_H, "h")
wn.onkeypress(check_letter_I, "i")
wn.onkeypress(check_letter_J, "j")
wn.onkeypress(check_letter_k, "k")
wn.onkeypress(check_letter_L, "l")
wn.onkeypress(check_letter_M, "m")
wn.onkeypress(check_letter_N, "n")
wn.onkeypress(check_letter_O, "o")
wn.onkeypress(check_letter_P, "p")
wn.onkeypress(check_letter_Q, "q")
wn.onkeypress(check_letter_R, "r")
wn.onkeypress(check_letter_S, "s")
wn.onkeypress(check_letter_T, "t")
wn.onkeypress(check_letter_U, "u")
wn.onkeypress(check_letter_V, "v")
wn.onkeypress(check_letter_W, "w")
wn.onkeypress(check_letter_X, "x")
wn.onkeypress(check_letter_Y, "y")
wn.onkeypress(check_letter_Z, "z")

current_letter="A"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")


wn.listen()
trtl.mainloop()