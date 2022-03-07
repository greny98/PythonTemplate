from typing import List, Union


def check_list(l1: List[Union[int, float, str]], l2: List[Union[int, float, str]]) -> bool:
    """
    Check 2 list of single values are same
    :param l1: List 1
    :param l2: List 2
    :return: same or not
    """
    # Check length
    if len(l1) != len(l2):
        return False
    # Check elements are same
    for elm1, elm2 in zip(l1, l2):
        if elm1 != elm2:
            return False
    return True

def check_dict(d1: dict, d2: dict) -> bool:
    """
    TODO: Check 2 dictionary of single values are same
    :param d1: dictionary 1
    :param d2: dictionary 2
    :return: same or not
    """
    pass

def run_test(func, tests):
    """
    Run test and print
        + Correct! if test correct
        + Wrong! if test can run but wrong
        + Error! if test error
        + Score: <score> / <total>
    :param func: Function need evaluate
    :return: None
    """
    score = 0
    max_scores = len(tests)
    print("Results:")
    for idx, test in enumerate(tests):
        prefix = f"\t{idx + 1}: "
        try:
            pred = func(*test["inp"])
            # Run Check
            if isinstance(pred, list):
                is_correct = check_list(pred, test["out"])
            else:
                is_correct = pred == test["out"]
            # Check correct
            if is_correct:
                score += 1
                print(prefix + "Correct!")
            else:
                print(prefix + "Wrong!")
        except:
            print(prefix + "Error!")
    print(f"Score: {score} / {max_scores}")
