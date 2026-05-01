class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        current_num=0
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))  
            elif token == "+":
                a =stack.pop(-1)
                b= stack.pop(-1)
                stack.append(a+b)
            elif token == "-":
                a =stack.pop(-1)
                b= stack.pop(-1)
                stack.append(b-a)
            elif token == "/":
                a =stack.pop(-1)
                b= stack.pop(-1)
                stack.append(int(b/a))
            elif token == "*":
                a =stack.pop(-1)
                b= stack.pop(-1)
                stack.append(a*b)
        return stack[0]