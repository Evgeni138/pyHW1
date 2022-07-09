# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x,y,z = None, None, None
if not(x or y or z) == (not x and not y and not z):
    print('true')
else:
    print('false')