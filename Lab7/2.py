import pygame, os

def play_music(track):
	if playlist:
		pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), playlist[track]))
		pygame.mixer.music.play()
		print(f"Playing {playlist[track]}")

def stop_music():
	pygame.mixer.music.stop()
	print(f"{playlist[current_track]} stopped")

def goto_xth_track(x):
	global current_track
	current_track = (current_track + x) % len(playlist)
	play_music(current_track)

playlist = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".mp3")]
current_track = 0

pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
#Play, stop, next, prev
keys = [pygame.K_i, pygame.K_k, pygame.K_l, pygame.K_j]
pygame.display.set_caption("Music player")

play_music(current_track)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == keys[0]:
				if pygame.mixer.music.get_busy():
					pygame.mixer.music.pause()
					print(f"{playlist[current_track]} paused")
				else:
					pygame.mixer.music.unpause()
					print(f"{playlist[current_track]} resumed")
			elif event.key == keys[1]:
				stop_music()
			elif event.key == keys[2]:
				goto_xth_track(1)
			elif event.key == keys[3]:
				goto_xth_track(-1)