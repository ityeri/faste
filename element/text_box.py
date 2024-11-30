import pygame
from element import *
from value import *
from SupportTypes import *
from element import Element
from rect import *



class AlignType:
    TOP_LEFT: int = 0
    TOP_RIGHT: int = 1
    BOTTOM_LEFT: int = 2
    BOTTOM_RIGHT: int = 3

    TOP_CENTER: int = 4
    BOTTOM_CENTER: int = 5
    LEFT_CENTER: int = 6
    RIGHT_CENTER: int = 7

    CENTER: int = 8

    def toRectType(alignType: int):
        if alignType == 8: return 9
        return alignType


class TextBox(Element):
    def __init__(self, 
                 elementId: str,
                 text: str,
                 font: pygame.Font,
                 pos: SupportPosValue,
                 color: ColorValue,
                 bgcolor: ColorValue | None = None,
                 alignType: int = AlignType.TOP_LEFT,
                 antiAlias: bool = True,
                 isVisible: bool = False):

        super().__init__(elementId, isVisible)

        self.text: str = text
        self.font: pygame.Font = font
        
        self.color: ColorValue = color
        self.bgcolor: ColorValue = bgcolor
        
        self.alignType: int = alignType
        self.antiAlias: bool = antiAlias
        
        self.surface: pygame.Surface
        
        self.x: rv
        self.y: rv

        if isinstance(pos[0], Number): self.x = lambda: pos[0]
        elif type(pos[0]) == rv: self.x = pos[0]
        if isinstance(pos[1], Number): self.y = lambda: pos[1]
        elif type(pos[1]) == rv: self.y = pos[1]

        self.setSurface()

    def setSurface(self) -> None:
        textSurfaces: list[pygame.Surface] = [
            self.font.render(text, self.antiAlias, self.color, self.bgcolor) 
            for text in self.text.split()
        ]


        globalWidth = max([textSurface.get_width() for textSurface in textSurfaces])
        globalHeight = textSurfaces[0].get_height() * len(textSurfaces)
        lineHeight = textSurfaces[0].get_height()

        self.surface = pygame.Surface((globalWidth, globalHeight))

        # 텍스트를 중앙에 놔야하는 경우
        if self.alignType == AlignType.CENTER or \
           self.alignType == AlignType.TOP_CENTER or \
           self.alignType == AlignType.BOTTOM_CENTER:

            surfaceCenterX = self.surface.get_width()/2

            for i, textSurface in enumerate(textSurfaces):
                self.surface.blit(textSurface, (surfaceCenterX-textSurface.get_width()/2, lineHeight*i))
        
        # 텍스트를 윈쪽에 놔야하는 경우
        if self.alignType == AlignType.TOP_LEFT or \
           self.alignType == AlignType.BOTTOM_LEFT or \
           self.alignType == AlignType.LEFT_CENTER:
            
            for i, textSurface in enumerate(textSurfaces):
                self.surface.blit(textSurface, (0, lineHeight*i))

        # 텍스트를 오른쪽에 놔야하는 경우
        if self.alignType == AlignType.TOP_RIGHT or \
           self.alignType == AlignType.BOTTOM_RIGHT or \
           self.alignType == AlignType.RIGHT_CENTER:
            
            for i, textSurface in enumerate(textSurfaces):
                self.surface.blit(
                    textSurface, 
                    (self.surface.get_width() - textSurface.get_width(), lineHeight*i)
                )

        self.rect = Rect(
            (self.x, self.y, globalWidth, globalHeight), 
            AlignType.toRectType(self.alignType)
        )

    def draw(self, surface):
        super().draw(surface)

        caculatedRect = self.rect.caculateRect()
        surface.blit(
            self.surface,
            (caculatedRect.left, caculatedRect.top)
        )