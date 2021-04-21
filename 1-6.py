from turing_machine import TuringMachine2

transition_function = {
  ("init"," "):("q0","R"),
  ("q0","a"):("q0","R"),
  ("q0","b"):("q1","R"),
  ("q0","c"):("n","c"),
  ("q1","a"):("n","a"),
  ("q1","b"):("q1","R"),
  ("q1","c"):("q2","R"),
  ("q2","a"):("n","a"),
  ("q2","b"):("n","b"),
  ("q2","c"):("q2","R"),
  ("q2"," "):("y"," "),
}

# 00001111
# X      X

final_states = { "n", "y"}

t = TuringMachine2(" aaaaabbbbcccc",
                    initial_state="init",
                    final_states=final_states,
                    transition_function=transition_function)

print("Input on tape:\n", t.get_tape())
while not t.final():
  t.step()