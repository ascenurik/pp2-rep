import pygame

global play_button, next_button, prev_button, music

play_button_img = pygame.image.load('play.png')
next_button_img = pygame.transform.scale(pygame.image.load('next.png'), play_button_img.get_size())
prev_button_img = pygame.transform.scale(pygame.image.load('prev.png'), play_button_img.get_size())
pause_button_img = pygame.transform.scale(pygame.image.load('pause.png'), play_button_img.get_size())

pygame.init()
SIZE = (400, 600)
screen = pygame.display.set_mode(SIZE)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('SongPad')

music = {
    1: 'Nirvana - Smells Like Teen Spirit ',
    2: 'Rick Astley - Never Gonna Give You Up',
    3: "Kungs & Cookin' On 3 Burners - This Girl",
    4: 'PSY - Gangnam Style'
}


def player(num, in_pause):
    if not in_pause:
        pygame.mixer_music.load(music[num] + '.mp3')
        pygame.mixer_music.play()
    else:
        pygame.mixer_music.unpause()


def player_status(num):
    artist_name = music[num][:music[num].find('-') - 1]
    song_name = music[num][music[num].find('-') + 2:]

    font = pygame.font.SysFont('Verdana', 20)
    song_name_result = font.render(song_name, True, (255, 255, 255))
    screen.blit(song_name_result, (10, 410))

    font = pygame.font.SysFont('Verdana', 16)
    artist_name_result = font.render(artist_name, True, (255, 255, 255))
    screen.blit(artist_name_result, (10, 433))

    try:
        album_cover = pygame.transform.scale(pygame.image.load(music[num] + '.jpg'), (300, 300))
    except FileNotFoundError:
        album_cover = pygame.transform.scale(pygame.image.load(music[num] + '.png'), (300, 300))
    screen.blit(album_cover, (50, 70))

    pygame.draw.rect(screen, (248, 164, 95), (47, 67, 303, 303), 3)


def main():
    running = True
    n_of_track = 1
    is_playing = False
    already_played = False
    paused = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    already_played = False
                    if is_playing:
                        is_playing = False
                        paused = True
                        pygame.mixer.music.pause()
                    else:
                        if not paused:
                            player(n_of_track, paused)
                        else:
                            pygame.mixer.music.unpause()
                        is_playing = True
                        paused = False
                elif next_button.collidepoint(x, y):
                    is_playing = True
                    paused = False
                    n_of_track += 1
                    while n_of_track > len(music): n_of_track -= len(music)
                    player(n_of_track, paused)
                elif prev_button.collidepoint(x, y):
                    is_playing = True
                    paused = False
                    n_of_track -= 1
                    while n_of_track < 1: n_of_track = len(music)
                    player(n_of_track, paused)

        if not is_playing and not already_played:
            screen.fill((130, 100, 75))
            play_button = screen.blit(play_button_img, (165, 500))
        else:
            if not pygame.mixer.music.get_busy():
                n_of_track += 1
                while n_of_track > len(music): n_of_track -= len(music)
                player(n_of_track, paused)
            screen.fill((130, 100, 75))
            pause_button = screen.blit(pause_button_img, (165, 500))
        next_button = screen.blit(next_button_img, (245, 500))
        prev_button = screen.blit(prev_button_img, (85, 500))
        pygame.draw.rect(screen, (248, 164, 95), (0, 0, 400, 471), 3)
        pygame.draw.rect(screen, (248, 164, 95), (0, 470, 400, 597), 3)

        if is_playing or paused: player_status(n_of_track)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()