
def text_change(input_txt):
    with open(input_txt, "r", encoding='utf-8') as file:
        lines = file.readlines()

    # 对每一行内容进行修改
    for i in range(len(lines)):
        # 这里是对每一行内容进行修改的具体代码
        speaker = "tutu"
        line = lines[i]
        new_line, text = line.strip().split("|")
        wav_path = new_line.split("/")[1]
        new_line = f"dataset/{speaker}/{wav_path}|{speaker}|ZH|{text}\n"
        lines[i] = new_line
        # 将修改后的内容保存到文件
    with open("output.txt", "w", encoding='utf-8') as file:
        file.writelines(lines)

input_text = "list.txt"
text_change(input_text)