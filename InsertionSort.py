import pygame
import random

WIDTH = 1000
HEIGHT = 500
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Insertion Sort Visualiser')
fps = 100
clock = pygame.time.Clock()
running = True

# number of collumn
collumns = 100
colWidth = WIDTH / collumns

# create array of number
array = [random.randint(1, HEIGHT) for x in range(collumns)] 

# create rects array and colors array
rects = []
colors = [(255, 255, 255) for x in range(collumns)]
for i in range(collumns):
	rects.append(pygame.Rect(colWidth * i, HEIGHT - array[i], colWidth - 1, array[i]))

# create a list of frame happen
listRects = []
listColors = []
listRects.append(rects)
listColors.append(colors)

def createNewRects(array):
	rects = []
	for i in range(collumns):
		rects.append(pygame.Rect(colWidth * i, HEIGHT - array[i], colWidth - 1, array[i]))
	return rects

def BubbleSort(array):
	global rects, colors, listRects, listColors
	for i in range(0, len(array) - 1):
		for j in range(0, len(array) - 1 - i):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				colors[j], colors[j + 1] = (255, 0, 0), (255, 0, 0)
				listRects.append(createNewRects(array))
				listColors.append(colors)
				colors[j], colors[j + 1] = (255, 255 ,255), (255 ,255 ,255)

def InsertionSort(array):
	global rects, colors, listRects, listColors
	for i in range(1, len(array)):
		temp = array[i]
		j = i
		# listRects.append(createNewRects(array))
		while j > 0 and array[j - 1] < temp:
			array[j] = array[j - 1]
			j -= 1
			listRects.append(createNewRects(array))
			# listColors.append(colors)
		array[j] = temp


def drawFrameHappen(index, surFace, listRects, listColors):
	surFace.fill((0, 0, 0))
	for i in range(collumns):
		pygame.draw.rect(surFace, (255, 255 ,255), listRects[index][i])

BubbleSort(array)

pygame.init()
count = 0

while running:
	screen.fill((0, 0, 0))
	if count == len(listRects):
		count = len(listRects) - 1
		print('done')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				running = False
	drawFrameHappen(count, screen, listRects, listColors)
	count += 1
	pygame.display.update()
	clock.tick(fps)

pygame.quit()