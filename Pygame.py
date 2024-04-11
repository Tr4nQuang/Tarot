# ---------------------------------------- IMPORT NEEDED LIBRARIES ----------------------------------------

# Main.py
from openai import OpenAI
import random
import time

# Pygame
import pygame
import pygame_gui
import sys
import os

pygame.init()
clock = pygame.time.Clock()

# ---------------------------------------- MAIN.PY ----------------------------------------

card_list = []
card_array = [
    # Arcade
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant",
    "The Lovers", "The Chariot", "Strength", "The Hermit", "The Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon",
    "The Sun", "Judgment", "The World",

    # Cups
    "Ace of Cups", "2 of Cups", "3 of Cups", "4 of Cups", "5 of Cups", "6 of Cups", "7 of Cups",
    "8 of Cups", "9 of Cups", "10 of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups",
    "King of Cups",

    # Pentacles
    "Ace of Pentacles", "2 of Pentacles", "3 of Pentacles", "4 of Pentacles", "5 of Pentacles",
    "6 of Pentacles", "7 of Pentacles", "8 of Pentacles", "9 of Pentacles", "10 of Pentacles",
    "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles",

    # Swords
    "Ace of Swords", "2 of Swords", "3 of Swords", "4 of Swords", "5 of Swords", "6 of Swords",
    "7 of Swords", "8 of Swords", "9 of Swords", "10 of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords",

            # Wands
    "Ace of Wands", "2 of Wands", "3 of Wands", "4 of Wands", "5 of Wands", "6 of Wands", "7 of Wands",
    "8 of Wands", "9 of Wands", "10 of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands",
    "King of Wands"
]

# Shuffle cards
def Shuffle_card(times):
    random.seed(time.time())
    while times > 0:
        id1 = random.randint(0,77)
        id2 = random.randint(0,77)

        card_array[id1], card_array[id2] = card_array[id2], card_array[id1]
        times -= 1
    
# ---------------------------------------- BUILD CLASS ----------------------------------------

# Build class Button
class Button_Title():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		else: 
			return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "cyan")
		else:
			self.text = main_font.render(self.text_input, True, "white")

class Button_Content():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = secondary_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		else: 
			return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = secondary_font.render(self.text_input, True, "black")
		else:
			self.text = secondary_font.render(self.text_input, True, "white")

class Button_Card():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, (self.x_pos, self.y_pos))

	def checkForInput(self, position, card_status_list, card_order_number, x_change):
		if card_status_list[card_order_number + 1]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 1) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
			
		elif card_status_list[card_order_number + 2]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 2) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
			
		elif card_status_list[card_order_number + 3]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 3) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
		
		elif card_status_list[card_order_number + 4]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 4) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
		
		elif card_status_list[card_order_number + 5]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 5) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False

		elif card_status_list[card_order_number + 6]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 6) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
		
		elif card_status_list[card_order_number + 7]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 7) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False
		
		else:
			if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
				return True
			else: 
				return False

	def animation(self, position, card_status_list, card_order_number, x_change):
		if card_status_list[card_order_number + 1]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 1) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
			
		elif card_status_list[card_order_number + 2]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 2) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
			
		elif card_status_list[card_order_number + 3]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 3) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
		
		elif card_status_list[card_order_number + 4]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 4) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
		
		elif card_status_list[card_order_number + 5]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 5) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200

		elif card_status_list[card_order_number + 6]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 6) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
		
		elif card_status_list[card_order_number + 7]:
			if position[0] in range(self.rect.left, self.rect.left + x_change * 7) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200
		
		else:
			if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
				self.y_pos = 175
			else: 
				self.y_pos = 200

# ---------------------------------------- SCREEN ----------------------------------------
			   
# The main screen
size = (1280,720)
screen = pygame.display.set_mode(size)

# The title and set up font
pygame.display.set_caption("Bói Tarot")
main_font = pygame.font.Font((os.path.join('Font', 'PlayfairDisplay-VariableFont_wght.ttf')), 100)
secondary_font = pygame.font.Font((os.path.join('Font', 'PlayfairDisplay-VariableFont_wght.ttf')), 50)
conclusion_font = pygame.font.Font((os.path.join('Font', 'PlayfairDisplay-VariableFont_wght.ttf')), 15)

# The icon
icon = pygame.image.load(os.path.join('Image', 'icon.png')).convert()
pygame.display.set_icon(icon)

# ---------------------------------------- START SCREEN ----------------------------------------

# Screen
start_screen = pygame.image.load(os.path.join('Image', 'start_screen.png')).convert()
start_screen_rect = start_screen.get_rect(topleft = (0,0))

# Start button
start_button_surface = pygame.image.load(os.path.join('Image', 'start_button.png')).convert()
start_button_surface = pygame.transform.scale(start_button_surface, (330, 100))

start_button = Button_Title(start_button_surface, 650, 450, "Bắt đầu")

# Function for start_screen
def start_screen_function():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if start_button.checkForInput(pygame.mouse.get_pos()):
					return True

		screen.blit(start_screen, start_screen_rect)   
		start_button.update()
		start_button.changeColor(pygame.mouse.get_pos())

		pygame.display.update()

# ---------------------------------------- QUESTION SCREEN ----------------------------------------

# Screen
question_screen = pygame.image.load(os.path.join('Image', 'question_screen.png')).convert()
question_screen_rect = question_screen.get_rect(topleft = (0,0))

# Input box
manager = pygame_gui.UIManager((1280, 720))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((600, 375), (600, 50)), manager=manager, object_id='#main_text_entry')

def get_user_name():
	while True:
		UI_REFRESH_RATE = clock.tick(60)/1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
				event.ui_object_id == '#main_text_entry'):
				return event.text
			
			manager.process_events(event)
		
		if text_input.hovered:
			# Set mouse cursor to normal form
			pygame.mouse.set_cursor(pygame.cursors.arrow)

		manager.update(UI_REFRESH_RATE)

		manager.draw_ui(screen)

		pygame.display.update()

question = ""

# Function for question_screen
def question_screen_function():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.blit(question_screen, question_screen_rect)

		pygame.display.update()

		return get_user_name()

# ---------------------------------------- SHUFFLE CARD SCREEN ----------------------------------------

# Screen
shuffle_card_screen = pygame.image.load(os.path.join('Image', 'shuffle_card_screen.png')).convert()
shuffle_card_screen_rect = shuffle_card_screen.get_rect(topleft = (0,0))

# Load the image for the card
card = pygame.image.load(os.path.join('Image', 'card.png')).convert()
card = pygame.transform.scale(card, (116, 199.33))

# Define x & y for card
# card_x = 582
# card_y = card_y

def print_card(x,y):
	screen.blit(card, (x, y))

# Animation for shuffle card
def shuflle_card_animation():
	# ----- Setting ------
	# Speed: 2 | 3 | 6 | 41|
	speed = 3
	amount = 40

	# Create a list to store all card_x
	card_x = [582] * amount
	card_y = 200

	# Define x_change
	x_change = 246

	# Create a list to store all x_after_change
	x_after_change = []

	random.seed(time.time())
	for i in range(amount):
		id = random.randint(0,1)

		if id == 0:
			x_after_change.append(582 - x_change)

		else:
			x_after_change.append(582 + x_change) 

	# Create variable that's needed in while loop
	check = True

	id_left = False
	card_left_x = 336

	id_right = False
	card_right_x = 828

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		if check:
			check = False

			for i in range(amount):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()

				if x_after_change[i] < card_x[i]:
					while x_after_change[i] < card_x[i]:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
								sys.exit()

						card_x[i] -= speed

						screen.blit(shuffle_card_screen, shuffle_card_screen_rect)
						if i != amount - 1: 
							print_card(582, card_y)

						if id_left:
							print_card(336, card_y)

						if id_right:
							print_card(828, card_y)

						print_card(card_x[i], card_y)

						pygame.display.update()

					if not id_left:
						id_left = True

				else:
					while x_after_change[i] > card_x[i]:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
								sys.exit()

						card_x[i] += speed

						screen.blit(shuffle_card_screen, shuffle_card_screen_rect)
						if i != amount - 1:
							print_card(582, card_y)

						if id_left:
							print_card(336, card_y)

						if id_right:
							print_card(828, card_y)

						print_card(card_x[i], card_y)

						pygame.display.update()

					if not id_right:
						id_right = True

				pygame.display.update()

		screen.blit(shuffle_card_screen, shuffle_card_screen_rect)

		print_card(card_left_x, card_y)
		card_left_x += speed

		print_card(card_right_x, card_y)
		card_right_x -= speed

		if card_left_x > 582 and card_right_x < 582:
			print_card(card_left_x, card_y)
			print_card(card_right_x, card_y)

			return

		pygame.display.update()

# Shuffle button 
shuffle_card_button_surface = pygame.image.load(os.path.join('Image', 'shuffle_card_button.png')).convert()
shuffle_card_button_surface = pygame.transform.scale(shuffle_card_button_surface, (250, 70))

shuffle_card_button = Button_Content(shuffle_card_button_surface, 380, 530, "Xào bài")
shuffle_card_confirm_button = Button_Content(shuffle_card_button_surface, 900, 530, "Xác nhận")

# Function for shuffle card screen
def shuffle_card_screen_function():
	shuffle_card_button_status = False

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if shuffle_card_button.checkForInput(pygame.mouse.get_pos()):
					shuffle_card_button_status =  True
					Shuffle_card(100000)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if shuffle_card_confirm_button.checkForInput(pygame.mouse.get_pos()):
					return True

		screen.blit(shuffle_card_screen, shuffle_card_screen_rect)
		print_card(582, 200)

		shuffle_card_button.update()
		shuffle_card_button.changeColor(pygame.mouse.get_pos())

		shuffle_card_confirm_button.update()
		shuffle_card_confirm_button.changeColor(pygame.mouse.get_pos())

		if shuffle_card_button_status: 
			shuflle_card_animation()
			shuffle_card_button_status = False

		pygame.display.update()

# ---------------------------------------- DRAW CARD SCREEN ----------------------------------------
	
# Screen
draw_card_screen = pygame.image.load(os.path.join('Image', 'draw_card_screen.png')).convert()
draw_card_screen_rect = draw_card_screen.get_rect(topleft = (0,0))

# x & y at the first of cards
card_x_left = 45
card_y = 200
change = 14

# Create a list to store all card_x after change
card_x_list = [card_x_left]
	
for i in range(1, 78):
	card_x_list.append(card_x_list[i-1] + change)

# Create a list to store all card status
card_status = [True] * 85

for i in range(78, 85):
	card_status[i] = False

# Create 78 button for 78 cards
cards_button = []

for i in range(78):
	cards_button.append(Button_Card(card, card_x_list[i], card_y))

# Animation for spread cards
def spread_card_animation():
	screen.blit(draw_card_screen, draw_card_screen_rect)
	print_card(card_x_left, card_y)

	pygame.display.update()

	time.sleep(0.3)

	# Spread cards
	for i in range(1, 78):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		print_card(card_x_list[i], card_y)
		time.sleep(0.01)

		pygame.display.update()

# Button to change to conclusion screen
conclusion_button = Button_Content(shuffle_card_button_surface, 650, 300, "Giải nghĩa")

# Animation for cards when move mouse
def print_all_card():
	for i in range(78):
		if card_status[i]:
			cards_button[i].update()
			cards_button[i].animation(pygame.mouse.get_pos(), card_status, i, change)

# Check clicking for cards
def draw_card():
	for i in range(78):
		if cards_button[i].checkForInput(pygame.mouse.get_pos(), card_status, i, change) and card_status[i]:
			card_list.append(card_array[i])
			card_status[i] = False

# Function for draw card screen
def draw_card_screen_function():
	spread_card_animation()

	card_1_status = True
	card_2_status = True
	card_3_status = True
	card_4_status = True
	card_5_status = True

	conclusion_button_status = False

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				for i in card_list:
					print(i)

				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN and len(card_list) < 5:
				draw_card()

			if event.type == pygame.MOUSEBUTTONDOWN and len(card_list) >= 5 and conclusion_button_status:
				if conclusion_button.checkForInput(pygame.mouse.get_pos()):
					return True
		
		if len(card_list) == 1 and card_1_status:
			card_1_status = False

			card_1 = pygame.image.load(os.path.join('Image', 'Card', card_list[0]+'.jpg')).convert()
			card_1 = pygame.transform.scale(card_1, (116, 199.33))

		elif len(card_list) == 2 and card_2_status:
			card_2_status = False

			card_2 = pygame.image.load(os.path.join('Image', 'Card', card_list[1]+'.jpg')).convert()
			card_2 = pygame.transform.scale(card_2, (116, 199.33))

		elif len(card_list) == 3 and card_3_status:
			card_3_status = False

			card_3 = pygame.image.load(os.path.join('Image', 'Card', card_list[2]+'.jpg')).convert()
			card_3 = pygame.transform.scale(card_3, (116, 199.33))

		elif len(card_list) == 4 and card_4_status:
			card_4_status = False

			card_4 = pygame.image.load(os.path.join('Image', 'Card', card_list[3]+'.jpg')).convert()
			card_4 = pygame.transform.scale(card_4, (116, 199.33))

		elif len(card_list) == 5 and card_5_status:
			card_5_status = False
				
			card_5 = pygame.image.load(os.path.join('Image', 'Card', card_list[4]+'.jpg')).convert()
			card_5 = pygame.transform.scale(card_5, (116, 199.33))

		screen.blit(draw_card_screen, draw_card_screen_rect)

		if len(card_list) >= 1:
			screen.blit(card_1, (72, 448.6666667))

		if len(card_list) >= 2:
			screen.blit(card_2, (340, 448.6666667))

		if len(card_list) >= 3:
			screen.blit(card_3, (586, 448.6666667))

		if len(card_list) >= 4:
			screen.blit(card_4, (830.6666667, 448.6666667))

		if len(card_list) >= 5:
			screen.blit(card_5, (1092, 448.6666667))

		if len(card_list) < 5:
			print_all_card()

		if len(card_list) >= 5:
			conclusion_button.update()
			conclusion_button.changeColor(pygame.mouse.get_pos())

			conclusion_button_status = True

		pygame.display.update()

# ---------------------------------------- CONCLUSION SCREEN ----------------------------------------

# Conclusion made by AI
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="Add your OpenAI API key here",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def convert_to_VN():
	question_convert = "Convert to Vietnamese: " + question
	return chat_gpt(question_convert)

def conclusion():
    user_input = "(You are a professional Tarot card reader)\nTell me the Overall to my preoccupation: " + question + "\nCards that I draw:\n" + card_list[0] + "\n" + card_list[1] + "\n" + card_list[2] + "\n" + card_list[3] + "\n" + card_list[4]
    return chat_gpt(user_input)

# Screen
conclusion_screen = pygame.image.load(os.path.join('Image', 'conclusion_screen.png')).convert()
conclusion_screen_rect = conclusion_screen.get_rect(topleft = (0,0))

# Output text
draw_text_x = 72
draw_text_y = 240.6666667

def draw_text(text):
	# Create a text box for displaying long text
	ui_manager = pygame_gui.UIManager((1280, 720))

	text_box = pygame_gui.elements.UITextBox(html_text=text,
											relative_rect=pygame.Rect((72, 178.6666667), (1136, 420)),
											manager=ui_manager)

	UI_REFRESH_RATE = clock.tick(60)/1000

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			# Update the UI manager with events
			ui_manager.process_events(event)

		# Update the UI manager
		#ui_manager.update(pygame.time.get_ticks())
		ui_manager.update(UI_REFRESH_RATE)

		# Draw everything
		ui_manager.draw_ui(screen)

		pygame.display.update()

# Function for conclusion screen
def conclusion_screen_function():
	conclusion_status = True

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.blit(conclusion_screen, conclusion_screen_rect)

		if conclusion_status:
			conclusion_status = False
			text = conclusion()
			os.system('cls')
			print(chat_gpt("Translate to Vietnamese (Do not translate the name of cards): " + text))

		pygame.display.update()

		return draw_text(text)

# ---------------------------------------- RUN GAME ----------------------------------------

# Start screen
start_screen_function()

# Quesion screen
question = question_screen_function()

# Shuffle card screen
shuffle_card_screen_function()

# Draw card screen
draw_card_screen_function()

# Conclusion screen
question = convert_to_VN()
conclusion_screen_function()

# ---------------------------------------- THE END ----------------------------------------
