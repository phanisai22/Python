from enemy import Enemy, Troll, Vampire, VampireKing

loki_king = VampireKing('loki')
print(loki_king)

while loki_king.alive:
    loki_king.take_damage(40)
    print(loki_king)

