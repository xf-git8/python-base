# use for loop print dict key and value with items()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
for item in favorite_languages.items():
    print(item)
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")