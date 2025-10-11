import pygame as p
from pygame import Surface, Rect
from collections import deque
from typing import Deque, Iterable, Tuple


class LogPanel:

    def __init__(
        self,
        rect: Rect,
        font: p.font.Font,
        *,
        bg_color: Tuple[int, int, int, int] = (20, 20, 20, 180),
        border_color: Tuple[int, int, int] = (200, 180, 120),
        padding: int = 12,
        capacity: int = 100,
        text_color: Tuple[int, int, int] = (255, 255, 255),
        line_gap: int = 0,
    ) -> None:
        self.rect = rect
        self.font = font
        self.bg_color = bg_color
        self.border_color = border_color
        self.padding = padding
        self.text_color = text_color
        self.line_gap = line_gap
        self._lines: Deque[str] = deque(maxlen=max(1, capacity))

    def set_rect(self, rect: Rect) -> None:
        self.rect = rect

    def clear(self) -> None:
        self._lines.clear()

    def extend(self, lines: Iterable[str]) -> None:
        for line in lines:
            self.append(line)

    def append(self, text: str) -> None:
        if text is None:
            return
        self._lines.append(str(text))

    @staticmethod
    def _truncate_to_width(text: str, max_width: int, font: p.font.Font) -> str:
        if font.size(text)[0] <= max_width:
            return text
        ellipsis = '…'
        lo, hi = 0, len(text)
        while lo < hi:
            mid = (lo + hi) // 2
            if font.size(text[:mid] + ellipsis)[0] <= max_width:
                lo = mid + 1
            else:
                hi = mid
        return text[: max(lo - 1, 0)] + ellipsis

    def render(self, screen: Surface) -> None:
        panel_surf = p.Surface((self.rect.width, self.rect.height), p.SRCALPHA)
        panel_surf.fill(self.bg_color)

        max_text_width = self.rect.width - 2 * self.padding
        line_spacing = max(1, self.font.get_linesize() + self.line_gap)
        content_height = self.rect.height - 2 * self.padding
        max_lines = max(1, content_height // line_spacing)

        lines_to_draw = list(self._lines)[-max_lines:]
        y = self.rect.height - self.padding - line_spacing * len(lines_to_draw)
        x = self.padding

        for line in lines_to_draw:
            txt = self._truncate_to_width(line, max_text_width, self.font)
            text_surface = self.font.render(txt, True, self.text_color)
            panel_surf.blit(text_surface, (x, y))
            y += line_spacing

        screen.blit(panel_surf, self.rect.topleft)
        p.draw.rect(screen, self.border_color, self.rect, 2)
