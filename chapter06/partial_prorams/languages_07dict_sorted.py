# user for loop dict key and print with sorted()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}")
