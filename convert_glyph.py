import json

def convert_to_expo_format(glyph_data):
    expo_data = {}
    for key, value in glyph_data.items():
        unicode_value = value.get("unicode", "")
        # Remove "&#x" prefix and ";" suffix from the Unicode value
        unicode_value = unicode_value.replace("&#x", "").replace(";", "")
        # Convert hexadecimal Unicode to decimal
        decimal_value = int(unicode_value, 16) if unicode_value else None
        expo_data[key] = decimal_value
    return expo_data

# Read glyph data from remixicon.glyph.json
with open("remixicon.glyph.json", "r") as file:
    glyph_data = json.load(file)

# Convert to Expo-compatible format
expo_data = convert_to_expo_format(glyph_data)

# Write to remixicon.expo.json
with open("remixicon.expo.json", "w") as file:
    json.dump(expo_data, file, indent=2)

print("Conversion completed. Output saved to remixicon.expo.json.")
