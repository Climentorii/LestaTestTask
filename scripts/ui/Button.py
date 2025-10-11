import pygame as p
import sys

p.init()
screen = p.display.set_mode((800, 600))
clock = p.time.Clock()

class Button:
    def __init__(self, x: int, y: int, imageLink: str, 
                 image_hovered_link: str, 
                 image_clicked_link: str,
                 image_disabled_link: str = None):
        self.x = x
        self.y = y
        self.images = {
            'normal': p.transform.scale(p.image.load(imageLink).convert_alpha(), (256, 64)),
            'hovered': p.transform.scale(p.image.load(image_hovered_link).convert_alpha(), (256, 64)),
            'clicked': p.transform.scale(p.image.load(image_clicked_link).convert_alpha(), (256, 64)),
            'disabled': p.transform.scale(p.image.load(image_disabled_link).convert_alpha(), (256, 64)) if image_disabled_link 
                      else self.create_disabled_image(imageLink)
        }
        
        self.rect = self.images['normal'].get_rect(topleft=(self.x, self.y))
        self.state = 'normal'
        self.is_enabled = True

    def create_disabled_image(self, imageLink):
        image = p.transform.scale(p.image.load(imageLink).convert_alpha(), (256, 64))
        disabled_surface = p.Surface(image.get_size(), p.SRCALPHA)
        image_copy = image.copy()
        image_copy.set_alpha(128)
        disabled_surface.blit(image_copy, (0, 0))
        return disabled_surface

    def handle_event(self, event):
        if not self.is_enabled:
            return False
            
        if event.type == p.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                if self.state != 'clicked':
                    self.state = 'hovered'
            else:
                self.state = 'normal'
                
        elif event.type == p.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.state = 'clicked'
                return True
                
        elif event.type == p.MOUSEBUTTONUP:
            if event.button == 1 and self.state == 'clicked':
                self.state = 'hovered' if self.rect.collidepoint(event.pos) else 'normal'
                
        return False

    def draw(self, surface: p.Surface):
        if not self.is_enabled:
            surface.blit(self.images['disabled'], (self.x, self.y))
        else:
            surface.blit(self.images[self.state], (self.x, self.y))

    def disable(self):
        self.is_enabled = False
        self.state = 'disabled'

    def enable(self):
        self.is_enabled = True
        self.state = 'normal'