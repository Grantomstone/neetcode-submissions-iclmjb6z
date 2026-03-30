class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\n"
        output = ""
        for item in strs:
            output += f"{item}\n"
        return output[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "\n":
            return []
        return s.split("\n")