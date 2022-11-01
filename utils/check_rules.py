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
    # Check the legitimacy of file rules
    if os.path.exists(txt_or_txt_file):
        file = open(txt_or_txt_file, 'r')
        readfile = file.read()
        is_file = True
        for rule in readfile.split(sep="\n"):
            if "：" in rule:
                rule_segment = rule.split(sep="：")
                if len(rule_segment) == 2:
                    if rule_segment[0].split(sep="）")[1] == None or rule_segment[1] == None:
                        return False
                else:
                    return False


if __name__ == "__main__":
    check_origin_rules()
    extend_path = "./dataset/extend_rules.txt"
    check_extend_rules(extend_path)