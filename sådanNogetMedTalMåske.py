# Spørger Mark om det er ham
markIsThatYou = input('Mark is that you?')

# Printer en lille besked
print('Det var heldigt, blev lidt bange der 😳')

# Spørger om et tal
try:
    aNumber = int(input('Skriv dit yndlingstal: '))

# Giver en error message, hvis det ikke lykkedes
except:
    print('What det virkede ikke, dårlig stil Mark')
    exit('CRINGE ONG 💀')

# Spørger om endnu et tal
anotherNumber = int(input('... Et til: '))

# Definerer math funktioner
summenAfTallene = aNumber + anotherNumber
differensenAfTallene = aNumber - anotherNumber
produktetAfTallene = aNumber * anotherNumber
kvotientenAfTallene = aNumber / anotherNumber

# Printer resultaterne
print('Summen af tallene er: ', summenAfTallene,'')
print('Differensen af tallene er: ', differensenAfTallene,'')
print('Produktet af tallene er: ', produktetAfTallene,'')
print('Kvotienten af tallene er: ', kvotientenAfTallene,'')

# Giver en besked
print('Ps. hvis du ikke vidste, hvad kvotient er, så er det helt okay, jeg havde heller ingen ide før 👍')