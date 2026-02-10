import re

# Slot dimensions
slot_width = 32  # rem
slot_height = 12  # rem
border_width = 1.625  # rem

# SVG viewBox dimensions
svg_width = 1000
svg_height = 230

# Calculate expected positions
expected_top_y = (border_width / 2) / slot_height * 100 / 100 * svg_height
expected_bottom_y = (slot_height - border_width / 2) / slot_height * 100 / 100 * svg_height
expected_left_x = (border_width / 2) / slot_width * 100 / 100 * svg_width
expected_right_x = (slot_width - border_width / 2) / slot_width * 100 / 100 * svg_width

print("Expected dot positions (in SVG units):")
print(f"  Top Y: {expected_top_y:.1f}")
print(f"  Bottom Y: {expected_bottom_y:.1f}")
print(f"  Left X: {expected_left_x:.1f}")
print(f"  Right X: {expected_right_x:.1f}")
print()

# Read actual SVG file
with open('src/assets/images/light-blubs.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

# Find actual coordinates in the SVG
top_dots = re.findall(r'M\d+\.?\d*,(15\.6)c0-3\.2', svg_content)
bottom_dots = re.findall(r'M\d+\.?\d*,(214\.4)c0-3\.2', svg_content)
left_dots = re.findall(r'M(25\.\d+),\d+\.?\d*c0-3\.2', svg_content)
right_dots = re.findall(r'M(974\.\d+),\d+\.?\d*c0-3\.2', svg_content)

print("Found in SVG file:")
print(f"  Top dots at Y=15.6: {len(top_dots)} dots")
print(f"  Bottom dots at Y=214.4: {len(bottom_dots)} dots")
print(f"  Left dots at X≈25.4: {len(left_dots)} dots")
print(f"  Right dots at X≈974.6: {len(right_dots)} dots")
print()

# Verification
all_correct = (
    len(top_dots) > 25 and  # Should have many top dots
    len(bottom_dots) > 25 and  # Should have many bottom dots
    len(left_dots) > 3 and  # Should have several left edge dots
    len(right_dots) > 3  # Should have several right edge dots
)

print("="*60)
if all_correct:
    print("✓ SUCCESS: Dots are NOW properly aligned with the border!")
    print("="*60)
    print(f"\nAll {len(top_dots) + len(bottom_dots) + len(left_dots) + len(right_dots)} decorative")
    print("light bulb dots are centered on the 1.625rem border.")
else:
    print("✗ ISSUE: Some dots may not be aligned correctly")
    print("="*60)
