import pygame.gfxdraw
from element import Element
from SupportTypes import *
from rect import *
from math import *

class Rect(Element):
    def __init__(self, 
                 elementId: str, 
                 color: ColorValue,
                 rect: SupportRectValue,
                 rectType: int = RectType.TOP_LEFT,
                 borderRadius: int = 0,
                 width: int = 0,
                 isVisible: bool = True):
        
        super().__init__(elementId, isVisible)

        self.rect: Rect = Rect(rect, rectType)
        self.color: ColorValue = color
        self.width: int = width
        self.borderRadius: int = borderRadius

        self.isVisible: bool = isVisible
    
    def draw(self, surface: pygame.Surface):

        super().draw(surface)

        if self.borderRadius > 0:
            # 사각형의 꼭짓점 위치를 먼저 다 가져옴
            caculatedRect = self.rect.caculateRect()
            topLeft = (caculatedRect.x, caculatedRect.y)
            topRight = (caculatedRect.x+caculatedRect.width, caculatedRect.y)
            bottomLeft = (caculatedRect.x, caculatedRect.y+caculatedRect.height)
            bottomRight = (caculatedRect.x+caculatedRect.width, 
                        caculatedRect.y+caculatedRect.height)
        
            radius = self.borderRadius

            
            if self.width == 0:
                pygame.draw.circle(surface, self.color, 
                                  (topLeft[0]+radius, topLeft[1]+radius),
                                  radius)
                pygame.draw.circle(surface, self.color,
                                   (topRight[0]-radius, topRight[1]+radius),
                                   self.borderRadius)
                pygame.draw.circle(surface, self.color,
                                   (bottomLeft[0]+radius, bottomRight[1]-radius),
                                   radius)
                pygame.draw.circle(surface, self.color,
                                   (bottomRight[0]-radius, bottomRight[1]-radius),
                                   radius)
                
                pygame.draw.rect(surface, self.color, 
                                 (topLeft[0]+radius, topLeft[1], 
                                  caculatedRect.width - radius*2, caculatedRect.height))
                pygame.draw.rect(surface, self.color, 
                                 (topLeft[0], topLeft[1]+radius,
                                  caculatedRect.width, caculatedRect.height - radius*2))
            else:
                ...


        # pygame.draw.rect(
        #     surface, self.color, self.rect.caculateRect(), self.width
        # )