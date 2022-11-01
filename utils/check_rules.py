from rules import init_rules, Point


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


def check_extend_rules():
    pass

if __name__ == "__main__":
    check_origin_rules()