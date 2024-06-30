
import pygame
from flappybird import WINDOW_HEIGHT, WINDOW_WIDTH, draw_screen
from models.bird import Bird
from models.floor import Floor
from models.pipe import Pipe


def main():
    birds = [Bird(x=230, y=350)]
    pipes = [Pipe(x=700)]
    floor = Floor(y=730)
    screen_main = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    points = 0
    timer = pygame.time.Clock()

    running = True
    while running:
        timer.tick(30)

    #interação com usuario
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if game_event.type == pygame.KEYDOWN:
                if game_event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()



    #mover objetos
        for bird in birds:
            bird.move()

        floor.move()

        add_pipe = False
        remove_pipe = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird=birds):
                    birds.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed =  True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.top_pipe_image.get_width() < 0:
                remove_pipe.append(pipe)

        if add_pipe:
            points+=1
            pipes.append(Pipe(x=600)) #provavel bug
        for pipe in remove_pipe:
            pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > floor.y or bird.y < 0:
                birds.pop(i)


        draw_screen(screen=screen_main,
                    birds=birds,
                    floor=floor,
                    pipes=pipes,
                    points=points)
        
        
        
if __name__ == '__main__':
    main()

