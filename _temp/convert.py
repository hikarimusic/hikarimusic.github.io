with open('../_note/physics.md', 'r') as f:
    lines = f.readlines()

result = []
i = 0
while i < len(lines):
    # Check if this line is {: .notice--primary}
    if lines[i].strip() == '{: .notice--primary}':
        # Remove the preceding $$ ... $$ block
        # Walk backwards from result to find the opening $$
        # First, remove any blank lines at end of result
        while result and result[-1].strip() == '':
            result.pop()
        # The last line should be '$$'
        if result and result[-1].strip() == '$$':
            result.pop()  # remove closing $$
            # Now remove lines until we find the opening $$
            while result and result[-1].strip() != '$$':
                result.pop()
            if result and result[-1].strip() == '$$':
                result.pop()  # remove opening $$
            # Remove any trailing blank lines before the block
            while result and result[-1].strip() == '':
                result.pop()
            # Add back one blank line
            result.append('\n')
        i += 1
    else:
        result.append(lines[i])
        i += 1

# Clean up triple+ blank lines
text = ''.join(result)
import re
text = re.sub(r'\n{3,}', '\n\n', text)

with open('physics_cleaned.md', 'w') as f:
    f.write(text)

count_primary = text.count('{: .notice--primary}')
count_info = text.count('{: .notice--info}')
print(f"notice--primary: {count_primary}")
print(f"notice--info: {count_info}")

# Original counts for comparison
orig = ''.join(lines)
print(f"Original notice--primary: {orig.count('{: .notice--primary}')}")
print(f"Original notice--info: {orig.count('{: .notice--info}')}")