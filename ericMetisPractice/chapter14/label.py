import pygame.font;

class Label():

    def __init__(self, ai_settings, screen, caption, top):

        self.screen = screen;
        self.screen_rect = screen.get_rect();

        self.text_color = (0, 255, 0);
        self.around_color = (0 , 0 , 0, 255);
        self.font = pygame.font.SysFont(None, 48);

        self.right = self.screen_rect.right;
        self.top = top;
        self.prep_msg(caption);

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color
                , self.around_color);
        self.rect = self.msg_image.get_rect();
        self.rect.right = self.right;
        self.rect.top = self.top;

    def draw(self):
        self.screen.blit(self.msg_image, self.rect);
