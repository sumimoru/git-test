class  Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b
    
    @staticmethod
    def mul(a: int, b: int) -> int:
        return a * b
    
    @staticmethod
    def div(a: int, b: int) -> int:
        return a / b
    
if __name__ == "__main__":
    numa = 23
    numb = 22

    print(Calculator.add(numa, numb))
    print(Calculator.sub(numa, numb))
    print(Calculator.mul(numa, numb))
    print(Calculator.div(numa, numb))