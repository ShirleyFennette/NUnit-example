import os


def verify(unit, functional):
    if not all(v.isascii() and v.isdecimal() and int(v) > 0 for v in (unit, functional)):
        raise ValueError("Both jobs must report a positive Launch ID")
    if int(unit) == int(functional):
        raise ValueError(f"Jobs were merged into Launch {unit}; UID override did not separate launches")
    return f"Separate launches confirmed: unit={unit}, functional={functional}"


if __name__ == "__main__":
    message = verify(os.environ.get("UNIT_LAUNCH", ""), os.environ.get("FUNCTIONAL_LAUNCH", ""))
    print(message)
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as summary:
        summary.write(message + "\n")
