#Matheus reis

import random

def main():
    # Atributos do aventureiro
    adv_life, adv_attack, adv_defense = 100, random.randint(10, 20), random.randint(1, 5)

    # Atributos do monstro
    mons_life, mons_attack = random.randint(60, 80), random.randint(20, 30)

    print("Aventureiro - Vida:", adv_life, "Ataque:", adv_attack, "Defesa:", adv_defense)
    print("Monstro - Vida:", mons_life, "Ataque:", mons_attack)

    round_num = 1

    # Loop do combate
    while adv_life > 0 and mons_life > 0:
        print("\nRodada", round_num)

        # Aventureiro ataca o monstro
        adv_damage = random.randint(1, adv_attack)
        mons_life -= adv_damage
        print("O aventureiro ataca o monstro causando", adv_damage, "de dano. Vida do monstro:", mons_life)

        # Verifica se o monstro morreu
        if mons_life <= 0:
            print("O monstro morreu!")
            break

        # Monstro ataca o aventureiro
        mons_damage = random.randint(1, mons_attack) - adv_defense
        if mons_damage < 0:
            mons_damage = 0
        adv_life -= mons_damage
        print("O monstro ataca o aventureiro causando", mons_damage, "de dano. Vida do aventureiro:", adv_life)

        # Verifica se o aventureiro morreu
        if adv_life <= 0:
            print("O aventureiro morreu!")
            break

        round_num += 1

    # Exibe os atributos finais
    print("\nAtributos finais do aventureiro - Vida:", adv_life, "Ataque:", adv_attack, "Defesa:", adv_defense)
    print("Atributos finais do monstro - Vida:", mons_life, "Ataque:", mons_attack)

if __name__ == "__main__":
    main()
