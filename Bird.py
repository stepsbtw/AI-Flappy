class Bird:
   TIME_ANIMATION = 30
   SPRITES = [pygame.image.load(os.path.join('sprites', 'bird2.png')),
              pygame.image.load(os.path.join('sprites', 'bird1.png'))]
   def __init__(self,x,y):
      #self.score = 0
      self.x = x
      self.y = y
      self.speed = 1
      self.tick= 0
      self.tick_animation=0
      #self.height = y
      self.accel = 20.5  # constante pra o movimento/gravidade
      self.sprite = SPRITES[0]

      #self.weights = [0, 0]

   #def vision(self, xpipe, ypipe):
   # pega o x e y do ponto
   # diminui do x e y do passaro
   # chama o think

   #def think(self, xdelta, ydelta):
   # pega os deltas e decide o output

   def jump(self):
      self.tick = 0
      self.y -= self.accel # valor negativo no y, boneco vai pra cima!
      # nao ta nada suave.

   def move(self):
      # PARABOLA!
      self.tick += 1
      self.y = min((self.y + (self.tick**2)/2000 ),SCREEN_HEIGHT - self.sprite.get_height())
     
      #if self.tick < 0:
         #self.y = self.y-self.speed-(self.tick**2)/100#max((self.y - self.speed -(self.tick**2)/2000),SCREEN_HEIGHT - self.sprite.get_height())
     
      if self.y >= SCREEN_HEIGHT - self.sprite.get_height():
         # caso ele chegue no fim da tela , ele pula! (debug)
            self.jump()

   def draw(self, window):
      self.tick_animation += 1
      if self.tick_animation < self.TIME_ANIMATION:
         self.sprite = self.SPRITES[1]
      elif self.tick_animation >= self.TIME_ANIMATION * 2:
         self.tick_animation = 0
      else:
         self.sprite = self.SPRITES[0]

      if self.speed > 0:
         self.sprite = self.SPRITES[1]

      #center_pos = self.sprite.get_rect(topleft=(self.x, self.y)).center
      #rect = self.sprite.get_rect(center=center_pos)
      window.blit(self.sprite,(self.x,self.y)) #imprime o boneco na tela

   #def gravity(self):
      #self.tick -= 1
      # seria interessante diminuir o tick, pq na funcao 'move', o movimento eh baseado no tick do personagem.
      #self.y = min((self.y + self.speed), SCREEN_HEIGHT-self.sprite.get_height())

   def do_all(self,window):
      # aqui vou printar e mover o personagem.
      self.draw(window)
      self.move()
      #self.gravity()
