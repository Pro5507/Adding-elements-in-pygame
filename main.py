import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 1000

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')


text = pygame.font.Font(None, 45).render('Hello Everyone ', True, pygame.Color('red'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


display_surface.blit(text, text_rect)

pygame.display.flip()