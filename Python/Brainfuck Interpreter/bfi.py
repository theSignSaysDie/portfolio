from typing import List, Dict
import argparse

# ------------
# Driver Class
# ------------
class BrainfuckInterpreter:
    """Provides an object which runs source code over input and a given tape length, provided during construction."""
    def __init__(self, source: str, tapeLength: int = 8, dumpTape = False):
        self.tape: List[int] = [0]*tapeLength
        self.source: str = source
        # Source cleaning, validation, preprocessing
        self.cleanSource()
        self.isValid = self.isSourceValid()
        if self.isValid:
            self.jumpPoints: Dict[int, int] = self.locateJumpPoints()

    def clearTape(self) -> None:
        """Empties the tape."""
        self.tape = [0 for _ in self.tape]
    
    def cleanSource(self) -> None:
        """Removes any non-Brainfuck characters from source."""
        self.source = "".join(i for i in self.source if i in "><+-,.[]")

    def isSourceValid(self) -> bool:
        """
        Validates that the given source has correctly nested and matched square brackets.
        """
        brackets: int = 0
        for c in self.source:
            if c == "[": brackets += 1
            if c == "]": brackets -= 1
            if brackets < 0: return False
        return brackets == 0
    
    def locateJumpPoints(self):
        """Returns a dictionary of jump points for square brackets.
        Precondition: isSourceValid is true"""
        pairs: Dict[int, int] = {}
        indexStack: List[int] = []
        for i, c in enumerate(self.source):
            if c == '[':
                indexStack.append(i)
            elif c == ']':
                start = indexStack.pop(-1)
                pairs[start] = i
                pairs[i] = start
        return pairs

    def interpretSource(self, inputs):
        """Runs its source and returns its output, or an error, as a string."""
        try:
            assert self.isValid, "SYNTAX ERROR"
            pTape:  int = 0
            pCode:  int = 0
            output: str = ""
            while pCode < len(self.source):
                # Process instruction
                inst: str = self.source[pCode]
                if   inst == "+": self.tape[pTape] += 1
                elif inst == "-": self.tape[pTape] -= 1
                elif inst == ">":           pTape  += 1
                elif inst == "<":           pTape  -= 1
                elif inst == ",": self.tape[pTape]  = inputs.pop(0)
                elif inst == ".": output           += chr(self.tape[pTape])
                elif inst == "[":           pCode   = self.jumpPoints[pCode] if self.tape[pTape] == 0 else pCode
                elif inst == "]":           pCode   = self.jumpPoints[pCode] if self.tape[pTape]  > 0 else pCode
                # Check for aberrant state
                assert 0 <= pTape < len(self.tape), "POINTER OUT OF BOUNDS"
                assert 0 <= self.tape[pTape] < 256, "INCORRECT VALUE"
                # Advance instruction pointer
                pCode += 1
            return output
        except AssertionError as msg:
            return msg
        finally:
            print(f"{self.tape=}")
            self.clearTape()

# -----------
# Driver code
# -----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input-file", dest='infile', required=True, help="Source code to run")
    parser.add_argument('-I', "--inputs", help="Byte inputs for program")
    args = parser.parse_args()

    with open(args.infile) as source_file:
        inputs: List[int] = []
        try:
            with open(args.inputs) as inputs_file:
                inputs = [*map(int, inputs_file.read().split())]
        except:
            pass

        source_code = source_file.read()
        
        bfi: BrainfuckInterpreter = BrainfuckInterpreter(source_code)
        print(bfi.interpretSource(inputs))


if __name__ == "__main__":
    main()
    

