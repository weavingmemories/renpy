# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Em")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    "[Maybe things will be alright.]"

## Fade to black. Credits roll.

## Slow fade in. First you ARE the person, then it slowly zooms out until you see their whole back. They slowly turn around and are shocked to see you.

    e "Who are you?"
    e "Wait, how long have you been here?"
    e "Have you been following me?"

##[Try to explain.]

    e "For how long?"
    e "Wait, you’ve been with me all that time?"
    e "For this whole week?"

##[Yes, and it’s okay. I know you’re anxious right now. I understand.]

    e "No, you don’t understand me."
    e "I guess you know a bit about me from following me all this time, that’s true."
    e "But you aren’t me."

##[I’ve been you. I’ve had access to your innermost thoughts. I understand.]

    e "No-- you don’t."
    e "Maybe you’ve worn me as a skin suit-"
    e "Maybe you’ve somehow read my mind-"
    e "Maybe you’ve walked in my shoes."
    e "But you’re going to leave at some point, aren’t you?"
    e "You’re not going to be me forever."
    e "You’re going to go back to your own life,"
    e "Wherever you live,"
    e "And you’re going to do whatever you do with your life."

    e "And then you’ll forget. Because you don’t have to deal with this."
    e "Deal with me. Deal with my issues."
    e "My anxiety. My gender questioning. My sexual orientation."

##[Two options: one more defeatist and one asking what can i do?]

##[What can I do, then?]
##(They look surprised.)
##[I want to help.]

    e "I guess… I mean, I don’t know. I guess you could always ask me if you have any questions."
    e "Or try to keep yourself informed."
    e "Using what you know to be a better person to others, or to help them speak out."

##[ a) Tell me about your anxiety.
##b) Tell me about your gender questioning.
##c) Tell me about your sexual orientation.
##If_talked about one:
##d) Okay. I won’t ask any more.]

##a)
    e "Anxiety is difficult."
    e "I mean-- I guess I can’t speak for everyone, but this is my experience."
    e "I always feel vaguely uncomfortable."
    e "I consciously have to remind myself to breathe a lot."
    e "I always double guess myself every time I have a social interaction and I ‘let myself go’."
    e "Forget presenting things. My heart pounds in my throat and I get nausea."
    e "I don’t think I’m ever doing enough. But then I’m not motivated by that- it just sends me into a self-fulfilling prophecy."
    e "Sometimes, for days on end, I’m not hungry because I’m just always on edge."
    e "And if I force myself to eat, I feel nauseous."
    e "… Though anxiety is different for everyone. I’m lucky I at least haven’t experienced a panic attack."
    e "I’ve seen a friend have one, and I felt awful."
    e "… I still have to remind myself that my own anxiety is valid- since a lot of people can have it to the point it can be dehabilitating."
    e "I’ve seen it."
    e "…"

b) Gender is… confusing.
I feel really nebulous about it, you know?
Like-- I’ve always gone along with being identified as ‘female’ because-- well-- I’ve never had major dysphoria or anything like that!
But I’ve done a lot of things that-- I realize now might be pointing me somewhere else.
When I was a kid, I loved shaving with my dad. I did it all the time.
Growing up, as a teenager, I started demanding to get my hair cut shorter and shorter. First at my shoulders, then into a longer bob. I also preferred the men’s section of most stores. I bought a suit for a costume-- and found myself really liking it, even wearing it for one of our formal dances.
For a short period of time, I tried growing my hair out and wearing dresses and make up, but… it felt really difficult to do. I couldn’t keep up with it.
So here I am now, I guess. Still always anxiously wanting to step into the men’s section, and thinking I’d like to have a flat chest and long legs and a bit of facial hair, but it doesn’t keep me up at night.
But I don’t really know if that’s why I’m not explicitly happy either, you know?
I’ve identified as nonbinary to a handful of friends for a couple of years now, since I’m not sure enough yet to come out openly.
Am I a man? A woman?
It’s a journey of discovery, I guess.
Everyone experiences gender differently, though.
I definitely think it’s worth asking people about their experiences-- but only if they want to talk about it.
After all, they don’t have to educate you.
There are lots of online resources to learn about gender stuff too.
Yay for the internet?

c) Realizing I was bisexual was a bit of a confusing process.
I initially thought I was a lesbian. I came out to one of my parents, and they told me that was impossible. I knew I definitely had romantic feelings towards women, though.
I never broached it again publicly until much more recently. I had relationships with guys, so I knew I wasn’t particularly against that either.
But I knew I also liked girls.
I identified as pansexual for a bit, which is technically how I think I identify? Although bisexual was a much more accessible term, so I stuck to that. I also don’t think bisexuality is limited to just two.
There’s a lot of awful stereotypes against all kinds of LGBT people, though.
Bi is often seen as either greedy or indecisive.
I actually am pretty indecisive.
But I know it’s related much more to my anxiety than my sexuality, haha.

d)

That’s alright.
… Sorry if I was kind of wary.
It’s weird, you know?
Being followed like that.
But I’m glad I noticed you before you just left.
It’s okay that you might not relate or be like me.
…
In the end, we’re just fellow people trying to get by.
Maybe you don’t have mental illnesses, or you’re straight, or cisgendered.
That’s okay.
But… I hope you don’t think this is like, your act of kindness for the day, or anything.
It’s always good to keep learning. You don’t have to stop here.
If enough people actually tried to be informed and care, we could make a real change, you know?


    # This ends the game.

    return
