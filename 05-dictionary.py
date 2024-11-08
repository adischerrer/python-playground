info: dict[str, str] = {'firstname': 'Bob', 'lastname': 'Smith'}
print(f'{info=}')
print("\n--------------------------------------------------------------------------------")

# Get attribute by name
print(f'{info['firstname']=}')

# This can cause trouble in case the attribute "xyz" does not exist
# print(info['xyz'])  =>  KeyError: 'xyz'

# Better use the getter which will return None in case the attribute does not exist
print(f'{info.get('firstname')=}')
print(f'Non-existing attribute xyz: {info.get('xyz')=}')
print(f'Non-existing attribute xyz with fallback: {info.get('xyz', 'n/a')=}')
print("\n--------------------------------------------------------------------------------")

scores: dict[str, int] = {'Bob': 88, 'Alice': 103}
print(f'{scores=}')
score_bob: int = scores.setdefault('Bob', 123)
print(f'{score_bob=} will return 88, since it is already defined')
score_james: int = scores.setdefault('James', 123)
print(f'{score_james=} will return 123, since James is not in the scores dict - but will be added!')
print(f'{scores=}')
print(f'Values {scores.values()=}')
print(f'Average {sum(scores.values())/len(scores.values())=}')
print("\n--------------------------------------------------------------------------------")

# Merging dictionaries
d1: dict[str, int] = {'a': 1, 'b': 2}
d2: dict[str, int] = {'c': 1, 'd': 2}
print(f'{d1=}')
print(f'{d2=}')
print(f'{d1|d2=}')
