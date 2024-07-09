# Text Fighter 2

A new, better version of my original 'text fighter'. Now uses classes and object oriented programming to create a Pokemon style fighter.
You can create your own fighters, and invent your own moves. Use the Battle(player,enemy) function to face off against another fighter of your choice.

If you are lazy to read my code, here's a basic example to create your own character: 
I expect you to understand the variable names. The damage variable is the value of the move. If the movetype is Attack, it will be used as damage. If the movetype is Buff, it will increase the Fighter's attack by that value.

1. Create a variable with the class Fighter. Ignore the delay function, it is a remanant of a previous system.
```
kaydenbasic = Fighter(
    name='Kayden(Basic)',
    health=150,
    move1=Move(movetype='Buff',name='vague_reference',damage=10,chant='hey guys... (vague reference)'),
    move2=Move(movetype=['Heal','Charge'],name='Sleep',damage=20,chant="kr mimimimimi"),
    move3=Move(movetype='Ultimate',name='Unlimited Rulebook',damage=70,chant="アンリミテッドルールブック, a rule book filled with mostly exceptions."),
    move4=Move(movetype="Debuff",name="Complain",damage=10,chant="YAP YAP YAP YAP YAP"),
    delay=0,
    entry="Kayden: hello",
    win="Kayden: f*ck you",
    loss='Kayden: owie'
    )
```
