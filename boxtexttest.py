import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))

def drawtext(text, color, x, y, size):
	font = pygame.font.Font(None, size)
	box = font.render(text, True, color)
	rect = box.get_rect(topleft = (x, y))
	screen.blit(box, rect)
name = ''
boxtext = pygame.Rect(10 + len('Enter the name of the sort: ') * 10 + 5, 10, 100, 22)

running = True

while running:
	screen.fill((0, 0, 0))
	boxtext = pygame.Rect(10 + len('Enter the name of the sort: ') * 10 + 5, 10, (len(name) + 1) * 13 - len(name) * 0.45, 22)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			# if pygame.key.name(event.key) != pygame.K_RETURN:
			# 	if pygame.key.name(event.key) == pygame.K_SPACE:
			# 		name += ' '
			# 	elif  pygame.key.name(event.key) == pygame.K_BACKSPACE:
			# 		lis = list(name)
			# 		lis.pop()
			# 		name = ''.join(lis)
			# 	else:
			# 		name += str(pygame.key.name(event.key))
			if event.key != pygame.K_RETURN:
				if event.key == pygame.K_BACKSPACE:
					lis = list(name)
					lis.pop()
					name = ''.join(lis)
				else:
					name += str(chr(event.key))

	drawtext('Enter the name of the sort: ', (255, 255, 255), 10, 10, 32)
	pygame.draw.rect(screen, (255 ,255, 255), boxtext, 2)
	drawtext(str(name), (255, 255 ,255), 10 + len('Enter the name of the sort: ') * 10 + 10, 11, 32)
	pygame.display.update()
pygame.quit()