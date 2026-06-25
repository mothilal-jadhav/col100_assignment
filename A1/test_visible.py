import logging
from datetime import datetime
from assignment import digit_dominance, number_hill, first_repeated_digit, hollow_right_triangle

LOG_FILE = "test_results.log"
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def test_digit_dominance():
    """Test cases for digit_dominance function"""
    logger.info("="*60)
    logger.info("Testing: digit_dominance")
    logger.info("="*60)
    
    test_cases = [
        (9607004, "MoreEven"),
        (13579, "MoreOdd"),
        (1234, "Equal"),
    ]
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        try:
            result = digit_dominance(input_val)
            status = "PASS" if result == expected else "FAIL"
            logger.info(f"Test Case {i}: {status}")
            logger.info(f"  Input: {input_val}")
            logger.info(f"  Expected: {expected}")
            logger.info(f"  Got: {result}")
            
            if result == expected:
                passed += 1
            else:
                logger.warning(f"  Value mismatch")
        except Exception as e:
            logger.error(f"Test Case {i}: EXCEPTION - {type(e).__name__}: {str(e)}")
    
    logger.info(f"digit_dominance: {passed}/{len(test_cases)} passed\n")
    return passed, len(test_cases)


def test_number_hill():
    """Test cases for number_hill function"""
    logger.info("="*60)
    logger.info("Testing: number_hill")
    logger.info("="*60)
    
    test_cases = [
        (3, "1\n121\n12321\n121\n1"),
        (5, "1\n121\n12321\n1234321\n123454321\n1234321\n12321\n121\n1"),
    ]
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        try:
            result = number_hill(input_val)
            status = "PASS" if result == expected else "FAIL"
            logger.info(f"Test Case {i}: {status}")
            logger.info(f"  Input: {input_val}")
            logger.info(f"  Expected:\n  {expected.replace(chr(10), chr(10) + '  ')}")
            logger.info(f"  Got:\n  {result.replace(chr(10), chr(10) + '  ')}")
            
            if result == expected:
                passed += 1
            else:
                logger.warning(f"  Pattern mismatch")
        except Exception as e:
            logger.error(f"Test Case {i}: EXCEPTION - {type(e).__name__}: {str(e)}")
    
    logger.info(f"number_hill: {passed}/{len(test_cases)} passed\n")
    return passed, len(test_cases)


def test_first_repeated_digit():
    """Test cases for first_repeated_digit function"""
    logger.info("="*60)
    logger.info("Testing: first_repeated_digit")
    logger.info("="*60)
    
    test_cases = [
        (527352, "2"),
        (987654, "No Repetition"),
        (10023, "0"),
        (4543214, "4"),
    ]
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        try:
            result = first_repeated_digit(input_val)
            status = "PASS" if result == expected else "FAIL"
            logger.info(f"Test Case {i}: {status}")
            logger.info(f"  Input: {input_val}")
            logger.info(f"  Expected: {expected}")
            logger.info(f"  Got: {result}")
            
            if result == expected:
                passed += 1
            else:
                logger.warning(f"  Value mismatch")
        except Exception as e:
            logger.error(f"Test Case {i}: EXCEPTION - {type(e).__name__}: {str(e)}")
    
    logger.info(f"first_repeated_digit: {passed}/{len(test_cases)} passed\n")
    return passed, len(test_cases)


def test_hollow_right_triangle():
    """Test cases for hollow_right_triangle function"""
    logger.info("="*60)
    logger.info("Testing: hollow_right_triangle")
    logger.info("="*60)
    
    test_cases = [
        (4, "*\n**\n* *\n****"),
        (6, "*\n**\n* *\n*  *\n*   *\n******"),
    ]
    
    passed = 0
    for i, (input_val, expected) in enumerate(test_cases, 1):
        try:
            result = hollow_right_triangle(input_val)
            status = "PASS" if result == expected else "FAIL"
            logger.info(f"Test Case {i}: {status}")
            logger.info(f"  Input: {input_val}")
            logger.info(f"  Expected:\n  {expected.replace(chr(10), chr(10) + '  ')}")
            logger.info(f"  Got:\n  {result.replace(chr(10), chr(10) + '  ')}")
            
            if result == expected:
                passed += 1
            else:
                logger.warning(f"  Pattern mismatch")
        except Exception as e:
            logger.error(f"Test Case {i}: EXCEPTION - {type(e).__name__}: {str(e)}")
    
    logger.info(f"hollow_right_triangle: {passed}/{len(test_cases)} passed\n")
    return passed, len(test_cases)


def main():
    """Run all test cases"""    
    logger.info("="*60)
    logger.info("COL100/COL1000 Assignment 1 - Test Suite")
    logger.info("="*60 + "\n")
    
    results = []
    try:
        results.append(("digit_dominance", test_digit_dominance()))
    except Exception as e:
        logger.error(f"Error in digit_dominance test function: {type(e).__name__}: {str(e)}")
        results.append(("digit_dominance", (0, 3)))
    
    try:
        results.append(("number_hill", test_number_hill()))
    except Exception as e:
        logger.error(f"Error in number_hill test function: {type(e).__name__}: {str(e)}")
        results.append(("number_hill", (0, 2)))
    
    try:
        results.append(("first_repeated_digit", test_first_repeated_digit()))
    except Exception as e:
        logger.error(f"Error in first_repeated_digit test function: {type(e).__name__}: {str(e)}")
        results.append(("first_repeated_digit", (0, 4)))
    
    try:
        results.append(("hollow_right_triangle", test_hollow_right_triangle()))
    except Exception as e:
        logger.error(f"Error in hollow_right_triangle test function: {type(e).__name__}: {str(e)}")
        results.append(("hollow_right_triangle", (0, 2)))
    
    logger.info("="*60)
    logger.info("SUMMARY")
    logger.info("="*60)
    
    total_passed = 0
    total_tests = 0
    for func_name, (passed, total) in results:
        logger.info(f"{func_name:.<40} {passed}/{total}")
        total_passed += passed
        total_tests += total
    
    logger.info("="*60)
    logger.info(f"{'Overall':.<40} {total_passed}/{total_tests}")
    logger.info("="*60)
    
    return total_passed == total_tests


if __name__ == "__main__":
    main()
