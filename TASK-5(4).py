# Lambda function to check if a string is a number (int or float)
is_number = lambda s: bool(s) and s.replace('.', '', 1).isdigit() and s.count('.') <= 1
# Test cases
test_strings = ["123", "45.67", "abc", "12.3.4", "", ".45", "0"]
for t in test_strings:
    print(f"{t!r} -> {is_number(t)}")
