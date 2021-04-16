from turing_machine import TuringMachine2

transition_functions = {
  ("q0"," "):("q0","R"),
  ("q0","a"):("q1","L"),
  ("q1"," "):("h","a")
}
final_states = {"h"}

t = TuringMachine2( tape = "    a ",
                    initial_state = "q0",
                    final_states = final_states,
                    transition_function = transition_functions )

print("Input on tape:\n", t.get_tape())
while not t.final():
  t.step()
