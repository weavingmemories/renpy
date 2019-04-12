# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Em")

default truth = False

# The game starts here.

label start:

    image em happy = "emhappy1.png"
    image em happy2 = "emhappy2.png"
    image em sad = "emsad.png"
    image em sad2 = "emsad2.png"
    image em neutral = "emneutral.png"
    image em neutral2 = "emneutral2.png"

    scene bg

    "In the end... maybe things will be alright."
    "Let's take life one day at a time."

label credits:
    scene black with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend

label aftermath:

    show frame1 with dissolve
    with Pause(3)
    show frame2 with dissolve
    with Pause(3)
    show frame3 with dissolve
    with Pause(3)
    show frame4 with dissolve
    with Pause(3)

    scene bg

## Slow fade in. First you ARE the person, then it slowly zooms out until you see their whole back. They slowly turn around and are shocked to see you.

    show em neutral with dissolve

    e "Who are you?"

    show em neutral2 with dissolve

    e "Wait, how long have you been here?"
    e "Have you been following me?"
    e "For how long?"

    menu:
     "For this whole... game, I guess?":
        jump game

     "I wasn't following you! I WAS you!":
        jump deny

    label game:
        $ truth = True
    show em neutral2 with dissolve

    e "Wait, you've been with me all that time?"
    e "For this whole week?"

    show em neutral with dissolve

    e "... I guess I had a feeling that was true."

    show em happy with dissolve

    e "Thanks for telling me the truth."

    show em neutral with dissolve

    e "Even if that's still really creepy."

    jump after1

    label deny:

    show em sad with dissolve

    e "What? That doesn't make any sense!"
    e "Even if this is a... game or whatever..."
    e "You'll never be me."

    show em neutral with dissolve

    e "I'm. Me."
    e "I had a feeling someone was following me, anyway."
    e "So I guess it's relieving to see I was right."

    label after1:

    e "Since you've apparently been around so long, at least tell me your name."

    $ name = renpy.input("My name is...")
    $ name = name.strip()

    e "Okay, [name]."
    e "This is all... I don't really know how to react."
    if truth:
        show em neutral2 with dissolve
        e "At least you're being forward about this."

    e "..."
    e "Um..."

    menu:
        "This is pretty awkward. I understand that you're anxious.":
            jump better
        "I know what you're thinking. I've had access to your innermost thoughts. It's okay.":
            jump worse

label better:
    show em sad2 with dissolve

    e "No, [name], you don't understand me."
    e "I guess you know a bit about me from following me all this time, that's true."
    e "But you aren't me."
    jump after2

label worse:

    show em neutral2 with dissolve

    e "No, you don't."
    e "Maybe you've worn me as a skin suit."

    show em sad2 with dissolve

    e "Maybe you've somehow read my mind..."
    e "Maybe you've walked in my shoes."

label after2:

    show em sad with dissolve

    e "You're going to leave at some point, though, aren't you?"
    e "You're not going to be me forever."
    e "You're going to go back to your own life..."

    show em sad2 with dissolve

    e "Wherever you live..."
    e "And you're going to do whatever you do with your life."

    show em sad with dissolve

    e "And then you'll forget, [name]. Because you don't have to deal with this."
    e "Deal with me. Deal with my issues."
    e "My anxiety. My gender questioning. My sexual orientation."

menu:
    "I'm sorry... I guess not.":
        jump defeatist
    "What can I do?":
        jump takingaction

##[Two options: one more defeatist and one asking what can i do?]
label defeatist:

    "I guess I can't do anything."
    show em sad2 with dissolve
    e "I guess not... really."
    e "No instant gratification, anyway."
    show em neutral with dissolve
    e "But maybe you should ask people if they need anything."
    e "Just because you might not live with these things doesn't mean you can't help others."

label takingaction:

    "What can I do, then?"

    show em neutral2 with dissolve

    e "Wha...?"
    "Well... I want to help."

    show em happy with dissolve

    e "... oh... um..."

    show em neutral with dissolve

    e "I guess... I mean, I don't know. I guess you could always ask me if you have any questions."
    e "Or try to keep yourself informed."

    show em neutral2 with dissolve

    e "Using what you know to be a better person to others, or to help them speak out."

default anxiety = True
default gender = True
default orientation = True

menu discussiontopics:
    "What is anxiety like?" if anxiety:
        $ anxiety = False
        show em sad with dissolve
        e "Anxiety is difficult."
        e "I mean... I guess I can't speak for everyone, but this is my experience."
        e "I always feel vaguely uncomfortable."
        show em sad2 with dissolve
        e "I consciously have to remind myself to breathe a lot."
        e "I always double guess myself every time I have a social interaction and I let myself go."
        e "Forget presenting things. My heart pounds in my throat and I get nausea."
        show em neutral with dissolve
        e "I don't think I'm ever doing enough. But then I'm not motivated by that... it just sends me into a self fulfilling prophecy."
        e "Sometimes, for days on end, I'm not hungry because I'm just always on edge."
        e "And if I force myself to eat, I feel nauseous."
        show em sad with dissolve
        e "... Though anxiety is different for everyone. I'm lucky I at least haven't experienced a panic attack."
        e "I've seen a friend have one, and I felt awful."
        e "... I still have to remind myself that my own anxiety is valid, since a lot of people can have it to the point it can be dehabilitating."
        show em sad2 with dissolve
        e "I've seen it."
        show em sad with dissolve
        e "..."
        jump discussiontopics
    "What about gender?" if gender:
        $ gender = False
        show em neutral with dissolve
        e "Gender is... confusing."
        e "I feel really nebulous about it, you know?"
        e "Like... I've always gone along with being identified as 'female' because... well..."
        show em neutral2 with dissolve
        e "I've never had major dysphoria or anything like that!"
        show em neutral with dissolve
        e "But I've done a lot of things that... I realize now might be pointing me somewhere else."
        e "When I was a kid, I loved shaving with my dad. I did it all the time."
        e "Growing up, as a teenager, I started demanding to get my hair cut shorter and shorter."
        e "First at my shoulders, then into a longer bob. I also preferred the men's section of most stores."
        e "I bought a suit for a costume... and found myself really liking it, even wearing it for one of our formal dances."
        e "For a short period of time, I tried growing my hair out and wearing dresses and make up, but..."
        show em sad with dissolve
        e "It felt really difficult to do. I couldn't keep up with it."
        e "So here I am now, I guess. Still always anxiously wanting to step into the men's section..."
        e "...and thinking I'd like to have a flat chest and long legs and a bit of facial hair, but it doesn't keep me up at night."
        show em sad2 with dissolve
        e "But I don't really know if that's why I'm not explicitly happy either, you know?"
        show em neutral with dissolve
        e "I've identified as nonbinary to a handful of friends for a couple of years now, since I'm not sure enough yet to come out openly."
        e "Am I a man? A woman? None of the above?"
        e "It's a journey of discovery, I guess."
        show em neutral2 with dissolve
        e "Everyone experiences gender differently, though."
        e "I definitely think it's worth asking people about their experiences... but only if they want to talk about it."
        e "After all, they don't have to educate you."
        e "There are lots of online resources to learn about gender stuff too."
        show em happy2 with dissolve
        e "Yay for the internet?"
        jump discussiontopics
    "What's your view on your orientation?" if orientation:
        $ orientation = False
        show em neutral with dissolve
        e "Realizing I was bisexual was a bit of a confusing process."
        e "I initially thought I was a lesbian. I came out to one of my parents, and they told me that was impossible."
        e "I knew I definitely had romantic feelings towards women, though."
        e "I never broached it again publicly until much more recently. I had relationships with guys, so I knew I wasn't particularly against that either."
        show em neutral2 with dissolve
        e "But I knew I also liked girls."
        e "I identified as pansexual for a bit, which is technically how I think I identify?"
        e "Although bisexual was a much more accessible term, so I stuck to that. I also don't think bisexuality is limited to just two."
        show em sad with dissolve
        e "There's a lot of awful stereotypes against all kinds of LGBT people, though."
        e "Bi is often seen as either greedy or indecisive."
        show em neutral with dissolve
        e "I actually am pretty indecisive."
        show em happy with dissolve
        e "But I know it's related much more to my anxiety than my sexuality, haha."
        jump discussiontopics
    "Okay. I won't ask any more.":
        jump after3

label after3:
    show em neutral with dissolve
    e "That's alright."
    e "... Sorry if I was kind of wary."
    e "It's weird, you know?"
    e "Being followed like that."
    show em happy with dissolve
    e "But I'm glad I noticed you before you just left."
    e "It's okay that you might not relate or be like me."
    show em neutral2 with dissolve
    e "..."
    e "In the end, we're just fellow people trying to get by."
    e "Maybe you don't have mental illnesses, or you're straight, or cisgendered."
    show em neutral with dissolve
    e "That's okay."
    show em neutral2 with dissolve
    e "But... I hope you don't think this is like, your act of kindness for the day, or anything."
    e "It's always good to keep learning. You don't have to stop here."
    show em happy2 with dissolve
    e "If enough people actually tried to be informed and care, we could make a real change, you know?"

label credits2:
    scene black with dissolve
    show therealend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide therealend

    # This ends the game.

    return

init:
    image theend = Text("{size=80}The End", text_align=0.5)
    image therealend = Text("{size=80}The (real) End\n", text_align=0.5)
