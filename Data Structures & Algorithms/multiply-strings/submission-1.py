class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        self.chtoi = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        self.itoch = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        nu1 = self.stoi(num1)
        nu2 = self.stoi(num2)
        return self.itos(nu1 * nu2)

    def stoi(self, string: str) -> int:
        output = 0
        for i, ch in enumerate(string):
            output += self.chtoi[ch] * pow(10, (len(string) - i - 1))
        return output
    
    def itos(self, integer: int) -> str:
        output = ""
        if integer == 0:
            return self.itoch[integer]
        while integer > 0:
            output = self.itoch[integer % 10] + output
            integer //= 10
        return output
        
