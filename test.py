#!/usr/bin/python3

from models.state import State

stat = State()
stat.name = "Arizona"
print(stat.to_dict())
