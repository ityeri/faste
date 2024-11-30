import pygame
from typing import Union
from numbers import Number
from typing import Callable

rv = Callable[..., float]

SupportRectValue = Union[
    pygame.Rect, 
    tuple[
        Number | Callable[..., Number], 
        Number | Callable[..., Number], 
        Number | Callable[..., Number], 
        Number | Callable[..., Number]]
    ]

SupportPosValue = tuple[Number | Callable[..., Number], Number | Callable[..., Number]]
SupportSizeValue = tuple[Number | Callable[..., Number], Number | Callable[..., Number]]

RelativeRectValue = tuple[Callable[..., Number], Callable[..., Number], Callable[..., Number], Callable[..., Number]]
RelativePosValue = tuple[Callable[..., Number], Callable[..., Number]]
RelativeSizeValue = tuple[Callable[..., Number], Callable[..., Number]]


DrawRectValue = tuple[int, int, int] | pygame.Rect

ColorValue = tuple[int, int, int]
