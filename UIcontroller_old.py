from typing import *
import pygame
from typing import *
from abc import *
# from value import RelativeType as rt
# from value import RelativeData as rd
# from value import RelativeValue as rv
from numbers import Number



class Faste:
    def __init__(self) -> None:
        pygame.init()
        self.scenes: list[pg.UIManager] = []

        self.screen: pygame.Surface = None
        self.screenSize: tuple = None
        self.clk = pygame.time.Clock()
        self.fps: int = 60
        self.dtms: int = 1
        self.dtsec: float = 0.001
        self.on = True

        self.scenes: dict[set, Scene] = {}
        self.goalSceneName: Optional[str] = None
        self.presentScene: Scene = None

    def setScreenSize(self, size: tuple[int, int]):
        self.screenSize = size
        self.screen = pygame.display.set_mode(self.screenSize, pygame.RESIZABLE)


    def setEntryScene(self, sceneName: str):
        self.presentScene = self.scenes[sceneName]

    def gotoScene(self, sceneName: str):
        self.goalSceneName = sceneName


    def addScene(self, sceneName: str, scene: 'Scene'):
        self.scenes[sceneName] = scene



    def run(self):

        while self.on:
            self.screenSize = self.screen.get_size()
            self.dtms = self.clk.tick(self.fps)
            self.dtsec = self.dtms / 1000
            
            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                self.presentScene.UImanager.process_events(event)

                if event.type == pygame.QUIT:
                    self.exit()

                self.presentScene.processEvent(event)

            self.presentScene.UImanager.update(self.dtsec)
            self.presentScene.update()
            self.presentScene.UImanager.draw_ui(self.screen)

            pygame.display.flip()

            if self.goalSceneName != None:
                self.presentScene = self.scenes[self.goalSceneName]
                self.goalSceneName = None

    
    def exit(self):
        self.on = False
        print("컨트롤러를 종료합니다...")



class Scene:
    def __init__(self, manager: Faste, 
        updateFunc:         Callable[['Scene'],                     None], 
        eventFunc: Optional[Callable[['Scene', pygame.event.Event], None]]) -> None:

        self.manager: Faste = manager
        self.UImanager: pygame_gui.UIManager = pygame_gui.UIManager(manager.screenSize)
        self.elements: dict[str, UIElement] = {}

        self.updateFunc: Callable[['Scene'], None] = updateFunc
        self.eventFunc: Optional[
            Callable[['Scene', pygame.event.Event], None]] = eventFunc


    def getUImanager(self):
        return self.UImanager


    def addElement(self, id: str, element: UIElement) -> None:
        self.elements[id] = element
    
    def getElementFromId(self, id: str) -> Optional[UIElement]:
        try:
            return self.elements[id]
        except: return None

    def getElementId(self, element: UIElement) -> Optional[str]:
        for id, element in self.elements.items():
            if element == element:
                return id
        return None


    def processEvent(self, event: pygame.event.Event) -> None:
        if self.eventFunc is not None:
            self.eventFunc(self, event)

    def update(self):
        self.updateFunc(self)