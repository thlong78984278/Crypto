from turing_machine import TuringMachine2

initial_state = "q0",
transition_function = { ("q0","a"):("q1", "b"),
                        ("q0","b"):("q1", "a"),
                        ("q0"," "):("h", " "),
                        ("q1","a"):("q0", "R"),
                        ("q1","b"):("q0", "R"),
                        ("q1"," "):("q0", "R"),
                      }
final_states = {"h"}

t = TuringMachine2( "aabbba ",
                    initial_state = "q0",
                    final_states = final_states,
                    transition_function=transition_function )

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()
