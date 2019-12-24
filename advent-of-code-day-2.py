test = "1,9,10,3,2,3,11,0,99,30,40,50" #3500,9,10,70,2,3,11,0,99,30,40,50
test2 = "1,0,0,0,99" #2,0,0,0,99 
test3 = "2,3,0,3,99" #2,3,0,6,99
test4 = "2,4,4,5,99,0" #2,4,4,5,99,9801
test5 = "1,1,1,4,99,5,6,0,99" #30,1,1,4,2,5,6,0,99
puzzle_input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,6,19,23,1,23,5,27,1,27,13,31,2,6,31,35,1,5,35,39,1,39,10,43,2,6,43,47,1,47,5,51,1,51,9,55,2,55,6,59,1,59,10,63,2,63,9,67,1,67,5,71,1,71,5,75,2,75,6,79,1,5,79,83,1,10,83,87,2,13,87,91,1,10,91,95,2,13,95,99,1,99,9,103,1,5,103,107,1,107,10,111,1,111,5,115,1,115,6,119,1,119,10,123,1,123,10,127,2,127,13,131,1,13,131,135,1,135,10,139,2,139,6,143,1,143,9,147,2,147,6,151,1,5,151,155,1,9,155,159,2,159,6,163,1,163,2,167,1,10,167,0,99,2,14,0,0"
memory = [int(x) for x in puzzle_input.split(",")]

def createIntCodeProgram(memory):
   intList = memory[:]
   instructionPointer = 4
   for i in range(0, len(intList), instructionPointer):
      oppCode = intList[i]
      addressAtZero = intList[0]
      noun = intList[i+1]
      verb = intList[i+2]
      if oppCode == 99:
         break;
      elif oppCode == 1:
         intList[intList[i+3]] = intList[noun] + intList[verb]
      elif oppCode == 2:
            intList[intList[i+3]] = intList[noun] * intList[verb]
   return addressAtZero
                
#createIntCodeProgram(input)

#Part 2
def findNounAndVerb(input_arr, result):
   for noun in range(100):
      for verb in range(100):
         input_arr[1] = noun
         input_arr[2] = verb
         output = createIntCodeProgram(input_arr)
         if (output == result):
            print('noun: ', noun)
            print('verb: ', verb)
            return (noun, verb)


findNounAndVerb(memory, 19690720)