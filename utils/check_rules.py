from rules import init_rules, Point
import os

def check_origin_rules():
    datasets, emissions, targets = init_rules()

    # Check the legitimacy of targets
    for target in targets:
        if datasets[target] == None:
            return False

    # Check the legitimacy of emissions
    for emission in emissions:
        if datasets[emission.result] == None:
            return False
    
    return True


def check_extend_rules(txt_or_txt_file):
    if os.path.exists(txt_or_txt_file):
        file = open(txt_or_txt_file, 'r')
        readfile = file.read()
        is_file = True
        print(readfile)


if __name__ == "__main__":
    check_origin_rules()
    extend_path = "./dataset/extend_rules.txt"
    check_extend_rules(extend_path)