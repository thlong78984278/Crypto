from turing_machine import TuringMachine2

# R not ⊔
transition_function = {
  ("q0"," "):("q0","R"),
  ("q0","a"):("h","a")
}
final_states = {"h"}

t = TuringMachine2( "      a ",
                    initial_state = "q0",
                    final_states = final_states,
                    transition_function=transition_function )
print("Input on Tape:\n" + t.get_tape())
while not t.final():
    t.step()

# R ⊔
transition_function = {
  ("q0","a"):("q0","R"),
  ("q0"," "):("h"," ")
}

t = TuringMachine2( "aa  a ",
                    initial_state = "q0",
                    final_states = final_states,
                    transition_function=transition_function )

print("Input on Tape:\n" + t.get_tape())
while not t.final():
    t.step()