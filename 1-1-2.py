from turing_machine import TuringMachine2

initial_state = "init",
transition_function = {("init","0"):("init", "x"),
                       ("init","0"):("init", "R"),
                       ("init","1"):("init", "x"),
                       ("init","1"):("init", "R"),
                       ("init"," "):("q_accept"," "),
                       ("init","#"):("q_reject","#"),
                       }
final_states = {"q_accept", "q_reject"}

t = TuringMachine2("010 011#",
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

