# use for loop collect dict value to set and print this set
# set not allow repeat
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
language_set = set()
for language in favorite_languages.values():
    language_set.add(language)
print(language_set)