message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
msg = []
for i in message:
    if i.isdigit():
        msg.extend(['"', i.zfill(2), '"'])
    elif i[1:].isdigit() and i[0] == '+' or i[0] == '-':
        msg.extend(['"', f'{i[0]}{int(i[1]):2}', '"'])
    else:
        msg.append(i)
str_msg = []
dub_sing = False
for i in range(len(msg)):
    str_msg.append(msg[i])
    if msg[i] == '"' and not dub_sing:
        dub_sing = True
    elif msg[i] == '"' and dub_sing:
        str_msg.append(" ")
        dub_sing = False
    elif msg[i] != '"' and i + 1 != len(msg) and not dub_sing:
        str_msg.append(" ")

print("".join(str_msg))





