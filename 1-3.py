from turing_machine import TuringMachine

initial_state = "q1",
transition_function = {("q1","0"):("q2", "x", "R"),
                       ("q1","1"):("q3", "x", "R"),
                       ("q1","#"):("q8", "#", "R"),
                       ("q2","0"):("q2", "0", "R"),
                       ("q2","1"):("q2", "1", "R"),
                       ("q2","#"):("q4", "#", "R"),
                       ("q3","0"):("q3", "0", "R"),
                       ("q3","1"):("q3", "1", "R"),
                       ("q3","#"):("q5", "#", "R"),
                       ("q4","x"):("q4", "x", "R"),
                       ("q4","0"):("q6", "x", "L"),
                       ("q4","1"):("n", "1", "L"),
                       ("q5","x"):("q5", "x", "R"),
                       ("q5","1"):("q6", "x", "L"),
                       ("q5","0"):("n", "0", "L"),
                       ("q6","0"):("q6", "0", "L"),
                       ("q6","1"):("q6", "1", "L"),
                       ("q6","x"):("q6", "x", "L"),
                       ("q6","#"):("q7", "#", "L"),
                       ("q7","0"):("q7", "0", "L"),
                       ("q7","1"):("q7", "1", "L"),
                       ("q7","x"):("q1", "x", "R"),
                       ("q8","x"):("q8", "x", "R"),
                       ("q8"," "):("y", " ", "R")
                       }
final_states = {"y", "n"}

print('Compare two binary number\nFor example: To compare 100 to 101 input the string "100#101"\n')

tape = input("Input on Tape: ")

t = TuringMachine(tape,
                  initial_state = "q1",
                  final_states = final_states,
                  transition_function=transition_function)

while not t.final():
    t.step()