# creating graph for states

import os
import typing

#1) typed DICT - most common approach

from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int

#2) pydantic approach
# good at data validation and type checking

from langgraph.graph import MessagesState
from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic : str
    summary : str
    score : int

    @field_validator('score')
    def score_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Score must be a positive integer')


#python dataclasses approach
#standard python dataclass but it is used very rarely

from dataclasses import dataclass, field

@dataclass
class State:
    topic : str = ""
    summary : str = ""
    score : int = field(default_factory=list)

class State(MessagesState):
  #messages field is alreadt icluded with add_messages reducer
  # just add your extra fields 
    user_name : str = ""
    language : str = ""