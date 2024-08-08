import math
import os


def lshi(a, step):
    return a[step:] + a[:step]


def action(name, word, ty):
    # алфавит для таблицы Виженера составлен из символов ASCII
    alphabet = [chr(i) for i in range(32, 128)] + [chr(i1) for i1 in range(1040, 1104)] + ["\n"] + ["ё"]
    gr = {alphabet[i]: {alphabet[j]: lshi(alphabet, i)[j] for j in range(len(alphabet))} for i in range(len(alphabet))}
    if ty == "-e":
        with open(name, "r", encoding="utf-8") as f:
            text = f.read()
        n, n1 = len(text), len(word)
        temp = (math.ceil(n / n1) * word)[:n]
        with open(os.path.splitext(name)[0] + ".par", "w", encoding="utf-8") as F:
            ans = ""
            for i in range(n):
                ans += gr[text[i]][temp[i]]
            F.write(ans)
    elif ty == "-d":
        with open(name, "r", encoding="utf-8") as f:
            text = f.read()
        n, n1 = len(text), len(word)
        temp = (math.ceil(n / n1) * word)[:n]
        with open(os.path.splitext(name)[0] + ".txt", "w", encoding="utf-8") as F:
            ans = ""
            for i in range(n):
                for key, value in gr[temp[i]].items():
                    if value == text[i]:
                        ans += key
            F.write(ans)
    else:
        print("Возникла ошибка при выборе режима (Достпуные режимы: <-d> - режим декодирвоания, <-e> - режим кодирования)")
