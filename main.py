import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuraciones del juego
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva Obstáculos")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Función para mostrar el mensaje en la pantalla
def show_message(message, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, WHITE)
    screen.blit(text, (x, y))

# Función principal del juego
def game():
    player_size = 50
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - 2 * player_size

    obstacle_size = 50
    obstacle_speed = 5
    obstacle_x = random.randint(0, WIDTH - obstacle_size)
    obstacle_y = 0

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 5
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += 5

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, WHITE, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_y = 0
            obstacle_x = random.randint(0, WIDTH - obstacle_size)
            score += 1

        if (
            player_x < obstacle_x + obstacle_size
            and player_x + player_size > obstacle_x
            and player_y < obstacle_y + obstacle_size
            and player_y + player_size > obstacle_y
        ):
            show_message("Game Over", 64, WIDTH // 4, HEIGHT // 2)
            pygame.display.update()
            pygame.time.delay(2000)
            return

        show_message(f"Score: {score}", 32, 10, 10)

        pygame.display.update()
        clock.tick(FPS)

# Función del menú principal
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

        screen.fill(BLACK)
        show_message("Esquiva Obstáculos", 64, WIDTH // 4, HEIGHT // 4)
        show_message("Presiona Enter para comenzar", 32, WIDTH // 4, HEIGHT // 2)

        pygame.display.update()
        clock.tick(FPS)

# Ejecutar el menú principal
main_menu()
