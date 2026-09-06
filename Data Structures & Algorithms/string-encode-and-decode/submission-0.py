class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):

            j = i

            # '#' find karo
            while s[j] != '#':
                j += 1

            # '#' se pehle jo number hai = word ki length
            length = int(s[i:j])

            # word extract karo
            word = s[j + 1 : j + 1 + length]

            decoded.append(word)

            # next word par move karo
            i = j + 1 + length

        return decoded
