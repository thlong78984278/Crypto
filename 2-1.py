
from turing_machine import TuringMachine

transition_function = {    
  ("s"," "):("q0", " ", "R"), 
  ("q0","1"):("q1", " ", "R"), 
  ("q0","+"):("q2", " ", "R"), 
  ("q1","1"):("q1", "1", "R"),
  ("q1","+"):("q2", "1", "R"),
  ("q2","1"):("q2", "1", "R"),
  ("q2","="):("y", " ", "L"), 
}

final_states = {"y"}

t = TuringMachine(" 11111+11=",
                  initial_state = "s",
                  final_states = final_states,
                  transition_function=transition_function)

while not t.final():
    t.step()