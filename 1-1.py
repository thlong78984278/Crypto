from turing_machine import TuringMachine

initial_state = "init",
transition_function = {("init","0"):("init", "x", "R"),
                       ("init","1"):("init", "x", "R"),
                       ("init"," "):("q_accept"," ", "N"),
                       ("init","#"):("q_reject","#", "N"),
                       }
final_states = {"q_accept", "q_reject"}

t = TuringMachine("010 011#",
                  initial_state = "init",
                  final_states = final_states,
                  transition_function=transition_function)

print("Input on Tape:\n" + t.get_tape())

while not t.final():
    t.step()

if t.get_current_state() == "q_accept":
    print("Found it!")
else:
    print("No luck today...")

