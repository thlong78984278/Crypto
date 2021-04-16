from turing_machine import TuringMachine2

initial_state = "q0",
transition_function = { ("q0","a"):("q0", " "),
                        ("q0"," "):("q1", "R"),
                        ("q1", "a"):("q0", "a"),
                        ("q1", " "):("h", " "),
                      }
final_states = {"h"}

t = TuringMachine2( "aaaaaa ",
                    initial_state = "q0",
                    final_states = final_states,
                    transition_function=transition_function )

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()