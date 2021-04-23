'''
Created 19/02/2021
Developed by Cao Tan Duc
'''

import pygame
import random

WIDTH = 1000
HEIGHT = 600

collumns = 100
colWidth = WIDTH / collumns

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting Visualization')

pygame.init()

def draw_text(text, color, x, y, fontSize):
	font = pygame.font.SysFont('Comic San MS', fontSize)
	textbox = font.render(text, 1, color)
	rect = textbox.get_rect(topleft = (x, y))
	screen.blit(textbox, rect)

def drawCollumns(index, listRects):
	for i in range(collumns):
		pygame.draw.rect(screen, (255, 255, 255), listRects[index][i])

def createNewRects(array):
	rects = []
	for i in range(collumns):
		rects.append(pygame.Rect(colWidth * i, 500 - array[i], colWidth - 1, array[i]))
	return rects

def BubbleSort(array, listRects):
	for i in range(len(array) - 1):
		for j in range(len(array) - 1 - i):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				listRects.append(createNewRects(array))
			else:
				listRects.append(createNewRects(array))

def InsertionSort(array, listRects):
	for i in range(1, len(array)):
		temp = array[i]
		j = i
		while j > 0 and array[j - 1] > temp:
			array[j] = array[j - 1]
			j -= 1
			listRects.append(createNewRects(array))
		listRects.append(createNewRects(array))
		array[j] = temp
		listRects.append(createNewRects(array))

def CycleSort(array, listRects):
	for cycleStart in range(0, len(array) - 1):
		item = array[cycleStart]
		pos = cycleStart
		for i in range(cycleStart + 1, len(array)):
			if array[i] < item:
				pos += 1
				listRects.append(createNewRects(array))
		if pos == cycleStart:
			continue
		while item == array[pos]:
			pos += 1
		array[pos], item = item, array[pos]
		listRects.append(createNewRects(array))
		while pos != cycleStart:
			pos = cycleStart
			for i in range(cycleStart + 1, len(array)):
				if array[i] < item:
					pos += 1
					listRects.append(createNewRects(array))
			while item == array[pos]:
				pos += 1
			array[pos], item = item, array[pos]
			listRects.append(createNewRects(array))

def SelectionSort(array, listRects):
	for i in range(len(array)):
		min_idx = i
		listRects.append(createNewRects(array))
		for j in range(i + 1, len(array)):
			if array[min_idx] > array[j]:
				min_idx = j
				listRects.append(createNewRects(array))
			else:
				listRects.append(createNewRects(array))
		array[i], array[min_idx] = array[min_idx], array[i]	
		listRects.append(createNewRects(array))

def CocktailSort(array, listRects):
	n = len(array)
	swapped = True
	start = 0
	end = n - 1
	while swapped == True:
		swapped = False
		for i in range(start, end):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True
				listRects.append(createNewRects(array))
			else:
				listRects.append(createNewRects(array))
		if swapped == False:
			break
		swapped = False
		end -= 1
		for i in range(end - 1, start - 1, -1):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True
				listRects.append(createNewRects(array))
			else:
				listRects.append(createNewRects(array))
		start += 1

def SORTONSQARE(SORTALGORITHMS, frame = 100):
	array = [random.randint(1, 500) for x in range(collumns)]
	listRects = []
	listRects.append(createNewRects(array))
	SORTALGORITHMS(array, listRects)
	clock = pygame.time.Clock()
	running = True
	i = 0
	while running:
		clock.tick(frame)
		if i == len(listRects):
			i = len(listRects) - 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					running = False
		screen.fill((0, 0, 0))
		drawCollumns(i, listRects)
		draw_text('The comparation NO. ' + str(i), (255, 255, 255), 10, 520, 100)
		i += 1
		if i >= len(listRects):
			draw_text('Done', (255, 0, 255), 20, 100, 200)
			draw_text('Press esc to back menu', (255, 0, 0), 20, 50, 100)

		pygame.display.update()

def partition(array, start, end, listRects):
	pivotIndex = start
	pivotValue = array[end]
	for i in range(start, end):
		if array[i] < pivotValue:
			array[i], array[pivotIndex] = array[pivotIndex], array[i]
			listRects.append(createNewRects(array))
			pivotIndex += 1
		else:
			listRects.append(createNewRects(array))
	array[end], array[pivotIndex] = array[pivotIndex], array[end]
	listRects.append(createNewRects(array))
	return pivotIndex

def QuickSort(array, start, end, listRects):
	if start >= end:
		return
	index = partition(array, start, end, listRects)
	QuickSort(array, start, index - 1, listRects)
	listRects.append(createNewRects(array))
	QuickSort(array, index + 1, end, listRects)
	listRects.append(createNewRects(array))

def QUICKSORT(frame = 100):
	array = [random.randint(1, 500) for x in range(collumns)]
	listRects = []
	listRects.append(createNewRects(array))
	QuickSort(array, 0, len(array) - 1, listRects)
	clock = pygame.time.Clock()
	running = True
	i = 0
	while running:
		clock.tick(frame)
		if i == len(listRects):
			i = len(listRects) - 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					running = False
		screen.fill((0, 0, 0))
		drawCollumns(i, listRects)
		draw_text('The comparation NO. ' + str(i), (255, 255, 255), 10, 520, 100)
		i += 1
		if i >= len(listRects):
			draw_text('Done', (255, 0, 255), 20, 100, 200)
			draw_text('Press esc to back menu', (255, 0, 0), 20, 50, 100)

		pygame.display.update()


def main():
	running = True
	clock = pygame.time.Clock()
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
								SORTONSQARE(BubbleSort)
							else:
								SORTONSQARE(BubbleSort, int(fps))

						if nameofsort.lower() == 'insertion sort':
							if len(fps) == 0:
								SORTONSQARE(InsertionSort)
							else:
								SORTONSQARE(InsertionSort, int(fps))

						if nameofsort.lower() == 'quick sort':
							if len(fps) == 0:
								QUICKSORT()
							else:
								QUICKSORT(int(fps))
						if nameofsort.lower() == 'cycle sort':
							if len(fps) == 0:
								SORTONSQARE(CycleSort)
							else:
								SORTONSQARE(CycleSort, int(fps))
						if nameofsort.lower() == 'selection sort':
							if len(fps) == 0:
								SORTONSQARE(SelectionSort)
							else:
								SORTONSQARE(SelectionSort, int(fps))
						if nameofsort.lower() == 'cocktail sort':
							if len(fps) == 0:
								SORTONSQARE(CocktailSort)
							else:
								SORTONSQARE(CocktailSort, int(fps))

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
								SORTONSQARE(BubbleSort())
							else:
								SORTONSQARE(BubbleSort, int(fps))
						if nameofsort.lower() == 'insertion sort':
							if len(fps) == 0:
								SORTONSQARE(InsertionSort)
							else:
								SORTONSQARE(InsertionSort, int(fps))
						if nameofsort.lower() == 'quick sort':
							if len(fps) == 0:
								QUICKSORT()
							else:
								QUICKSORT(int(fps))
						if nameofsort.lower() == 'cycle sort':
							if len(fps) == 0:
								SORTONSQARE(CycleSort)
							else:
								SORTONSQARE(CycleSort, int(fps))
						if nameofsort.lower() == 'selection sort':
							if len(fps) == 0:
								SORTONSQARE(SelectionSort)
							else:
								SORTONSQARE(SelectionSort, int(fps))
						if nameofsort.lower() == 'cocktail sort':
							if len(fps) == 0:
								SORTONSQARE(CocktailSort)
							else:
								SORTONSQARE(CocktailSort, int(fps))
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

if __name__ == '__main__':
	main()