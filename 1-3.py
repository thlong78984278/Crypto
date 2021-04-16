from turing_machine import TuringMachine2

initial_state = "init"
transition_function = {
  ("init","a"):("q0","R"),
  ("q0","a"):("q1","L"),
  ("q0","b"):("q0","R"),
  ("q0"," "):("q0","R"),
  ("q1","a"):("q1","L"),
  ("q1","b"):("q2","R"),
  ("q1"," "):("q1","L"),
  ("q2","a"):("q2","R"),
  ("q2","b"):("q2","R"),
  ("q2"," "):("h"," "),
}
final_states = {"h"}

t = TuringMachine2( "abb bb   aba ",
                    initial_state = "init",
                    final_states = final_states,
                    transition_function=transition_function )

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()