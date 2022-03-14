from inspect import stack
from turtle import position
from typing import Counter
from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    def isEmpty(self):
        return self.size == 0
 
    def peek(self):
 
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

class GenCode(marzoListener):
   
    def __init__(self):
        self.stack = Stack()
        self.counter = 0
        self.dict = {}

    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".BeginProgram")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        self.stack.push(ctx.Numero().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD $" + str(self.counter) + ', ' + str(self.stack.pop()) + ", " + str(self.stack.pop()))
        self.counter += 1
    
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        self.stack.push(ctx.getTokens(marzoParser.Name)[0].getText())

    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        temp = self.stack.pop()
        if temp not in self.dict:
            self.dict[self.counter] = temp
            self.counter += 1
        key_list = list(self.dict.keys())
        val_list = list(self.dict.values())
        pos = val_list.index(temp)
        print('lw $' + str(key_list[pos]) + ' '  + ', 0')
    
    def enterComparation(self, ctx:marzoParser.ComparationContext):
        self.stack.push(ctx.getTokens(marzoParser.Name)[0].getText())
        self.counter+=1
        self.dict[self.counter] = ctx.getTokens(marzoParser.Name)[0].getText()
        self.stack.push(ctx.getTokens(marzoParser.Numero)[0].getText())
        self.counter += 1
        self.dict[self.counter] = ctx.getTokens(marzoParser.Numero)[0].getText()
    
    def exitComparation(self, ctx:marzoParser.ComparationContext):
        key_list = list(self.dict.keys())
        val_list = list(self.dict.values())
        
        num = self.stack.pop()
        name = self.stack.pop()
        pos = val_list.index(num)
        pos2 = val_list.index(name)
        print('eq $' + str(key_list[pos2]) + ', $' + str(key_list[pos]) + ' j ELSE')

    def enterIfConElse(self, ctx:marzoParser.IfConElseContext):
        print('IF ')
        #print('Testeo de valores ' + str(ctx.getToken(marzoParser.statements, 1)))


    def exitIfConElse(self, ctx:marzoParser.IfConElseContext):
        print('ENDIF')
        

    def enterAssign(self, ctx:marzoParser.AssignContext):
        self.stack.push(ctx.getTokens(marzoParser.Numero)[0].getText())
        self.stack.push(ctx.getTokens(marzoParser.Name)[0].getText())

    def exitAssign(self, ctx:marzoParser.AssignContext):
        temp = self.stack.pop()
        if temp not in self.dict:
            self.dict[self.counter] = temp
            self.counter += 1
        key_list = list(self.dict.keys())
        val_list = list(self.dict.values())
        pos = val_list.index(temp)
        print('lw $' + str(key_list[pos]) + ', ' + self.stack.pop())
        

    def exitPrintstmt(self, ctx:marzoParser.PrintstmtContext):
        print('prt ' + ctx.getTokens(marzoParser.Numero)[0].getText())
