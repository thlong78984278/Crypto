from turing_machine import TuringMachine

initial_state = "q1",
transition_function = {("q1","a"):("q2", "x", "R"),
                       ("q1","b"):("q3", "x", "R"),
                       ("q1","c"):("q7", "x", "R"),
                       ("q1","x"):("y", "x", "R"),

                       ("q2","a"):("q2", "a", "R"),
                       ("q2","b"):("q2", "b", "R"),
                       ("q2","c"):("q2", "c", "R"),
                       ("q2","x"):("q4", "x", "L"),
                       ("q2"," "):("q4", " ", "L"),

                       ("q3","a"):("q3", "a", "R"),
                       ("q3","b"):("q3", "b", "R"),
                       ("q3","c"):("q3", "c", "R"),
                       ("q3","x"):("q5", "x", "L"),
                       ("q3"," "):("q5", " ", "L"),

                       ("q4","x"):("y", "x", "R"),
                       ("q4","a"):("q6", "x", "L"),
                       ("q4","b"):("n", "b", "L"),
                       ("q4","c"):("n", "c", "L"),

                       ("q5","x"):("y", "x", "R"),
                       ("q5","a"):("n", "a", "L"),
                       ("q5","b"):("q6", "x", "L"),
                       ("q5","c"):("n", "c", "L"),

                       ("q6","a"):("q6", "a", "L"),
                       ("q6","b"):("q6", "b", "L"),
                       ("q6","c"):("q6", "c", "L"),
                       ("q6","x"):("q1", "x", "R"),

                       ("q7","a"):("q7", "a", "R"),
                       ("q7","b"):("q7", "b", "R"),
                       ("q7","c"):("q7", "c", "R"),
                       ("q7"," "):("q8", " ", "L"),
                       ("q7","x"):("q8", "x", "L"),

                       ("q8","x"):("y", "x", "R"),
                       ("q8","a"):("n", "a", "L"),
                       ("q8","b"):("n", "b", "L"),
                       ("q8","c"):("q6", "x", "L"),
                       }
final_states = {"y", "n"}
tape = input("Input on Tape: ")

t = TuringMachine(tape,
                  initial_state = "q1",
                  final_states = final_states,
                  transition_function=transition_function)

while not t.final():
    t.step()