"""
各类单词的种类：标识符，常量，运算符，关键字，分隔符，注释，宏定义
IDENT:标识符，“abc"
INT_CONST,FLOAT_CONST,CHAR_CONST:常量
Comment
enum token_kind {ERROR_TOKEN, IDENT, INT_CONST,  FLOAT_CONST, CHAR_CONST,  INT ,FLOAT,CHAR,IF,ELSE,..........EQ,ASSIGN, ......,LP,RP,......  SEMI，COMMA，......}

词法规则：
现定义下划线，大小写字母，数字，小数点，单引号为字符类文字
（1）若开头是下划线和大写字母，往后继续直到出现非字符类文字，则停止并识别为标识符
（2）若开头为小写字母，则遍历一边所有关键字，找出是否有首字母是该字母的关键字，若有则接着往后匹配，直到出现非字符类文字，完全匹配该关键字（如int1不匹配int），则识别为该关键字，若未识别为关键字则识别为标识符
（4）若开头为数字，则往后识别，若后面出现下划线或者字母，则报错，若后面全是数字，则为整型常量，若后面有且仅有一个小数点，则识别为浮点型常量
（5）若开头为单引号，往下识别，之间为单个字母，结束为单引号，识别为字符常量
（6）若为“/"判断是块注释还是行注释
（7）若为“#”判断是否是宏定义
（8）跳过所有空格和换行
（9）其他不满足C语言词法情况均报错
"""
from enum import Enum


class TokenKind(Enum):
    ERROR_TOKEN = 1
    # 标识符
    IDENT = 2
    # 常量
    CONST_INT = 3
    CONST_FLOAT = 4
    CONST_CHAR = 5
    # 关键字
    INT = 6
    FLOAT = 7
    CHAR = 8
    LONG = 9
    SHORT = 10
    IF = 11
    ELSE = 12
    WHILE = 13
    FOR = 14
    VOID = 15
    BREAK = 16
    CONTINUE = 17
    RETURN = 18
    UNSIGNED = 19
    # 运算符
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    REMAINDER = 24
    GREATER = 25
    LESS = 26
    EQ = 27
    NEQ = 28
    GREATEREQ = 29
    LESSEQ = 30
    AND = 31
    OR = 32
    ASSIGN = 33
    # 界定符
    COLON = 34
    COMMA = 35
    SEMI = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    LCB = 41
    RCB = 42
    # 注释
    BCOMMENT = 43
    LCOMMENT = 44
    # 宏定义
    MACRO = 45


keywords = {"int", "float", "long", "short", "char", "if", "else", "while", "for", "void", "break", "continue",
            "return", "unsigned"}
operators = {"+", "-", "*", "/", "%", ">", "<", "==", ">=", "<=", "!=", "&&", "||", "="}  # 不包含逗号运算符、位运算符、各种单目运算符等等
separators = {":", ",", "(", ")", "[", "]", "{", "}", ";"}

key_dic = {
    "int": TokenKind.INT,
    "float": TokenKind.FLOAT,
    "long": TokenKind.LONG,
    "short": TokenKind.SHORT,
    "char": TokenKind.CHAR,
    "if": TokenKind.IF,
    "else": TokenKind.ELSE,
    "while": TokenKind.WHILE,
    "for": TokenKind.FOR,
    "void": TokenKind.VOID,
    "break": TokenKind.BREAK,
    "continue": TokenKind.CONTINUE,
    "return": TokenKind.RETURN,
    "unsigned": TokenKind.UNSIGNED,
}

sep_dict = {
    '(': TokenKind.LP,
    ')': TokenKind.RP,
    '[': TokenKind.LB,
    ']': TokenKind.RB,
    '{': TokenKind.LCB,
    '}': TokenKind.RCB,
    ';': TokenKind.SEMI,
    ',': TokenKind.COMMA,
    ':': TokenKind.COLON,
}

ope_dic = {
    '+': TokenKind.ADD,
    '-': TokenKind.SUB,
    '*': TokenKind.MUL,
    '/': TokenKind.DIV,
    '%': TokenKind.REMAINDER,
    '>': TokenKind.GREATER,
    '<': TokenKind.LESS,
    '=': TokenKind.ASSIGN,
    '==': TokenKind.EQ,
    '>=': TokenKind.GREATEREQ,
    '<=': TokenKind.LESSEQ,
    '!=': TokenKind.NEQ,
    '&&': TokenKind.AND,
    '||': TokenKind.OR,
}


class Token:
    def __init__(self, pos: int, kind: TokenKind, value: str):
        self.pos = pos
        self.kind = kind
        self.value = value


def tryMatchWord(txt, start_pos) -> Token:
    cur_pos = start_pos
    while cur_pos < len(txt) and (txt[cur_pos].isalnum() or txt[cur_pos] == '_'):
        cur_pos += 1
    token_value = txt[start_pos:cur_pos]
    # 检查是否是关键字
    if token_value in key_dic:
        return Token(start_pos, key_dic[token_value], token_value)
    else:
        return Token(start_pos, TokenKind.IDENT, token_value)


def tryMatchNumber(txt, start_pos) -> Token:
    cur_pos = start_pos
    is_float = False
    while cur_pos < len(txt):
        if txt[cur_pos].isdigit():
            cur_pos += 1
        elif txt[cur_pos] == '.' and not is_float:
            is_float = True
            cur_pos += 1
        else:
            break

    # 检查后面是否有非法字符（字母或下划线）
    if cur_pos < len(txt) and (txt[cur_pos].isalpha() or txt[cur_pos] == '_'):
        return Token(start_pos, TokenKind.ERROR_TOKEN, txt[start_pos:cur_pos + 1])
    elif is_float:
        return Token(start_pos, TokenKind.CONST_FLOAT, txt[start_pos:cur_pos])
    else:
        return Token(start_pos, TokenKind.CONST_INT, txt[start_pos:cur_pos])


def tryMatchComment(txt, start_pos):
    c = txt[start_pos + 1]
    cur_pos = start_pos + 2
    if c == "/":
        while cur_pos < len(txt):
            if txt[cur_pos] == '\n':
                return Token(start_pos, TokenKind.LCOMMENT, txt[start_pos:cur_pos])
            cur_pos += 1
    elif c == "*":
        while cur_pos < len(txt) - 1:
            if txt[cur_pos] == '*' and txt[cur_pos + 1] == '/':
                return Token(start_pos, TokenKind.BCOMMENT, txt[start_pos:cur_pos + 2])
            cur_pos += 1
    else:
        return Token(start_pos, TokenKind.ERROR_TOKEN, txt[start_pos])


def tryMatchOperator(txt, start_pos):
    c1 = txt[start_pos:start_pos + 1]
    c2 = txt[start_pos:start_pos + 2]
    if c2 in operators:
        return Token(start_pos, ope_dic[c2], c2)
    elif c1 in operators:
        return Token(start_pos, ope_dic[c1], c1)
    else:
        return Token(start_pos, TokenKind.ERROR_TOKEN, c1)


def tryMatchCharConstant(txt, start_pos) -> Token:
    if start_pos + 2 >= len(txt):
        return Token(start_pos, TokenKind.ERROR_TOKEN, txt[start_pos])

    c = txt[start_pos + 2]
    if c != "'":
        return Token(start_pos, TokenKind.ERROR_TOKEN, txt[start_pos])

    return Token(start_pos, TokenKind.CONST_CHAR, txt[start_pos:start_pos + 3])


def tryMatchMacro(txt, start_pos) -> Token:
    cur_pos = start_pos
    while cur_pos < len(txt):
        if txt[cur_pos] == '\n':
            return Token(start_pos, TokenKind.MACRO, txt[start_pos:cur_pos])
        cur_pos += 1


if __name__ == '__main__':
    fname = "tests/1.c"
    txt = open(fname, "rt").read() + "\n"

    tokens = []
    cur_pos = 0
    while cur_pos < len(txt):
        cur_char = txt[cur_pos]
        if cur_char == "/":
            next_c = txt[cur_pos + 1]
            if next_c == "/" or next_c == "*":
                token = tryMatchComment(txt, cur_pos)
            else:
                token = tryMatchOperator(txt, cur_pos)
        elif cur_char == "#":
            token = tryMatchMacro(txt, cur_pos)
        elif cur_char == '_' or ('A' <= cur_char <= 'Z') or ('a' <= cur_char <= 'z'):
            token = tryMatchWord(txt, cur_pos)
        elif '0' <= cur_char <= '9':
            token = tryMatchNumber(txt, cur_pos)
        elif cur_char == "'":
            token = tryMatchCharConstant(txt, cur_pos)
        elif cur_char in sep_dict.keys():
            token = Token(cur_pos, sep_dict[cur_char], txt[cur_pos])
        elif cur_char in {x[0] for x in ope_dic.keys()}:
            token = tryMatchOperator(txt, cur_pos)
        elif cur_char in " \r\n\t":
            cur_pos += 1
            continue
        else:
            token = Token(cur_pos, TokenKind.ERROR_TOKEN, cur_char)

        if token.kind == TokenKind.ERROR_TOKEN:
            print("ERROR: ", token.pos, txt[token.pos:token.pos + 20])
            break

        tokens.append(token)
        cur_pos += len(token.value)

    for t in tokens:
        print(t.kind, t.value)
