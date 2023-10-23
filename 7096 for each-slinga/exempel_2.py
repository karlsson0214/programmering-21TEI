# Exempel - räkna antal 'a' i en text
text = "alfabetet"

antal_a = 0

for bokstav in text:
    if bokstav == 'a':
        antal_a = antal_a + 1

print('antal a:', antal_a)
# utskriften blir:
# antal a: 2