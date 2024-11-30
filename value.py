# '''
# UI 를 구성할때는 특정 요소의 크기 변경이 다른 요소의 크기 변경을 불러올때가 있다.
# 이러한 상황을 쉽게 해결하기 위해 각 값이나 크기간의 관계를 정의하고, 
# 계층적으로 계산할수 있도록 다양한 value 객체를 사용한다
# 근데 버림 ㅋ
# '''

# from typing import Optional


# class RelativeType:
#     ABS: int = 0
#     ADD: int = 1
#     MULTIPLY: int = 2
#     DIVIDE: int = 3


# class RelativeValue():
#     '''
#     다른 값을 참조하는 상대적인 값을 정의하는데 사용되는 클래수.
#     다른 RelativeValue 객체를 참조하지만,
#     relativeType 이 ABS 일경우 다른 객체를 참조하지 않고,
#     절대적인 값을 가짐
#     '''
    
#     def __init__(self, 
#                  value: Optional[float], 
#                  relativeType: int,
#                  referenceValue: Optional['RelativeValue']) -> None:
        
#         self.origValue: float = value
#         self.referenceValue: 'RelativeValue' = referenceValue
#         self.relativeType = relativeType

#     @property
#     def value(self) -> float:
#         '''
#         맘스터치 먹고싶다
#         '''
#         match self.relativeType:
#             case RelativeType.ABS:
#                 return self.origValue
#             case RelativeType.ADD:
#                 return self.referenceValue.value + self.origValue
#             case RelativeType.MULTIPLY:
#                 return self.referenceValue.value * self.origValue
#             case RelativeType.DIVIDE:
#                 return self.referenceValue.value / self.origValue

#     @value.setter
#     def value(self):
#         '''
#         해당하는 값을 성립시키는 value 를 계산하여 설정함
#         '''
#         # TODO ㅋ