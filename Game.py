import pygame, random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
FPS = 30


rock, paper, scissors = "Rock.png", "Paper.png", "Scissors.png" 

objects = []
objectcount = 50


class Object:
    def __init__(self, color) -> None:
        self.k = random.randrange(50, 475)
        self.pos = [self.k, random.randrange(50, 475), 25, 25]
        self.rect = pygame.Rect(self.pos)
        self.width, self.height = 500, 500
        self.xvel, self.yvel = random.choice([1, -1, 2, -2]), random.choice([1, -1, 2, -2])
        self.color = color
        self.image = pygame.image.load(self.color).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))

    def move(self):
        if self.rect.left <= 0:
            self.xvel = -self.xvel
        if self.rect.right > self.width:
            self.xvel = -self.xvel
        if self.rect.top < 0:
            self.yvel = -self.yvel
        if self.rect.bottom > self.height:
            self.yvel = -self.yvel
        self.rect.centerx += self.xvel
        self.rect.centery += self.yvel

    def create(self):
        screen.blit(self.image, self.rect)
        self.move()


for i in range(objectcount):
    color = random.choice((rock, paper, scissors))
    objects.append(Object(color))


run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("White")
    for i in range(len(objects)):
        objects[i].create()
        for j in range(len(objects)):
            if i != j:
                if objects[i].rect.colliderect(objects[j].rect):
                    if (
                        objects[i].color == rock
                        and objects[j].color == rock
                        or objects[i].color == paper
                        and objects[j].color == paper
                        or objects[i].color == scissors
                        and objects[j].color == scissors
                        ):
                        continue

                    elif objects[i].color == rock and objects[j].color == paper:
                        objects[i].color = paper
                        objects[j].color = paper
                        objects[i].image = pygame.image.load(objects[i].color).convert_alpha()
                        objects[i].image = pygame.transform.scale(objects[i].image, (30, 30))


                    elif objects[i].color == rock and objects[j].color == scissors:
                        objects[i].color = rock
                        objects[j].color = rock
                        objects[j].image = pygame.image.load(objects[j].color).convert_alpha()
                        objects[j].image = pygame.transform.scale(objects[j].image, (30, 30))

                    elif objects[i].color == paper and objects[j].color == scissors:
                        objects[i].color = scissors
                        objects[j].color = scissors
                        objects[i].image = pygame.image.load(objects[i].color).convert_alpha()
                        objects[i].image = pygame.transform.scale(objects[i].image, (30, 30))


    pygame.display.update()

pygame.quit()
