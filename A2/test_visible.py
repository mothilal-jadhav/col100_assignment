import io
import sys
import ast
from assignment import power, isEven, isOdd, count_paths, is_palindrome, generate_subsets

def run_test(test_name, func, args, expected_output, is_q5=False):
    print(f"--- Testing {test_name} ---")
    captured_out = io.StringIO()
    original_out = sys.stdout
    sys.stdout = captured_out
    
    try:
        if isinstance(args, tuple):
            func(*args)
        else:
            func(args)
    except Exception as e:
        sys.stdout = original_out
        print(f"FAIL: Exception occurred: {e}\n")
        return False
        
    sys.stdout = original_out
    actual_stdout = captured_out.getvalue()
    
    if is_q5:
        # Dynamic checking for Q5 (order-agnostic)
        try:
            # Extract the list part from the output string
            list_str = actual_stdout[actual_stdout.find('['):actual_stdout.rfind(']')+1]
            actual_list = ast.literal_eval(list_str)
            
            # Sort inner lists, then sort outer list for comparison
            expected_sorted = sorted([sorted(sub) for sub in expected_output])
            actual_sorted = sorted([sorted(sub) for sub in actual_list])
            
            if expected_sorted == actual_sorted:
                print("PASS\n")
                return True
            else:
                print("FAIL")
                print(f"Expected Subsets (any order): {expected_output}")
                print(f"Your Output:\n{actual_stdout}\n")
                return False
        except Exception as e:
            print("FAIL: Could not parse your output. Ensure you are printing exactly in the format: Final Result: [[...]]")
            print(f"Your raw output was:\n{actual_stdout}\n")
            return False
    else:
        # String comparison for Q1-Q4 (whitespace stripped)
        actual_norm = "".join(actual_stdout.split())
        
        # Handle if expected_output is a list of valid options
        if isinstance(expected_output, list):
            passed = any(actual_norm == "".join(opt.split()) for opt in expected_output)
            expected_display = "\n  --- OR --- \n".join(expected_output)
        else:
            expected_norm = "".join(expected_output.split())
            passed = (actual_norm == expected_norm)
            expected_display = expected_output

        if passed:
            print("PASS\n")
            return True
        else:
            print("FAIL")
            print(f"Expected Output:\n{expected_display}")
            print(f"Your Output:\n{actual_stdout}\n")
            return False

def main():
    power_expected = "power(2, 3)\npower(2, 2)\npower(2, 1)\npower(2, 0)\nFinal Result: 8"
    run_test("Q1: Power", power, (2, 3), power_expected)

    even_expected = "isEven(4)\nisOdd(3)\nisEven(2)\nisOdd(1)\nisEven(0)\nFinal Result: True"
    run_test("Q2: Ping-Pong Parity", isEven, (4,), even_expected)

    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    paths_expected = "Final Result: 2"
    run_test("Q3: Grid Paths", count_paths, (grid,), paths_expected)

    pal_expected = ("Comparing: 'a' and 'a'\nComparing: 'm' and 'm'\n"
                    "Comparing: 'a' and 'a'\nComparing: 'n' and 'n'\n"
                    "Comparing: 'a' and 'a'\nComparing: 'p' and 'p'\n"
                    "Comparing: 'l' and 'l'\nComparing: 'a' and 'a'\n"
                    "Comparing: 'n' and 'n'\nComparing: 'a' and 'a'\nFinal Result: True")
    run_test("Q4: Palindrome", is_palindrome, ("A man a plan a canal Panama",), pal_expected)

    # Q5 is now fully dynamic and order-agnostic
    q5_expected = [[1, 2], [1], [2], []]
    run_test("Q5: Subsets", generate_subsets, ([1, 2],), q5_expected, is_q5=True)

if __name__ == "__main__":
    main()