import pygame



class Paddle:

    def __init__(self, X, Y, A, B):
        self.posX = X
        self.posY = Y
        self.height = A
        self.width = B




    # def moveUp(self):
    #     self.posY -= 10
    #
    # def moveDown(self):
    #     self.posY += 8

    def collides(self, ball):
        return ball.posX + 2*ball.radius >= self.posX and ball.posX + 2*ball.radius <= self.posX + self.width and \
               ball.posY - ball.radius >= self.posY and ball.posY - ball.radius <= self.posY + self.height or\
               ball.posX + 2*ball.radius >= self.posX and ball.posX + 2*ball.radius <= self.posX + self.width and \
               ball.posY + ball.radius >= self.posY and ball.posY + ball.radius <= self.posY + self.height or\
               ball.posX >= self.posX and ball.posX <= self.posX + self.width and \
               ball.posY - ball.radius >= self.posY and ball.posY - ball.radius <= self.posY + self.height or \
               ball.posX  >= self.posX and ball.posX <= self.posX + self.width and \
               ball.posY + ball.radius >= self.posY and ball.posY + ball.radius <= self.posY + self.height




    def render(self ,screen):
        pygame.draw.line(screen, pygame.Color("green"), [self.posX, self.posY],
                         [self.posX, self.posY +self.height], self.width)


class Ball:
    def __init__(self, X, Y, R):
        self.posX = X
        self.posY = Y
        self.radius = R
        self.speed = 0
        # self.color = (255, 0, 0)
        self.img = pygame.image.load("flappy bird.png").convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, 0.2)

    def update(self):
        self.posY -= self.speed
        self.speed -= 1

    def render(self, screen):
        #Image
        w, h = self.img.get_rect().size
        screen.blit(self.img, (self.posX - w / 2, self.posY - h / 2))


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.ball = None
        self.point = 0


    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):

        self.screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("flappy-bird")

        self.clock = pygame.time.Clock()

        self.running = True
        self.line = Paddle(500,40,1,1000)
        self.upperPaddle1 = Paddle(450,40,260,50)
        self.lowerPaddle1 = Paddle(450,450,400,50)
        self.upperPaddle2 = Paddle(650,40,60,50)
        self.lowerPaddle2 = Paddle(650,250,300,50)
        self.upperPaddle3 = Paddle(875,40,100,50)
        self.lowerPaddle3 = Paddle(875,300,350,50)
        self.upperPaddle4 = Paddle(220,40,110,50)
        self.lowerPaddle4 = Paddle(220,300,550,50)
        self.ball = Ball(80, 250, 20)

    def update(self):
        self.events()
        if self.ball.posX == self.lowerPaddle1.posX or self.ball.posX == self.lowerPaddle2.posX or self.ball.posX == self.lowerPaddle3.posX or self.ball.posX == self.lowerPaddle4 .posX:
            self.point += 1

        if self.ball.posY - self.ball.radius <= 40 or self.ball.posY + self.ball.radius >= 500:
            self.running = False

        if self.upperPaddle1.collides(self.ball) or self.lowerPaddle1.collides(self.ball) or self.upperPaddle2.collides(self.ball) or\
                self.lowerPaddle2.collides(self.ball)or self.lowerPaddle3.collides(self.ball) or self.upperPaddle3.collides(self.ball) or  self.lowerPaddle4.collides(self.ball) or self.upperPaddle4.collides(self.ball):
            self.running = False


        if self.ball.posX - self.ball.radius <= 0 or self.ball.posX + self.ball.radius >= 1000 :
            self.running = False
        self.ball.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
               self.ball.speed = 10
        self.ball.posX += 1


    def render(self):
        self.screen.fill((0, 0, 0))
        self.ball.render(self.screen)
        self.line.render(self.screen)
        self.upperPaddle1.render(self.screen)
        self.lowerPaddle1.render(self.screen)
        self.upperPaddle2.render(self.screen)
        self.lowerPaddle2.render(self.screen)
        self.upperPaddle3.render(self.screen)
        self.lowerPaddle3.render(self.screen)
        self.upperPaddle4.render(self.screen)
        self.lowerPaddle4.render(self.screen)
        self.drawText('Flappy-bird',50,5,"red")
        self.drawText('Score: '+str(self.point) ,860,5,"yellow")
        pygame.display.flip()
        self.clock.tick(60)

    def drawText(self,text,X,Y,color):
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 20)

        # Text
        self.screen.blit(
            font.render(text, False, pygame.Color(color))
            , (X, Y))


    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()