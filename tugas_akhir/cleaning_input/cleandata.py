# Setting Files
input = open('input_files/input-fix.txt', 'r')
output = open('input_files/output-fix.txt', 'w')

# Replace
clean = input.read().replace("#Economic", "#1.0").replace("#Security", "#2.0").replace("#Social", "#3.0").replace("#Infrastructure", "#4.0").replace("#Security", "#5.0").replace("#Education", "#6.0").replace("#Law", "#7.0").replace("#Energy", "#8.0").replace("#PublicHealth", "#9.0").replace("#Others", "#0.0").replace("#Other", "#0.0").replace("#other", "#0.0").replace("#PublicHeatlh", "#9.0")

output.write(clean)

