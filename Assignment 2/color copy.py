#!/usr/bin/env python3
#
# Solution of 720 Assignment 2 (linear-time 3-colorable algorithm)
# (mjd@cs.auckland.ac.nz)  Mar 2004
import sys, re, array

class tOp:
  "A t-parse Operator"
  def __init__(self,tok): self.tok=int(tok)
  def __str__(self): return str(self.tok)
  def isEdgeOp(self): return (self.tok > 9)
  def isVertexOp(self): return (self.tok <= 9)
  def v1(self): return self.tok % 10 # vertex 1
  def v2(self): return self.tok // 10 # vertex 2 if EdgeOp

def rankColoring(C):
  "extract boundary vertex coloring from state index"
  num=0
  for i in range(t+1): num=num*3+C[t-i]
  return num

def unrankColoring(num):
  "extract boundary vertex coloring from state index"
  C=[]
  for i in range(t+1):
    C.append(num % 3); num //= 3
  return C

def pw3Col(pwTokens,state):
  c_sum = 100000000
  "dynamic program for Pathwidth 3-Colorable"
  for op in pwTokens:
    o=tOp(op) #; print(o, end=" "), 
    if o.isEdgeOp():
      #If is edge
      v1=o.v1(); v2=o.v2() #Get vertex
      #Update state boundary
      for i in range(3**(t+1)): # update all state boundary combinations
        C=unrankColoring(i)                
        if C[v1]==C[v2]: 
          state[i]=0 # edge makes invalid coloring
        else:
          if(sum(C)<c_sum and sum(C)!=0):
            c_sum = sum(C)
    else: # isVertOp()
      v1=o.v1()
      for i in range(3**(t+1)):
        C=unrankColoring(i)
        if C[v1]==0: # process all coloring states only when v1 is colored 0           
           #C[v1]=1; i1=rankColoring(C)  # extract other slices
           #C[v1]=2; i2=rankColoring(C)
           #if max(state[i],state[i1],state[i2])==1: 
           #   state[i]=state[i1]=state[i2]=1
          if(sum(C)<c_sum and sum(C)!=0):
            c_sum = sum(C)
  totals.append(c_sum)
  return state
  
def tw3Col(G):
  "dynamic program for Treewidth 3-Colorable"
  G=G.strip(); # print("G=",G)
  state=array.array('i', map((lambda n:1), range(3**(t+1))))
  # state of empty t-parse
  if len(G)==0: 
    return state

  #Found parameter. tparse
  if G[0]!='(':
    return pw3Col(re.findall('\d+',G),state)

  #Otherwise check levels.
  lev=1 #G[0]=='('
  for i in range(1,len(G)):
    if G[i]==')':
      lev-=1
    elif G[i]=='(':
      lev+=1
    #Find first closing bracket
    if lev==0:
      #Process first closing bracket
      state1=tw3Col(G[1:i-1]) # strip a level of ()'s
      while True:
        k = G[i+1:len(G)].find('(')
        if k==-1:
          return pw3Col(re.findall('\d+',G[i+1:len(G)]),state1)
        for j in range(i+1+k,len(G)):
            if G[j]== ')':
              lev-=1
            elif G[j]=='(':
              lev+=1
            if lev==0:
                state2=tw3Col(G[i+2+k:j-1]) # circle plus found
                state=array.array('i')
                for l in range(3**(t+1)): # now update state for circle plus
                    state.append(min(state1[l],state2[l]))
                if j+1 < len(G):
                    state1=state
                    i=j+1
                    break # to find next circle plus
                else:
                    return state

# main program
#
while True:
    s=sys.stdin.readline().strip()              # read input graph
    print("="*10)
    i=s.find('('); t=int(s[0:i-1]); s=s[i:] # set global treewidth t
    global totals
    totals = [] 
    state = tw3Col(s)
    #print("3-Colorable =", ("No","Yes")[max(state)], "\n")
    try:
      print("TOTAL",min(totals))
    except ValueError:
      pass
    if t==0: break