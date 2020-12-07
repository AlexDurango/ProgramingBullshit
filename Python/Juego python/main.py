import pygame

def main():
    pygame.init()

    logo = pygame.image.load("descarga.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("shitty ass robot")

    screen = pygame.display.set_mode((500,500))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()