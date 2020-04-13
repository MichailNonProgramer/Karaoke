import datetime, time

def text_to_lines(file):
    with open(file, 'r', encoding='utf8') as file:
        lines = file.readlines()
    return lines

def parce_lines_in_words(dict):
    res_dict = {}
    for index in dict:
        str = dict[index].split(' / ')
        time_for_one_word = round(int(str[1]) / len(str[0].split(' ')), 2)
        temp_dict = {}
        timer = 0
        for word in str[0].split(' '):
            temp_dict[timer] = word
            timer += time_for_one_word
        res_dict[index] = temp_dict
    print(res_dict)
    print(dict)
    return res_dict


def game_state(text):
    lines = text_to_lines(text)
    str = lines[0].split('//')
    return int(str[2].split('\n')[0])



def knife_text(dict, time, actual_time, game_play):
    state_dict = parce_lines_in_words(dict)
    if round(time) - 1 in dict:
        strs = dict[round(time) - 1].split(' /')
        # strs = state_dict[round(time) - 1]
        # for ind in strs:
        #     str = strs[ind]
        return  strs[0], int(strs[1]), intit_color(actual_time, time)
    else:
        if game_play:
             return  "", 0, (0, 0, 255)
        else:
            return "Приготовьтесь!", 0, (0,0,255)

def intit_color(actual_time, time_coloring):
    if actual_time >= time_coloring:
        return (255,0,255)
    else:
        return (0,0,255)

def init_dict(text):
    lines = text_to_lines(text)
    dict = {}
    for i in range(len(lines)):
        str = lines[i].split('//')
        dict[int(str[2].split('\n')[0])]= str[0] + '/ ' + str[1]
    return dict


parce_lines_in_words(init_dict('music/text/les.txt'))



