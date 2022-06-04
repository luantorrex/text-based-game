from models import items


class MainCharacter:
    health = 10
    mana = 1
    strength = 1
    constitution = 1
    dexterity = 1
    intelligence = 1
    wisdow = 1
    charisma = 1
    helmet = items.Helmet
    armor = items.Armor
    legs = items.Legs
    weapon = items.Weapon
    boots = items.Boots
    shield = items.Shield
    backpack = []
    capacity = 0.0


class Npc:
    # Lista de itens dos npc negociantes
    items = []
    # Gold no NPC, para comprar itens do jogador.
    gold = 0
    # Rate de pagamento em compra de itens.
    pay_rate = 0.0
    dialogs = {}