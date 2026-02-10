import re

# Read the SVG file
with open('src/assets/images/light-blubs.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

print("Original SVG read. Starting coordinate corrections...")

# Coordinate corrections based on analysis:
# Bottom horizontal dots: Y should be 214.4 (currently 217)
# Top horizontal dots: Y should be 15.6 (currently 13)  
# Left vertical edge: X should be around 25.4 (currently 7.1)
# Right vertical edge: X should be around 974.6 (currently 981-987)

# Step 1: Fix bottom horizontal row (Y=217 -> Y=214.4)
# Bottom dots at y=217, need to shift to y=214.4 (shift of -2.6)
svg_content = re.sub(r'(\d+),217c0-3\.2', r'\1,214.4c0-3.2', svg_content)  # center y
svg_content = re.sub(r'C(\d+\.?\d*),222\.9,(\d+\.?\d*),220\.2,(\d+\.?\d*),217z',  
                     r'C\1,220.3,\2,217.6,\3,214.4z', svg_content)  # curve coords
svg_content = svg_content.replace('M963,222.9L963,222.9L963,222.9c-3.3,0-5.9-2.6-5.9-5.9l0,0c0-3.2,2.6-5.9,5.9-5.9',
                                  'M963,220.3L963,220.3L963,220.3c-3.3,0-5.9-2.6-5.9-5.9l0,0c0-3.2,2.6-5.9,5.9-5.9')
svg_content = svg_content.replace('C969,220.2,966.4,222.8,963,222.9',
                                  'C969,217.6,966.4,220.2,963,220.3')

# Step 2: Fix top horizontal row (Y=13 -> Y=15.6)
# Top dots at y=13, need to shift to y=15.6 (shift of +2.6)
svg_content = re.sub(r'(\d+\.?\d*),13c0-3\.2', r'\1,15.6c0-3.2', svg_content)  # center y
svg_content = re.sub(r'C(\d+\.?\d*),18\.9,(\d+\.?\d*),16\.2,(\d+\.?\d*),13z',  
                     r'C\1,21.5,\2,18.2,\3,15.6z', svg_content)  # curve coords

# Step 3: Fix left vertical edge (X around 7-13 -> X around 25-31)
# Shift of +18
left_adjustments = [
    ('M7.7,198.9', 'M25.8,197.2'),
    ('M7.1,164.7', 'M25.4,164.7'),
    ('M7.1,131.6', 'M25.4,131.6'),
    ('M7.1,98.5', 'M25.4,98.5'),
    ('M7.1,65.5', 'M25.4,65.5'),
    ('M12.3,38.2', 'M30.4,38.1'),
    ('M13.1,38.3', 'M31.2,38.2'),
    ('C10.7,203.6', 'C28.8,203.5'),
    ('C9.8,170.5', 'C28.1,170.5'),
    ('C9.8,137.5', 'C28.1,137.5'),
    ('C9.8,104.4', 'C28.1,104.4'),
    ('C9.8,71.3', 'C28.1,71.3'),
]

for old, new in left_adjustments:
    svg_content = svg_content.replace(old, new)

# Step 4: Fix right vertical edge (X around 981-987 -> X around 974.6)
# Shift of approximately -7 to -12
right_adjustments = [
    ('M985.5,203.3', 'M974.6,203.3'),
    ('M986.2,203.4', 'M975.3,203.4'),
    ('M981.1,164.5', 'M974.6,164.5'),
    ('C983.8,170.3', 'C977.3,170.3'),
    ('M981.1,131.4', 'M974.6,131.4'),
    ('C983.8,137.3', 'C977.3,137.3'),
    ('M981.1,98.3', 'M974.6,98.3'),
    ('C983.8,104.2', 'C977.3,104.2'),
    ('M981.1,65.3', 'M974.6,65.3'),
    ('C983.8,71.1', 'C977.3,71.1'),
    ('M980.8,33.4', 'M974.6,33.4'),
    ('M983.8,38.1', 'M977.3,38.1'),
]

for old, new in right_adjustments:
    svg_content = svg_content.replace(old, new)

# Write the corrected SVG
with open('src/assets/images/light-blubs.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("✓ SVG alignment corrected successfully!")
print("  - Bottom dots shifted from Y=217 to Y=214.4")
print("  - Top dots shifted from Y=13 to Y=15.6")
print("  - Left edge dots shifted from X≈7-13 to X≈25-31")
print("  - Right edge dots shifted from X≈981-987 to X≈974-977")
