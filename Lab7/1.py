import pygame, os, datetime

_image_library = {}
def get_image(path):
	path = os.path.join(os.path.dirname(__file__), path)
	global _image_library
	image = _image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		_image_library[path] = image
	return image

def blitRotateCenter(surf, image, topleft, angle):
	rotated_image = pygame.transform.rotate(image, -angle)
	new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

	surf.blit(rotated_image, new_rect)

def degree_of_minutes(minutes, seconds):
	minutes += 8.7 # because original image points to approximately 51.3 min.
	return 6 * minutes + 0.1 * seconds

def degree_of_seconds(seconds):
	seconds -= 9.7 # because original image points to approximately 9.7 sec.
	return 6 * seconds

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
clock = pygame.time.Clock()
pygame.display.set_caption("Clock")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255, 255, 255))
	
	screen.blit(get_image("clock.png"), (0, 0))

	now = datetime.datetime.now()
	min, sec = now.minute, now.second
	# print(min, sec)

	blitRotateCenter(screen, get_image("min_hand.png"), (0, 0), degree_of_minutes(min, sec))
	blitRotateCenter(screen, get_image("sec_hand.png"), (0, 0), degree_of_seconds(sec))
	
	pygame.display.flip()
	clock.tick(60)