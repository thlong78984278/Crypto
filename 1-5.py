from turing_machine import TuringMachine2

transition_function = {
  ("init"," "):("q0","R"),
  ("q0","0"):("q1","X"),
  ("q0","1"):("n","1"),
  ("q0","X"):("y","X"),
  ("q1","X"):("q2","R"),
  ("q2","0"):("q2","R"),
  ("q2","X"):("n","X"),
  ("q2","1"):("q3","R"),
  ("q3","1"):("q3","R"),
  ("q3","0"):("n","0"),
  ("q3"," "):("q4","L"),
  ("q3","X"):("q4","L"),  # ->|
  ("q4","1"):("q5","X"),
  ("q5","X"):("q6","L"),
  ("q6","0"):("q6","L"),
  ("q6","1"):("q6","L"),
  ("q6","X"):("q0","R")
}

# 00001111
# X      X

final_states = { "n", "y"}

t = TuringMachine2(" 0000011111",
                    initial_state="init",
                    final_states=final_states,
                    transition_function=transition_function)

print("Input on tape:\n", t.get_tape())
while not t.final():
  t.step()