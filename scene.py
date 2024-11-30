from operator import imod
import pygame
from element import Element

class Scene:
    '''
    elementOrder 에서 0 에 가까운 인덱스를 가질수록
    더 뒤에 그려짐 (for 문에서 0 부터 그림)
    '''
    def __init__(self):
        self.elements: dict[str, Element] = dict()
        self.elementOrder: list[str] = list()
    
    def addElement(self, element: Element) -> None:

        # 추가하고자 하는 요소의 ID 가 이미 딕셔너리에 있으면?
        if element.id in self.elements:
            raise NameError(f'Element Id "{element.id}" 가 이미 있습니다.')
        else: 
            self.elements[element.id] = element
            self.elementOrder.insert(0, element.id)
    
    def getElement(self, elementId: str) -> Element:
        if not elementId in self.elements:
            raise NameError(f'Element Id "{elementId}" 를 찾을수 없읍')
        else: return self.elements[elementId]
    
    def setOrder(self, elementId: str, newIndex: int):
        try: index = self.elementOrder.index(elementId)
        except ValueError: raise NameError(f'Element Id "{elementId}" 를 찾을수 없읍')

        elementId = self.elementOrder.pop(index)
        self.elementOrder.insert(newIndex, elementId)

    def setOrderBack(self, elementId: str):
        try: index = self.elementOrder.index(elementId)
        except ValueError: raise NameError(f'Element Id "{elementId}" 를 찾을수 없읍')

        elementId = self.elementOrder.pop(index)
        self.elementOrder.insert(0, elementId)

    def setOrderFront(self, elementId: str):
            try: index = self.elementOrder.index(elementId)
            except ValueError: raise NameError(f'Element Id "{elementId}" 를 찾을수 없읍')

            elementId = self.elementOrder.pop(index)
            self.elementOrder.insert(0, elementId)



    def draw(self, surface: pygame.Surface):
        for elementId in self.elementOrder:
            self.elements[elementId].draw(surface)