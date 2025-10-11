import pygame as p


class Tooltip:
    def __init__(self, font_name: str = 'Comic Sans MS', font_size: int = 18,
                 text_color=(255, 255, 255), bg_color=(32, 32, 32, 220),
                 padding: int = 8, border_radius: int = 6):
        self.font = p.font.SysFont(font_name, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.padding = padding
        self.border_radius = border_radius

    def render(self, text: str) -> p.Surface:
        lines = text.split('\n') if text else ['']
        line_surfaces = [self.font.render(line, True, self.text_color) for line in lines]
        width = max((s.get_width() for s in line_surfaces), default=0)
        height = sum((s.get_height() for s in line_surfaces)) + max(0, (len(lines) - 1) * 2)

        surf = p.Surface((width + self.padding * 2, height + self.padding * 2), p.SRCALPHA)
        p.draw.rect(surf, self.bg_color, surf.get_rect(), border_radius=self.border_radius)

        y = self.padding
        for s in line_surfaces:
            surf.blit(s, (self.padding, y))
            y += s.get_height() + 2
        return surf

    def draw(self, screen: p.Surface, text: str, pos: tuple[int, int]):
        tooltip_surf = self.render(text)
        rect = tooltip_surf.get_rect(topleft=pos)
        sw, sh = screen.get_size()
        if rect.right > sw:
            rect.left = sw - rect.width
        if rect.bottom > sh:
            rect.top = sh - rect.height
        screen.blit(tooltip_surf, rect.topleft)
