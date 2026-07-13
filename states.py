# In LangGraph to perform any task we create a graph
# And to create a graph the first thing we need is a state

import os
# 1. Using typed Dict
from typing import TypedDict
class State(TypedDict):
    topic:str
    summary:str
    score:int

# 2. pydantic approach -- It is good for data validation 
from pydantic import BaseModel,field_validator
class State(BaseModel):
    topic:str
    summary:str=""
    score:int

    @field_validator
    def score_positive(cls,v):
        if v<0:
            raise ValueError("Score must be positive")
        return v

# 3. Python dataclasses
from dataclasses import dataclass,field

@dataclass
class State:
    topic:str=""
    summary:str=""
    score:int=0

# 4.
from langgraph.graph import MessagesState
class State(MessagesState):
    topic:str
    summary:str
    score:int
