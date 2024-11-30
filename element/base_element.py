from typing import *
from SupportTypes import *
from typing import *
from rect import *
from abc import ABC

# TODO : 프젝 구조 뜯어 고치기 함



class Element(ABC):
    def __init__(self, elementId: str, isVisible: bool = True) -> None:
        self.id: str = elementId
        self.rect: Rect
        self.isVisible = isVisible

    
    def draw(self, surface: pygame.Surface): 
        '''
        UI 객체를 그릴때 scene 에서 호출하는 함수
        오버라이딩 필수
        '''
        if not self.isVisible: return