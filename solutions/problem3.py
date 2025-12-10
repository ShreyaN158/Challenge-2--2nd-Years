def apply_state_machine(n, rules):
    state = "START"

    # Keep applying transitions until no rule matches
    while True:
        changed = False
        for (src, condition, dest) in rules:
            if src == state and eval(condition):
                state = dest
                changed = True
                break
        if not changed:
            break

    return state == "DONE"


def solve_problem3():
    with open("inputs/problem3_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = []
    rules = []
    reading_rules = False

    for line in lines:
        if line.startswith("numbers:"):
            nums = line.split(":")[1].strip().split()
            numbers = list(map(int, nums))
        elif line == "rules:":
            reading_rules = True
        elif reading_rules and line:
            # Example: A -> B if n%2==0
            src, arrow, rest = line.split(maxsplit=2)
            dest, _, condition = rest.partition(" if ")
            rules.append((src, condition, dest))

    done_count = sum(apply_state_machine(n, rules) for n in numbers)

    print(done_count)
    return done_count


if __name__ == "_main_":
    solve_problem3()