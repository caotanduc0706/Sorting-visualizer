"""
Created 16/02/2021
Developed by Cao Tan Duc
"""

import pygame, sys
import random

running = True

number = 200
length = 1000 / number
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Sorting visualization')

pygame.init()

clock = pygame.time.Clock()

def draw_text(text, color, x, y, size):
	font = pygame.font.SysFont('Comic San MS', size)
	textbox = font.render(text, True, color)
	textrect = textbox.get_rect(topleft = (x, y))
	screen.blit(textbox, textrect)

def draw_listofarray(listofarray, index):
	for i in range(number):
		pygame.draw.rect(screen, (255, 255, 255), listofarray[index][i])

def InsertionSort(listofarray, array):
	for i in range(1, len(array)):
		temp = array[i]
		j = i
		rects = []
		while (j > 0 and array[j - 1] > temp):
			array[j] = array[j - 1]
			for k in range(number):
				rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
			listofarray.append(rects)
			j -= 1
		array[j] = temp
		rects = []
		for k in range(number):
			rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
		listofarray.append(rects)

def BubbleSort(listofarray, array):
	for i in range(len(array) - 1):
		for j in range(0, len(array) - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				rects = []
				for k in range(number):
					rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
				listofarray.append(rects)


def partition(a, start, end, listofarray, array):
	pivotIndex = start
	pivotValue = a[end]
	for i in range(start, end):
		if a[i] < pivotValue:
			a[i], a[pivotIndex] = a[pivotIndex], a[i]
			rects = []
			for k in range(number):
				rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
			listofarray.append(rects)
			pivotIndex += 1
	a[pivotIndex], a[end] = a[end], a[pivotIndex]
	rects = []
	for k in range(number):
		rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
	listofarray.append(rects)
	return pivotIndex

def QuickSort(a, start, end, listofarray, array):
	if start >= end:
		return
	index = partition(a, start, end, listofarray, array)
	# rects = []
	# for k in range(number):
	# 	rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
	# listofarray.append(rects)
	QuickSort(a, start, index - 1, listofarray, array)
	# rects = []
	# for k in range(number):
	# 	rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
	# listofarray.append(rects)
	QuickSort(a, index + 1, end, listofarray, array)
	rects = []
	for k in range(number):
		rects.append(pygame.Rect(length * k, 500 - array[k], length - 1, array[k]))
	listofarray.append(rects)


def BUBBLESORT(frame = 100):
	array = []
	for i in range(number):
		array.append(random.randint(0, 501))
		
	rects = []
	for i in range(number):
		rects.append(pygame.Rect(length * i, 500 - array[i], length - 1, array[i]))

	listofarray = []
	listofarray.append(rects)
	BubbleSort(listofarray, array)

	running = True
	i = 0
	while running:
		if i >= len(listofarray):
			i = len(listofarray) - 1
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
					running = False
		screen.fill((0, 0, 0))
		draw_listofarray(listofarray, i)
		draw_text('The comparation NO. ' + str(i), (255, 255, 255), 10, 520, 100)
		i += 1
		if i >= len(listofarray):
			draw_text('Done', (255, 0, 255), 20, 100, 200)
			draw_text('Press esc to back menu', (255, 0, 0), 20, 50, 100)
		
		pygame.display.update()
		clock.tick(frame)

def INSERTIONSORT(frame = 100):
	array = []
	for i in range(number):
		array.append(random.randint(0, 501))
		
	rects = []
	for i in range(number):
		rects.append(pygame.Rect(length * i, 500 - array[i], length - 1, array[i]))

	listofarray = []
	listofarray.append(rects)
	InsertionSort(listofarray, array)

	running = True
	i = 0
	while running:
		if i >= len(listofarray):
			i = len(listofarray) - 1
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
					running = False
		screen.fill((0, 0, 0))
		draw_listofarray(listofarray, i)
		draw_text('The comparation NO. ' + str(i), (255, 255, 255), 10, 520, 100)
		i += 1
		if i >= len(listofarray):
			draw_text('Done', (255, 0, 255), 20, 100, 200)
			draw_text('Press esc to back menu', (255, 0, 0), 20, 50, 100)
		pygame.display.update()
		clock.tick(frame)

def QUICKSORT(frame = 100):
	array = []
	for i in range(number):
		array.append(random.randint(0, 501))
	rects = []
	for i in range(number):
		rects.append(pygame.Rect(length * i, 500 - array[i], length - 1, array[i]))

	listofarray = []
	listofarray.append(rects)
	QuickSort(array, 0, len(array) - 1, listofarray, array)

	running = True
	i = 0
	while running:
		if i >= len(listofarray):
			i = len(listofarray) - 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
					running = False
		screen.fill((0, 0, 0))
		draw_listofarray(listofarray, i)
		draw_text('The comparation NO. ' + str(i), (255, 255, 255), 10, 520, 100)
		i += 1
		i += 1
		if i >= len(listofarray):
			draw_text('Done', (255, 0, 255), 20, 100, 200)
			draw_text('Press esc to back menu', (255, 0, 0), 20, 50, 100)
		pygame.display.update()
		clock.tick(frame)


def main_menu():
	running = True
	nameofsort = ''
	font = pygame.font.SysFont('Comic San MS', 100)
	click = False
	boxclick = False
	color_box = (255 ,255, 255)
	color_box_fps = (255, 255, 255)
	boxtext = pygame.Rect(20, 300, 960, 80)
	fpsbox = pygame.Rect(280, 400, 700, 80)
	fpsboxclick = False
	fps = ''
	clearbox = pygame.Rect(20, 500, 230, 80)
	blackbox = pygame.Rect(20, 500, 960, 80)
	while running:
		click = False
		mouse = pygame.mouse.get_pos()
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (255, 255, 255), clearbox)
		draw_text('CLEAR', (0, 0, 0), 30, 515, 90)
		draw_text('Default Speed = 100', (255, 255, 255), 300, 510, 100)

		newrectoftext = font.render(nameofsort, True, (255 ,255, 255))
		if boxclick:
			color_box = (255 ,255, 0)
		if fpsboxclick:
			color_box_fps = (255, 255, 0)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if newrectoftext.get_width() + 20 <= 960:
					if event.key != pygame.K_RETURN:
						if boxclick:
							if event.key == pygame.K_SPACE:
								nameofsort += ' '
							elif event.key == pygame.K_BACKSPACE and len(nameofsort) != 0:
								lis = list(nameofsort)
								lis.pop()
								nameofsort = ''.join(lis)
							else:
								nameofsort += str(chr(event.key))
						if fpsboxclick and len(fps) <= 17:
							if event.key == pygame.K_BACKSPACE and len(fps) != 0:
								lis = list(fps)
								lis.pop()
								fps = ''.join(lis)
							if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
								fps += str(chr(event.key))

					else:
						if nameofsort.lower() == 'bubble sort':
							if len(fps) == 0:
								BUBBLESORT()
							else:
								BUBBLESORT(int(fps))

						if nameofsort.lower() == 'insertion sort':
							if len(fps) == 0:
								INSERTIONSORT()
							else:
								INSERTIONSORT(int(fps))

						if nameofsort.lower() == 'quick sort':
							if len(fps) == 0:
								QUICKSORT()
							else:
								QUICKSORT(int(fps))

						else:
							pygame.time.wait(500)
							pygame.draw.rect(screen, (0, 0, 0), blackbox)
							draw_text("Don't have that algorithms!!", (255, 0, 255), 20, 500, 100)

				else:
					if event.key == pygame.K_BACKSPACE:
						lis = list(nameofsort)
						lis.pop()
						nameofsort = ''.join(lis)
					if event.key == pygame.K_RETURN:
						if nameofsort.lower() == 'bubble sort':
							if len(fps) == 0:
								BUBBLESORT()
							else:
								BUBBLESORT(int(fps))
						if nameofsort.lower() == 'insertion sort':
							if len(fps) == 0:
								INSERTIONSORT()
							else:
								INSERTIONSORT(int(fps))
						if nameofsort.lower() == 'quick sort':
							if len(fps) == 0:
								QUICKSORT()
							else:
								QUICKSORT(int(fps))
						else:
							draw_text("Don't have that algorithms!!", (255, 0, 255), 20, 500, 100)
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				click = True
		draw_text('Enter the name of the sort ', (128, 128, 128), 10, 10, 100)
		draw_text('algorithms', (128, 128, 128), 10, 70, 100)
		draw_text('want to see visualization', (128, 128, 128), 10, 130, 100)
		draw_text('at the box below', (128, 128, 128), 10, 190, 100)
		newrectoftext = font.render(nameofsort, True, (255, 255, 255))
		# newrectoffps = font.render(fps, True, (255, 255, 255))

		draw_text(nameofsort, (255 ,255, 255), 30, 310, 100)
		draw_text('Speed: ', (255, 255, 255), 20, 410, 100)
		draw_text(fps, (255, 255, 255), 290, 410, 100)
		if click and boxtext.collidepoint(mouse[0], mouse[1]):
			boxclick = True
		if click and fpsbox.collidepoint(mouse[0], mouse[1]):
			fpsboxclick = True
		if click and boxtext.collidepoint(mouse[0], mouse[1]) == False:
			boxclick = False
			color_box = (255, 255, 255)
		if click and fpsbox.collidepoint(mouse[0], mouse[1]) == False:
			fpsboxclick = False
			color_box_fps = (255, 255, 255)
		if click and clearbox.collidepoint(mouse[0], mouse[1]):
			nameofsort = ''
			fps = ''


		pygame.draw.rect(screen, color_box, boxtext, 2)
		pygame.draw.rect(screen, color_box_fps, fpsbox, 2)

		clock.tick(100)
		pygame.display.update()

main_menu()

pygame.quit()