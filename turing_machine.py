class Tape(object):

    blank_symbol = " "

    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        # last line is equivalent to the following three lines:
        #self.__tape = {}
        #for i in range(len(tape_string)):
        #    self.__tape[i] = input[i]

    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char


class TuringMachine(object):

    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None,
                 reject_state = "NaN"):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        self.__reject_state = reject_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_current_state(self):
        return str(self.__current_state)

    def get_tape(self):
        return str(self.__tape)

    def print_current_state_and_tape(self):
        # print current state and the tape
        state_string = '(' + self.get_current_state() + ')'
        print("{0: <7}▷".format(state_string), end=" ")
        for i in range(len(self.get_tape()) + 1):
            c = self.__tape[i]
            if i == self.__head_position:
                print('{}_'.format(c), end="")
            else:
                print(c, end="")
        print()

    def step(self):
        self.print_current_state_and_tape()
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]
        else:
            print('Error: "{}, {}" is not recognizable'.format(self.__current_state, char_under_head))
            self.__current_state = self.__reject_state

    def final(self):
        if self.__current_state == self.__reject_state:
            return True
        if self.__current_state in self.__final_states:
            self.print_current_state_and_tape()
            return True
        else:
            return False


class TuringMachine2(object):
    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None,
                 reject_state = "NaN"):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        self.__reject_state = reject_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_current_state(self):
        return str(self.__current_state)

    def get_tape(self):
        return str(self.__tape)

    def print_current_state_and_tape(self):
        # print current state and the tape
        state_string = '(' + self.get_current_state() + ')'
        print("{0: <7}▷".format(state_string), end=" ")
        for i in range(len(self.get_tape()) + 1):
            c = self.__tape[i]
            if i == self.__head_position:
                print('{}_'.format(c), end="")
            else:
                print(c, end="")
        print()


    def step(self):
        self.print_current_state_and_tape()
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            # change a little bit of code here, is that ok? Idk But let's try
            if y[1] == "R":
                self.__head_position += 1
            elif y[1] == "L" and self.__head_position > 0:
                self.__head_position -= 1
            elif y[1] != "R" and y[1] != "L":
                self.__tape[self.__head_position] = y[1]
            self.__current_state = y[0]
        else:
            print('Error: "{}, {}" is not recognizable'.format(self.__current_state, char_under_head))
            self.__current_state = self.__reject_state


    def final(self):
        if self.__current_state == self.__reject_state:
            return True
        if self.__current_state in self.__final_states:
            self.print_current_state_and_tape()
            return True
        else:
            return False
