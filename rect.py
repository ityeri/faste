from typing import *
from SupportTypes import *
from typing import *
from abc import *
from value import *
from numbers import Number

# TODO : 그 뭐냐 텍스크 거시미 만들기


class RectType:
    TOP_LEFT: int = 0
    TOP_RIGHT: int = 1
    BOTTOM_LEFT: int = 2
    BOTTOM_RIGHT: int = 3

    TOP_CENTER: int = 4
    BOTTOM_CENTER: int = 5
    LEFT_CENTER: int = 6
    RIGHT_CENTER: int = 7

    CENTER_RADIUS: int = 8
    CENTER_DIAMETER: int = 9

    TWO_POINT: int = 10

    pygame.Rect


class Rect():
    '''
    사각형의 형태를 정의할때 사용되는 클래수.
    참고로 이 사각형은 그리는 용도가 아니라, 형태만 존재하는 계산용 사각형임

    rect 와 rectType 를 통해 다양한 사각형의 형태로 정의 가능
    rect 를 tuple 로 입력시에, int 로 할시 절대적갑스 rv 로 입력할시 그대로 데이터에 드감
    '''
    def __init__(self, 
                 rect: SupportRectValue,
                 rectType: int = RectType.TOP_LEFT,
                 isVisible: bool = False,
                 color: ColorValue = (255, 0, 0)) -> None:
        
        self.x: rv
        self.y: rv
        self.dx: rv
        self.dy: rv

        if isinstance(rect[0], Number): self.x = lambda: rect[0]
        elif type(rect[0]) == rv: self.x = rect[0]
        if isinstance(rect[1], Number): self.y = lambda: rect[1]
        elif type(rect[1]) == rv: self.y = rect[1]
        if isinstance(rect[2], Number): self.dx = lambda: rect[2]
        elif type(rect[2]) == rv: self.dx = rect[2]
        if isinstance(rect[3], Number): self.dy = lambda: rect[3]
        elif type(rect[3]) == rv: self.dy = rect[3]
        

        self.rectType: int = rectType
        self.isVisible: bool = isVisible
        self.color: ColorValue = color
    
    def caculateRect(self) -> pygame.Rect:

        x = self.x()
        y = self.y()
        dx = self.dx()
        dy = self.dy()

        left: int
        top: int
        width: int
        height: int

        match self.rectType:
            case RectType.TOP_LEFT:
                left = x
                top = y
                width = dx
                height = dy

            case RectType.TOP_RIGHT:
                left = x - dx
                top = dy
                width = dx
                height = dy
                
            case RectType.BOTTOM_LEFT:
                left = x
                top = y - dy
                width = dx
                height = dy

            case RectType.BOTTOM_RIGHT:
                left = x - dx
                top = y - dy
                width = dx
                height = dy



            case RectType.TOP_CENTER:
                left = x - dx/2
                top = y
                width = dx
                height = dy

            case RectType.BOTTOM_CENTER:
                left = x - dx/2
                top = y - dy
                width = dx
                height = dy

            case RectType.LEFT_CENTER:
                left = x
                top = y - dy/2
                width = dx
                height = dy
            
            case RectType.RIGHT_CENTER:
                left = x - dx
                top = y - dy/2
                width = dx
                height = dy



            case RectType.CENTER_RADIUS:
                left = x - dx
                top = y - dy
                width = dx*2
                height = dy*2

            case RectType.CENTER_DIAMETER:
                left = x - dx/2
                top = y - dy/2
                width = dx
                height = dy

            

            case RectType.TWO_POINT:
                if x < dx:
                    left = x
                    width = dx - x
                else: 
                    left = dx
                    width = x - dx

                if y < dy:
                    top = y
                    height = dy - y
                else: 
                    top = dy
                    height = y - dy



        return pygame.rect.Rect(left, top, width, height)
    
    @property
    def size(self) -> tuple[int, int]:
        return self.caculateRect().size