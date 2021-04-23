import pygame
import random

WIDTH = 1000
HEIGHT = 500
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Bubble Sort Visualiser')
fps = 100

# number of collumn
collumns = 50
colWidth = WIDTH / collumns

array = []
for i in range(collumns):
	array.append(random.randint(1, HEIGHT + 1))

rects = []
colors = []
listrect = []
listcolor = []

for i in range(collumns):
	rects.append(pygame.Rect(colWidth * i, HEIGHT + 1 - array[i], colWidth - 1, array[i]))
	colors.append((255, 255, 255))

listrect.append(rects)
listcolor.append(colors)

pygame.init()

clock = pygame.time.Clock()
running = True

def bubblesort(array, listrect, listcolor):
	count = 0
	for i in range(len(array) - 1):
		rects = []
		colors = []
		for j in range(len(array) - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				for k in range(collumns):
					rects.append(pygame.Rect(colWidth * k, HEIGHT + 1 - array[k], colWidth - 1, array[k]))
					if k == j or k == j + 1:
						colors.append((255, 0, 0))
					elif k > len(array) - 1 - count and k < len(array) + count:
						colors.append((0, 255, 0))
					else:
						colors.append((255, 255, 255))
				listrect.append(rects)
				listcolor.append(colors)
			rects = []
			colors = []
			for k in range(collumns):
				rects.append(pygame.Rect(colWidth * k, HEIGHT + 1 - array[k], colWidth - 1, array[k]))
				if k == j or k == j + 1:
					colors.append((255, 0, 0))
				elif k > len(array) - 1 - count and k < len(array) + count:
					colors.append((0, 255, 0))
				else:
					colors.append((255, 255 ,255))
			listrect.append(rects)
			listcolor.append(colors)
		count += 1
	rects = []
	colors = []
	for i in range(collumns):
		rects.append(pygame.Rect(colWidth * i, HEIGHT + 1 - array[i], colWidth - 1, array[i]))
		colors.append((0, 255, 0))
	listrect.append(rects)
	listcolor.append(colors)

bubblesort(array, listrect, listcolor)

count = 0

def draw(index, listrect, listcolor):
	screen.fill((0, 0, 0))
	for i in range(collumns):
		pygame.draw.rect(screen, listcolor[index][i], listrect[index][i])

while running:
	if count == len(listrect):
		count = len(listrect) - 1
		print('done')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				running = False
	draw(count, listrect, listcolor)
	count += 1
	clock.tick(fps)
	pygame.display.update()
	
pygame.quit()