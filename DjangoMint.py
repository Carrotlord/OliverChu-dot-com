
OPERATORS = ["++", "--", "/", "+", "-", "^"]
# The lower the precedence, the more strongly
# an operator binds to its operand(s).
# The highest possible precedence is 0,
# reserved for cases such as function calls.
# -- ASUNA Yuuki
PRECEDENCES = {"++": 1, "--": 1, "^": 2, "/": 3, "+": 4, "-": 4}
MAX_PRECEDENCE = 4

# Grabs an item labeled with itemLabel
# out of the dictionary named bag.
# @author ASUNA Yuuki
def grab(bag, itemLabel):
    try:
        return bag[itemLabel]
    except:
        return None

# In Mint, there are hashed strings,
# categorical strings, ribbons (mutable strings),
# and strings (immutable strings)
#
# #hashed_right_here
# @Category
# 'this is a ribbon'
# "this is a string"
#
# Only the final two can have spaces in them.
#
# @author Oliver Chu
def mangleStrings(code):
    # Base case
    if '"' not in code and "'" not in code:
        return code
    def plusOne(char):
        return chr(ord(char) + 1)
    isInsideQuotes = False
    isInsideDoubleQuotes = False
    buffer = ""
    for eachChar in code:
        if isInsideQuotes:
            if eachChar == "'":
                isInsideQuotes = False
                continue
            else:
                buffer += plusOne(eachChar)
        elif isInsideDoubleQuotes:
            if eachChar == '"':
                isInsideDoubleQuotes = False
                continue
            else:
                buffer += plusOne(eachChar)
        else:
            if eachChar == "'":
                isInsideQuotes = True
                continue
            if eachChar == '"':
                isInsideDoubleQuotes = True
                continue
            buffer += eachChar
    return buffer

# Evaluates a single line of Mint 3.0 code.
# @author ASUNA Yuuki
# @author Oliver Chu
def evaluateMint3(code):
    # Evaluates Mint 3 code. First split on delimiters
    # which are actually binary & unary operators.
    # -- ASUNA Yuuki
    code = code.strip()
    code = mangleStrings(code)
    print(code)
    # Let us always use implicit multiplication.
    # -- ASUNA Yuuki
    code = code.replace("*", " ")
    for eachOp in OPERATORS:
        code = code.replace(eachOp, " " + eachOp + " ")
    tokens = code.split()
    # Unlike previous versions of Mint, allow
    # passing through the expression exactly once
    # for a linear time evaluation:
    indices = [[] for _ in range(MAX_PRECEDENCE + 1)]
    # We will have numbers = precedences
    # and values = indices to be evaluated.
    # -- Oliver Chu
    i = 0
    for token in tokens:
        operatorPrecedence = grab(PRECEDENCES, token)
        if operatorPrecedence is None:
            pass
        else:
            indices[operatorPrecedence].append(i)
        i += 1
    return indices
        
# @author Oliver Chu
def repl():
    while True:
        print("Mint 3.0> ", end="")
        commands = input()
        print(evaluateMint3(commands))

repl()
