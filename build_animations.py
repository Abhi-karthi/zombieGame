import pygame


class Animation:
    def __init__(self, right_images, left_images):
        self.right_images = right_images
        self.left_images = left_images
        self.limit = len(right_images) - 1
        self.animation_number = 0

    def get_image(self, face: str):
        if self.animation_number == self.limit:
            self.animation_number = 0
        else:
            self.animation_number += 1

        if face == "left":
            return self.left_images[self.animation_number - 1]
        elif face == "right":
            return self.right_images[self.animation_number - 1]

        raise IOError("Face must equal 'right' or 'left'")


def load_images(name: str, number_of_items: int, size: tuple[int, int], is_player: bool = False) -> list:
    output_left = []
    output_right = []
    for i in range(number_of_items):
        if is_player:
            image = pygame.image.load(f"Assets/player/{name}00{number_of_items}.png")
        else:
            image = pygame.image.load(f"Assets/zombie/{name} ({i + 1}).png")
        image = pygame.transform.scale(image, (int(size[0]/4), int(size[1]/4)))
        output_left.append(image)
        image = pygame.transform.flip(image, True, False)
        output_right.append(image)
    return [output_right, output_left]


zombie_attack_right = load_images("Attack", 8, (430, 519))[0]
zombie_attack_left = load_images("Attack", 8, (430, 519))[1]

zombie_dead_right = load_images("Dead", 12, (629, 526))[0]
zombie_dead_left = load_images("Dead", 12, (629, 526))[1]

zombie_walking_right = load_images("Walk", 10, (430, 519))[0]
zombie_walking_left = load_images("Walk", 10, (430, 519))[1]

player_attack_right = load_images("Attack__", 9, (536, 495), True)[0]
player_attack_left = load_images("Attack__", 9, (536, 495), True)[1]

player_dead_right = load_images("Dead__", 9, (482, 498), True)[0]
player_dead_left = load_images("Dead__", 9, (482, 498), True)[1]

player_run_right = load_images("Run__", 7, (363, 458), True)[0]
player_run_left = load_images("Run__", 7, (363, 458), True)[1]

player_idle_right = load_images("Idle__", 9, (232, 439), True)[0]
player_idle_left = load_images("Idle__", 9, (232, 439), True)[1]

player_jump_right = load_images("Jump__", 9, (362, 483), True)[0]
player_jump_left = load_images("Jump__", 9, (362, 483), True)[1]

player_jump_attack_right = load_images("Jump_Attack__", 9, (504, 522), True)[0]
player_jump_attack_left = load_images("Jump_Attack__", 9, (504, 522), True)[1]

zombie_attack_animation: Animation = Animation(zombie_attack_right, zombie_attack_left)
zombie_dead_animation: Animation = Animation(zombie_dead_right, zombie_dead_left)
zombie_walking_animation: Animation = Animation(zombie_walking_right, zombie_walking_left)
player_attack_animation: Animation = Animation(player_dead_right, player_dead_left)
player_dead_animation: Animation = Animation(player_dead_right, player_dead_left)
player_run_animation: Animation = Animation(player_run_right, player_run_left)
player_idle_animation: Animation = Animation(player_idle_right, player_idle_left)
player_jump_animation: Animation = Animation(player_jump_right, player_jump_left)
player_jump_attack_animation: Animation = Animation(player_jump_attack_right, player_jump_attack_left)
