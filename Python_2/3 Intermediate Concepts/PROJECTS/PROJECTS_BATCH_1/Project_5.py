
def greet(*names: str, **options):
    response = []

    prefix = options.get('prefix', "Halloha!")
    punctuation = options.get('punctuation', '!!!')
    upper = options.get('upper', False)

    for name in names:
        final_name = name.upper() if upper else name
        greeting = f'{prefix} {final_name}{punctuation}'
        response.append(greeting)
    return response



greetings = greet('kopi', 'nryo', 'kophalem', 'pipoy', 'walter',
      prefix="Hallo",
      upper=True
      )

for greeting in greetings:
    print(greeting)
