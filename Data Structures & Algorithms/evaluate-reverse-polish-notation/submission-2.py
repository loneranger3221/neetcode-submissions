class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''Note Reverse Polish Notation is Postfix Expression 
        We can use a stack to evaluate it : 
        when we find an operator pop the prev 2 operands ,
        operate on them and push the result in stack'''

        stack=[]#initializing empty stack

        import operator #to intialize operators to dictionary keys
        symbol_map={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/":  lambda a, b: int(a / b)  
    # This forces truncation toward zero immediately
    }
        
        #traversing the token list
        for token in tokens :
            if token in symbol_map:

                operand2=stack.pop()# second operand by LIFO
                operand1=stack.pop()# first operand by LIFO

                res=symbol_map[token](operand1,operand2)#STORING RESULT

                stack.append(res)
            else:
                stack.append(int(token))
        
        return int(stack[-1]) #at end the result will be at stack top the only elem left





