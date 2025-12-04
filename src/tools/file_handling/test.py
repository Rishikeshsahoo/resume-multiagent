"""
Simple test runner that prints results clearly
"""
import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from pdf_tools import open_file, read_file, read_file_write_output

print("\n" + "="*60)
print("RUNNING TESTS FOR FILE HANDLING FUNCTIONS")
print("="*60)

# Test 1: open_file
print("\n[TEST 1] Testing open_file function...")
test_file = r"c:\Users\Rohit Ojha\projects\Rohit_Ojha_SDE_2YOE_Updated.pdf"

try:
    doc = open_file(test_file)
    if doc:
        page_count = len(doc)
        print(f"  Result: PASSED")
        print(f"  - Opened file successfully")
        print(f"  - Page count: {page_count}")
        doc.close()
        test1_passed = True
    else:
        print(f"  Result: FAILED - returned None")
        test1_passed = False
except Exception as e:
    print(f"  Result: FAILED - {e}")
    test1_passed = False

# Test 2: read_file
print("\n[TEST 2] Testing read_file function...")

try:
    text = read_file(test_file)
    if text and isinstance(text, str) and len(text) > 0:
        print(f"  Result: PASSED")
        print(f"  - Read file successfully")
        print(f"  - Text length: {len(text)} characters")
        print(f"  - Preview: {text[:80]}...")
        test2_passed = True
    else:
        print(f"  Result: FAILED - invalid text")
        test2_passed = False
except Exception as e:
    print(f"  Result: FAILED - {e}")
    test2_passed = False

# Test 3: read_file_write_output
print("\n[TEST 3] Testing read_file_write_output function...")

try:
    result = read_file_write_output(test_file, "test_output.txt")
    if result:
        print(f"  Result: PASSED")
        print(f"  - File written successfully")
        test3_passed = True
    else:
        print(f"  Result: FAILED - returned None")
        test3_passed = False
except Exception as e:
    print(f"  Result: FAILED - {e}")
    test3_passed = False

# Summary
print("\n" + "="*60)
print("TEST SUMMARY")
print("="*60)
print(f"open_file:  {'PASSED' if test1_passed else 'FAILED'}")
print(f"read_file:  {'PASSED' if test2_passed else 'FAILED'}")
print(f"read_file_write_output:  {'PASSED' if test3_passed else 'FAILED'}")
print("-"*60)
total = 3
passed = sum([test1_passed, test2_passed, test3_passed])
print(f"Total: {total} | Passed: {passed} | Failed: {total - passed}")
print("="*60 + "\n")
