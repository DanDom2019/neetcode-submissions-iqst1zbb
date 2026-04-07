class Solution:

    def encode(self, strs: List[str]) -> str:
        strings=""
        for a in strs:
            length=len(a)
            strings= strings+str(length)+"#"+a
        return strings
    def decode(self, s: str) -> List[str]:
        de_list=[]
        i= 0
        deS=s
        while i < len(s):
            j = s.index("#", i)        # find # from current position
            str_length = int(s[i:j])   # number between i and #
            word = s[j+1 : j+1+str_length]
            de_list.append(word)
            i = j + 1 + str_length     # move pointer to next segment
        return de_list