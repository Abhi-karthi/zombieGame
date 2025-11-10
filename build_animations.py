import pygame


def load_images(name: str, number_of_items: int, is_player: bool = False) -> list[pygame.image]:
    output = []
    for i in range(number_of_items):
        if is_player:
            image = pygame.image.load(f"{name}00{number_of_items}")
        else:
            image = pygame.image.load(f"{name} ({i + 1}).png")
        image = pygame.transform.scale(image, (121, 175))
        output.append(image)
        image = pygame.transform.flip(image, True, False)
        output.append(image)
    return output


zombie_attack_right = load_images("Attack", 8)[0]
zombie_attack_left = load_images("Attack", 8)[1]

zombie_dead_right = load_images("Dead", 12)[0]
zombie_dead_left = load_images("Dead", 12)[1]

zombie_walking_right = load_images("Walk", 10)[0]
zombie_walking_left = load_images("Walk", 10)[1]

player_attack_right = load_images("Attack__", 9)[0]
player_attack_left = load_images("Attack__", 9)[1]

# player_dead_right = load_images("")
