from turing_machine import TuringMachine2

transition_function = {
  ("init"," "):("q0","R"),
  ("init","a"):("q0","R"),
  ("q0"," "):("q1"," "),
  ("q0","a"):("q2"," "),
  ("q2"," "):("q3","R"),
  ("q3","a"):("q3","R"),
  ("q3"," "):("q4","R"),
  ("q4","a"):("q4","R"),
  ("q4"," "):("q5","a"),
  ("q5","a"):("q5","L"),
  ("q5"," "):("q6","L"),
  ("q6","a"):("q6","L"),
  ("q6"," "):("q7","a"),
  ("q7","a"):("q0","R"),
  ("q1","a"):("q1","R"),
  ("q1"," "):("h"," "),
}
final_states = {"h"}

t = TuringMachine2("aaa aaa aaa aaa aaa aaa aaaa aaa",
                    initial_state="init",
                    final_states=final_states,
                    transition_function=transition_function )

print("Input on tape:\n", t.get_tape())
while not t.final():
  t.step()