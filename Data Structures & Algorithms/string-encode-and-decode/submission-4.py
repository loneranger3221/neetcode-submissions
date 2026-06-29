class Solution:

    def encode(self, strs: list[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        
        encoded = ""
        for s in strs:
            # Prefix each string with its length and a '#' delimiter
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        
        decoded = []
        i = 0  # Pointer to traverse the encoded string
        
        while i < len(s):
            # Find the delimiter '#' starting from our current position
            j = s.find('#', i)
            
            # The characters between i and j represent the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            decoded.append(s[start_of_str:end_of_str])
            
            # Move our pointer past the extracted string to process the next one
            i = end_of_str
            
        return decoded
