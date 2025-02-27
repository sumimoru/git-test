class  Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
if __name__ == "__main__":
    numa = 23
    numb = 22

    print(Calculator.add(numa, numb))