import pytest
import copy


def test_part_one():
    assert [2, 0, 0, 0, 99] == compute([1, 0, 0, 0, 99])
    assert [2, 3, 0, 6, 99] == compute([2, 3, 0, 3, 99])
    assert [2, 4, 4, 5, 99, 9801] == compute([2, 4, 4, 5, 99, 0])
    assert [30, 1, 1, 4, 2, 5, 6, 0, 99] == compute([1, 1, 1, 4, 99, 5, 6, 0, 99])


def compute(input_program, noun=None, verb=None):
    program = copy.deepcopy(input_program)
    program[1] = noun if noun is not None else program[1]
    program[2] = verb if verb is not None else program[2]
    ops_pointer = 0
    
    while True:
        current_op = program[ops_pointer]

        if current_op == 99:
            break
        elif current_op == 1:
            program[program[ops_pointer + 3]] = program[program[ops_pointer + 1]] + program[program[ops_pointer + 2]]
            ops_pointer += 4
        elif current_op == 2:
            program[program[ops_pointer + 3]] = program[program[ops_pointer + 1]] * program[program[ops_pointer + 2]]
            ops_pointer += 4
        else:
            raise Exception("Unknown Operation: {}".format(current_op))

    return program


def part_one(program):
    # Replace according to instructions
    
    print("Input Program:\n{}".format(program))
    print("Output Program:\n{}".format(compute(program, 12, 2)))
    

def part_two(program):
    for noun in range(100):
        for verb in range(100):
            print("Testing [noun, verb]: [{},{}]".format(noun, verb))
            result = compute(program, noun, verb)
            print(result[0])
            if compute(program, noun, verb)[0] == 19690720:
                print("Winning Noun Verb: {}, {}".format(noun, verb))
                return (noun, verb)



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program_list = f.readline().strip().split(",")
        program = list(map(int, program_list))
        # part_one(program)
        print(part_two(program))
        
