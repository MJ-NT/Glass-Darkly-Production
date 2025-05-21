challenges = [
    # Introduction story_state 0-50
    {
        "story_state": 0,
        "text": """Kinetopede. That's what the captain - the one with the hat - had called it. A clanking, perambulatory metal beast. Now, your home, for better or worse. One cannot choose one's guardian angels.

Huddled under a moth-eaten blanket, hands wrapped around a hot mug of what might charitably be described as tea, you take in your surroundings. Two soot-caked stokers rush past, barely sparing you a glance. You gaze after them. You're fairly certain that one of them was a shark. A <em>bipedal</em> shark. You give your 'tea' a long look.

<em>This is a stat challenge. You have 4 core stats: Watchful, Shadowy, Dangerous and Persuasive. The higher your level in a given stat, the more likely you are to succeed in a challenge testing that stat. You can see your current stat levels in the 'Myself' page. This challenge tests your Watchful stat.</em>""",
         "options": [
            {
                "text": """Gaze into the liquid and try to recall how you came to be here, in this metal box""",
                "stat": "watchful",
                "difficulty": 1,
                "success_text": """Images come to you slowly, tentatively, like supplicants approaching an unstable monarch. Cold stone beneath you, cracked like rimed ice. A deep, oppressive, impenetrable dark. The sudden blaze of light to dispel that dark, and the abrupt cessation of whispers within it.

Do you feel better for having remembered? An impossible question. But on balance, you feel that you would rather know than not.""",
                "failure_text": """It is uncomfortable to remember. There is a pressure that builds behind your eyes as you insist upon it. A slow trickle of blood forms at the corner of your mouth. You wipe it away, perturbed.""",
                "next_state_success": 10,
                "next_state_failure": 10,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 5
            }
        ]
    },

    {
        "story_state": 10,
        "text": """<em>Success brings Apprehensions, the summation of knowledge gained. But failure, too, can be instructive. Put simply, you gain Apprehensions by both passing and failing challenges. Success awards more Apprehensions than failure in a challenge, and some challenges award more than others. You can see your current number of Apprehensions and spend them to improve your stats in the 'Myself' page.</em>.

You shake your head free of errant reminiscence and once again cast your gaze about. Down the other end of the hold, past shelves groaning under the weight of a miscellany of open crates, each stamped with 'Hextall' - whatever that is -  a swabbie listlessly pushes a mop around the deck.

As you begin to surreptitiously decant your cup into a nearby urn, a sudden impact rocks the locomotive, and you are thrown to the floor. Wrestling with the blanket, you hear muffled shouts from the upper deck, and catch the voice of the captain, rising above the din: "All hands on deck! Gunners to stations!  Fire up the Scuttlers!". The kinetopede jerks into rocking motion, and you feel the familiar pull of a sudden acceleration.

Finally extricating yourself from the blanket, you haul yourself up and stumble in the direction of the upper deck, joining the dazed swabbie at the foot of the stairs. They had picked you from the floor, plucked from the clutches of dehydration and madness, and now you were going to die anyway. The world is truly unfair.

The kinetopede lists dangerously to the left and you lurch towards a porthole, gazing out into the dark, where the flash of cannonfire briefly illuminates another vessel. You turn. The swabbie, a young man with a wispy beard, blinks blearily back at you.

<em>However great you grow, some challenges will always be unanswerable. Take heart in your coming failure that this challenge, at least, you could never meet.</em>""",
        "options": [
            {
                "text": """(Pull the swabbie out of the crossfire).""",
                "stat": "dangerous",
                "difficulty": 1000,
                "success_text": """Well done, this should be impossible!

Unfortunately, in pushing the swabbie out of the line of fire, you took a cannon ball in your chest. What rotten luck, eh?""",
                "failure_text": """You saw the flash too late, heard the thunder of the cannon too late. The shot tears into the hull and passes clean through the other side.

There is no scream. One moment the swabbie is there, the next he is gone.

The darkness howls outside the kinetopede. Some thought rises from deep within your mind, a kraken rushing to the surface.

<em>It is hungry</em>.
""",
                "next_state_success": 50,
                "next_state_failure": 50,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 1,
                "menace_change_success": 100,
                "menace_change_failure": 25
            },
        ]
    },

    {
        "story_state": 50,
        "text": """<em>Not all injuries are visible, nor all threats tangible. Menace is an abstract representation of the travails that you contend with. Facing threats to your bodily person, your sanity, or, gods forbid, your sartorial integrity, may increase your Menace level should you fail the challenge (and, occasionally, when you succeed). Menace, like your other stats, can be found in the 'Myself' page.</em>.

You remain, quite remarkably, unscathed, although it will be a long time before you can forget the swabbie's face.

You turn from the yawning tear in the hull and blunder dazedly up the stairs. The upper deck is a chaos of smoke and bodies. The air is filled with the nostril-stinging scent of gunpowder and the crackle of small arms fire. You collide with someone. It's the captain - the one with the hat. She swivels to catch your arm as a fresh barrage hits the kinetopede. Flames begin to lick across the deck. The captain, wild-eyed and bleeding freely from a gash in her side, presses what looks like a small music box into your hands and leans in close, almost screaming into your ear.

"Visitant! Take this and keep it safe. Look for me in the Ministry. Five days. And don't speak to the Governor's Men!"

With those cryptic words, she removes a silver-framed mirror from her pocket and, without so much as a word of warning, smashes it against your forehead.

<em>Remember that you can always spend your available Apprehensions on the 'Myself' page to improve your stats. Try it now and see how your chances of success change. Or don't, and risk a minor faux pas!</em> """,
        "options": [
            {
                "text": "Accept the situation with equanimity",
                "stat": "persuasive",
                "difficulty": 1,
                "success_text": """There is much you do not know about this world. Perhaps it is customary here to break a mirror over the head of a valued friend? Perhaps you are making inroads to becoming such a friend? Perhaps you are simply in shock. In any case, what follows next serves to put it from your mind.""",
                "failure_text": """You can't help but allow a look of reproach to cross your features. Is she hurt? Well then, perhaps she shouldn't go around breaking mirrors over others' heads.

You have little time to ponder this, however, as the world around you distorts and shatters.""",
                "next_state_success": 100,
                "next_state_failure": 100,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 5
            },
        ]
    },

 # Mirrorwise Transition 1 story_state 100
    {
        "story_state": 100,
        "text": """You fall. Through kaleidoscopic brilliance, past countless gilded frames and snapshot tableaux: A vast gothic sprawl of a city, great airborne sailing ships tethered like bunting to its spires. Laughing fishermen trawling gravestones from a meandering river. A dizzyingly tall cascade of pale water, equally pale figures swooping dreamlike within it. A ten-mile-high totem, draped in a cloak of a million cawing crows.

You cast about for reason within this ever-shifting madness, stuffing the music box into your pocket before it can be knocked from your grasp. Your heartbeat thunders, impossibly loud, as you attempt to still your panicking mind.

<em>Sometimes, fate will offer multiple approaches to tackling a challenge. These may test different stats, or sometimes the same stat at a different difficulty level. More difficult challenges may offer more narrative or mechanical benefits.</em>""",
        "options": [
            {
                "text": """Decipher some pattern in the swirling of the pale figures.""",
                "stat": "watchful",
                "difficulty": 2,
                "success_text": """Through snatches of images, understanding dawns, building piecemeal from the morass of wheeling and diving figures. They are spirits, you realise. Your mind is guided by these psychopomps to a plain-framed mirror.""",
                "failure_text": """The realisation strikes you: these are ghosts. Ducking, diving, like swallows after flies at sunset. Are they trapped here? Could this be your fate, too?

You tumble towards a plain-framed mirror.""",
                "next_state_success": 101,
                "next_state_failure": 101,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": -25,
                "menace_change_failure": -15
            },
            {
                "text": """A ship sweeps in front of you, sails filling with a non-existent breeze. Slip under its hull; let it guide you.""",
                "stat": "shadowy",
                "difficulty": 2,
                "success_text": """You glide into its slipstream and down, latching onto the underside like a particularly stealthy barnacle. You are not alone here. Above, a child on board is crying for their doll. Next to you, a clown-faced puppet grins.

As the ship passes over a wall of silvered metal, you detach, diving through a plain-framed mirror.""",
                "failure_text": """Shouts come from the deck as you approach. A hunched, avian creature has raised the hue and cry from the rigging. Indistinct figures with large poles appear on the sides to fend you off, and send you careening towards a plain-framed mirror below.""",
                "next_state_success": 101,
                "next_state_failure": 101,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": -25,
                "menace_change_failure": -15
            },
            {
                "text": """Reach to snatch the titan's cloak. Fly with a thousand wings!""",
                "stat": "dangerous",
                "difficulty": 2,
                "success_text": """Here, in the irreality of this plunging vortex of mirrors, nothing could seem more natural. You snap out a hand and catch not the cloak, but a crow from within it. It struggles in your grasp; beats its wings; steers you inexorably towards a plain-framed mirror.""",
                "failure_text": """You reach for the cloak. A thousand thousand mad gimlet eyes stare at your outstretched arm.

<em>Food</em>.

You tumble away, clutching the bloodied stump where your arm used to be. You watch in fascinated horror as it regrows, like a new bud, sprouting from your elbow. You feel a crunch as you crash through a plain-framed mirror.""",
                "next_state_success": 101,
                "next_state_failure": 101,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": -25,
                "menace_change_failure": -15
            },
            {
                "text": """There! Your reflection stands by the bank of the river, line in hand, sharing some private joke with another fisherman. Ask it - you - for directions.""",
                "stat": "persuasive",
                "difficulty": 2,
                "success_text": """Your reflection nods and winks, gesturing to a plain-framed mirror to your right. You turn and propel yourself towards it, bracing for impact.""",
                "failure_text": """Your reflection turns and holds up a tombstone - it's yours! Theirs! Whatever - you spiral away towards a plain-framed mirror. Your reflection smiles.""",
                "next_state_success": 101,
                "next_state_failure": 101,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": -25,
                "menace_change_failure": -15
            }
        ]
    },

# Ghoulwatch story_state 101-140
    {
        "story_state": 101,
        "text": """Your exit from the mirror is decidedly inelegant. Whatever designs on elegance you may have had are forfeit the moment you meet with a wall of wood and dirt in a sudden, painful collision.

It takes you a moment to get your bearings, as you gingerly check your nose for signs of breakage. It seems functional, at least, but your nostrils are filled with the rich scent of soil, and… pine? You shift, feeling fragments of the mirror digging into your back as you do so. You flex your limbs.

<em>Hmm</em>.

You are in an enclosed space. Perhaps six feet long. Two, or perhaps two-and-a-half feet wide, and a foot or so tall.

<em>Ah</em>.

The unhappy realisation slopes abashedly into your mind: you are buried alive.

You have to hope that this is not what the captain intended for you. You feel the music box, miraculously intact, still in your pocket. You leave it there: you have more immediate concerns.""",
         "options": [
            {
                "text": """Wait. Listen to the slow earth.""",
                "stat": "watchful",
                "difficulty": 3,
                "success_text": """With a supreme effort, you calm your rising panic, slowing your breathing until you can almost hear the earthworms shifting in the soil around the coffin. You place one hand on the lid; feel your heartbeat pulse under your fingertips. Beneath you - far beneath - you fancy that you can hear another heart, beating in sympathy with yours.

You take a deep breath.""",
                "failure_text": """Try as you might, you cannot quell the rising panic building inside you. Your breaths come short and shallow. Your heartbeat thunders in your ears.

<em>A-gain</em>
<em>A-gain</em>
<em>A-gain</em>""",
                "next_state_success": 105,
                "next_state_failure": 105,
                "apprehension_change_success": 3,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 20
            },
            {
                "text": """Call for help.""",
                "stat": "persuasive",
                "difficulty": 2,
                "success_text": """Your howls of protest are answered, eventually, as you hear the soil shifting above you; a spade hitting the lid of the coffin, loosing a shower of gravedirt into your face.""",
                "failure_text": """You shout until your throat is raw, and then you shout some more. Nothing happens. This place is as silent as, well, the grave.""",
                "next_state_success": 110,
                "next_state_failure": 105,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            }
        ]
    },

    {
        "story_state": 105,
        "text": """Are you going to die down here, deep in the earth?

Not if you can help it.""",
         "options": [
            {
                "text": """Shout. Make thunder of it. Put Stentor to shame.""",
                "stat": "persuasive",
                "difficulty": 2,
                "success_text": """You curse and scream. You rail against every god you know, and blaspheme any others that might be listening for good measure.

Your howls of protest are answered, eventually, as you hear the soil shifting above you; a spade hitting the lid of the coffin, loosing a shower of gravedirt into your face.""",
                "failure_text": """You curse and scream. You rail against every god you know, and blaspheme any others that might be listening for good measure.

But it's not enough.

If any god is listening, they do so only to mock you. You can hear your heart, joined in chorus by others here in the dark earth.

<em>A-gain</em>
<em>A-gain</em>
<em>A-gain</em>""",
                "next_state_success": 110,
                "next_state_failure": 110,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 110,
        "text": """The lid is prised open. Gnarled fingers pluck you from the coffin and into a vaulted catacomb, illuminated by greenish lantern light: glow-worms, writhing against glass jars.

Your saviour is a peculiar sort. A gangling figure, spindle-armed within a battered overcoat that threatens to engulf his entire frame. He leers unpleasantly at you, flesh hanging in jowls that are looser than mere age would account for.

You engage in a spirited debate over your comparative state of vitality. He is a ghoul, he says, and a caretaker of the dead that prefer to remain that way. Did you perhaps get cold feet? Decide that life had a little more to offer you? How presumptuous, he says. You have an easy rebuttal: you are, in fact, not dead.

It takes a number of strong words, but he eventually agrees, with some reluctance, that you don't <em>seem</em> dead. And that's good enough for him.

"Yer in Gravespite, or underneath it" he informs you with a rotten-toothed grin. Now that he's been assured that you're not a member of the ungrateful dead, he is quite chipper.

Gravespite, it transpires, is a colony of the dead. And this, a lower floor of the settlement, housed in a great sunken mausoleum, of which this catacomb is but a smaller part, should normally be inaccessible to the living. No, the ghoul doesn't know where the Ministry is. He has never heard of the Governor's Men. He is cheerfully unhelpful on the subject of your next steps, save for one piece of advice.

"You came through the Mirrorwise, yeah? Best find another mirror then".

So <em>that's</em> what you'd call the kaleidoscopic nightmare you just passed through. Oh well, it's heartening to know that you'll have to go through it again, you wouldn't want to get <em>too</em> comfortable in this hellhole.

The ghoul gestures to a worn stairway, a horrible smile still settled on his receded lips. You totter unsteadily over, shedding gravedirt as you go, and make your way up it. After a dozen steps or so, you emerge into a sprawling subterranean necropolis, bathed in the sickly green luminescence of a thousand glow-worm lanterns. It is, fittingly, deathly quiet.

Now then: if you were a mirror, where would you be?

Your gaze fixes on a clocktower, half-buried perhaps half a mile away. There is no obvious pathway there.""",
        "options": [
            {
                "text": """You need perspective. Climb the spire of a nearby sepulchre.""",
                "stat": "dangerous",
                "difficulty": 3,
                "success_text": """This place, though dedicated to decay, was built to last. You fly up the marble edifice, finding handholds and footholds in the statue-work of the long-dead. Soon, you arrive at a vantage point.""",
                "failure_text": """You are not the only one to have attempted this climb, if the bones littered around the base of the tomb are anything to go by. How many others were once trapped here, like you? How many others broke their bodies in the fall?

You make slow progress, but progress nonetheless, finally arriving, somewhat shaken, at a vantage point.""",
                "next_state_success": 120,
                "next_state_failure": 120,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
            {
                "text": """You need a guide. Knock on the door of one of the nearby tombs.""",
                "stat": "persuasive",
                "difficulty": 3,
                "success_text": """You approach a likely-looking tomb and begin to knock politely but insistently upon the heavy stone door.

Your summons are eventually met by a stooped gentleman in faded finery. He invites you in with surprising cordiality, his voice far smoother than you would expect from the long-dead. But then, it is not a topic you had given much thought until now.

"We were preparing dinner" he intones, beckoning you to follow him down a stairway. "Join us, won't you?" """,
                "failure_text": """You approach a likely-looking tomb and begin to knock politely but insistently upon the heavy stone door.

Muffled shouts from inside tell you exactly where you can go, in the least helpful sense of the expression. You beat a hasty retreat, out into the endless rows of headstones.""",
                "next_state_success": 130,
                "next_state_failure": 135,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 0
            }
        ]
    },

    {
        "story_state": 120,
        "text": """From this eyrie, all of the vast graveyard is laid out below you. A hundred different religious symbols compete for dominance on the spires of the grander tombs. The battle is mirrored on the humbler headstones, set in haphazard rows. A few designs are repeated again and again: a serpent; a distressingly-bulging pyramid; a swine-head; a clock. Perhaps this clocktower is the grandest tomb of them all? It dominates the opposing wall from your position. In front of it, a sea of writhing glow-worms provides undulating illumination.

There is another tomb, almost as large, halfway between you and the clocktower. You'll make that your next marker, you decide, and deal with the sea of worms when you come to it.

But how to get there?""",
        "options": [
            {
                "text": """Map out the way from this vantage point.""",
                "stat": "watchful",
                "difficulty": 4,
                "success_text": """You trace the winding tombways, the snickets and ginnels between each crypt and catacomb, in the dust on the spire.

You spend a moment to commit it to memory, then pick your way back down and walk the streets, guided by your mind's-eye map.

You come upon it sooner than expected: the low rise of white marble.""",
                "failure_text": """You trace the winding tombways, the snickets and ginnels between each crypt and catacomb, in the dust on the spire.

You gaze at it for a long moment, attempting to commit it to memory, then pick your way back down to the streets.

But they are different. Shifted? Changed, somehow? You soon realise that you are hopelessly lost.""",
                "next_state_success": 140,
                "next_state_failure": 125,
                "apprehension_change_success": 3,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 20
            },
            {
                "text": """There must be some hidden configuration to this matryoshka necropolis. Think: what is <em>not</em> being shown?""",
                "stat": "shadowy",
                "difficulty": 4,
                "success_text": """There is a tracery of a pattern here, written in the tombs viewed from above. A maddening geometry, but you have the key, you're sure.

You pick your way back down to the streets, then breathe deeply, and close your eyes. The pattern burns, incarnadine on the back of your eyelids. You let your feet guide you, until you bump up against a cold stone door. You smile: you have arrived.""",
                "failure_text": """There is a tracery of a pattern here, written in the tombs viewed from above. A maddening geometry, if only you could keep it in your head.

You pick your way back down to the streets, then press on, reaching for the thread in your mind's eye. But it is elusive, whipping around every corner, snaking through lintels and skulking in neighbouring doorways, never lingering long enough for you to get your bearings. Eventually, you are forced to admit that you are lost.""",
                "next_state_success": 140,
                "next_state_failure": 125,
                "apprehension_change_success": 3,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 20
            }
        ]
    },

    {
        "story_state": 125,
        "text": """You wander the streets, searching for any sign of the tomb you had spotted from the tower. It is quiet, save for the soft sound of your footfalls in the dust and gravedirt.

Eventually, you see it, looming above a row of headstones presumably marking lesser lives. It squats on a low rise, almost accusatory in its ostentation.

Indeed, as you approach, you can feel a weight of judgement pressing against you, emanating from the tomb. How dare you approach? Are you not better suited to these lowly satellite graves?""",
        "options": [
            {
                "text": """The stone is right. You are nobody. You are not a threat. Hide your smile.""",
                "stat": "shadowy",
                "difficulty": 4,
                "success_text": """No, not you. You are an unworthy supplicant, happy to simply share a reality with the unfeeling stone. Your smile widens as you make the final few steps to the mausoleum.""",
                "failure_text": """It is not until the final few paces that your deception is discovered. The full weight of wrathful indignation pushes down upon you, but you will not be swayed. You push forwards, ignoring the pain; the blood that pools in your mouth.""",
                "next_state_success": 140,
                "next_state_failure": 140,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
            {
                "text": """You will not bow to a tomb. What right have the dead to judge you?""",
                "stat": "persuasive",
                "difficulty": 5,
                "success_text": """The stone does not expect this. You march towards the mausoleum with purpose, throwing off what feeble attempts the stone makes to penetrate your mind. The roar in your ears recedes to a sullen hum as you trip up the stairs to the door.""",
                "failure_text": """The weight intensifies around you, but you march on, fuelled by sheer force of will. It is a struggle though. The final few steps sap your strength, but you will not be deterred.""",
                "next_state_success": 140,
                "next_state_failure": 140,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            }
        ]
    },

    {
        "story_state": 130,
        "text": """The gentleman leads you down a winding stair into a large dining room, a long table piled high with a mouldering feast. Seated on wing-backed chairs all around the table, corpses recline, slumped against the stained velvet. They are very much <em>not</em> alive. 

Your host shuffles into a seat at the head of the table, smiling with rheumy amiability around the room. Empty sockets stare back.

"Well, tuck in!" urges the gentleman, offering you a plate crawling with maggots. You make a heroic attempt at a smile.

"And, terribly sorry, what was it that you needed?" """,
        "options": [
            {
                "text": """You need answers. How can you reach the clocktower?""",
                "stat": "Persuasive",
                "difficulty": 4,
                "success_text": """Your host looks at your plate expectantly before answering.

You have come this far. You grit your teeth and swallow a mouthful of writhing grave-worms. He beams at you.

"Well, to get there you'll need to go through the mausoleum of old Abraham Croaker, in the centre of the necropolis. Prime spot", he adds, conspiratorially.

And how does one reach said mausoleum?

It is simple, he says. And indeed it appears to be so. He even offers you a map. Not such a bad sort, in the end.

A few minutes and many hasty apologies later, you politely extricate yourself from his hospitality. A few more minutes later, you find yourself outside the mausoleum of this 'Abraham Croaker'.""",
                "failure_text": """Your host looks at your plate expectantly before answering.

You have come this far. You grit your teeth and swallow a mouthful of writhing grave-worms.

The world goes dark. Images flash before your eyes. A many-spired city, buckling under a sudden pressure, the masonry cracking and crumbling in one motion. A heat-haze rising from a boiling ocean. A tree laden with shining stars.

You wake with a start, the old man's cloudy eyes, full of concern, mere inches from yours. He scrambles back, apologising profusely.

The swift dispensing of information is your remedy of choice, and that, he has to hand. The clocktower is inaccessible from the necropolis proper, he says, but there is a way through the mausoleum of Abraham Croaker, at the centre of the place. He even offers a map by way of an apology.

A few minutes later, you find yourself outside the mausoleum""",
                "next_state_success": 140,
                "next_state_failure": 140,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 2,
                "menace_change_success": 0,
                "menace_change_failure": 50
            },
            {
                "text": """You need to get out of here.""",
                "stat": "shadowy",
                "difficulty": 4,
                "success_text": """You make a dramatic show of dropping your fork, ducking under the table to retrieve it. You then slip out the other side and make a dash for the door.

As it happens, you needn't have bothered with such an elaborate ruse. When you glance back at the doorway, your host is babbling happily in the general direction of your vacated chair, apparently oblivious to your absence.

You trot back up the stairs and head out into a field of headstones.""",
                "failure_text": """Your host has a wiliness that belies his decrepitude. Try as you might, you cannot manufacture an excuse to slip away, nor a distraction to facilitate a clean escape.

You do, at least, manage to avoid eating any of the food, but when you leave hours later, you are none the wiser about your next destination. You trudge out through a field of headstones.""",
                "next_state_success": 135,
                "next_state_failure": 135,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            }
        ]
    },

    {
        "story_state": 135,
        "text": """You wander, rudderless, between the gravestones for a time. Do you see your own, there? Do you see your epitaph? Is that what prompts you to return to the sepulchre?

You'd rather not say.

The cryptkeeper is stood outside the catacomb you recently vacated. He chuckles as you pass, low and dry, like dirt shaken in a tin can.""",
       "options": [
            {
                "text": """Brace yourself. Climb the spire.""",
                "stat": "dangerous",
                "difficulty": 3,
                "success_text": """This place, though dedicated to decay, was built to last. You fly up the marble edifice, finding handholds and footholds in the statue-work of the long-dead. Soon, you arrive at a vantage point.""",
                "failure_text": """You are not the only one to have attempted this climb, if the bones littered around the base of the tomb are anything to go by. How many others were once trapped here, like you? How many others broke their bodies in the fall?

You make slow progress, but progress nonetheless, finally arriving, somewhat shaken, at a vantage point.""",
                "next_state_success": 120,
                "next_state_failure": 120,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
        ]
    },

    {
        "story_state": 140,
        "text": """Outside the mausoleum, you take a deep, steadying breath. From here, you can make out the febrile glow emanating from the mass of worms before the clocktower. Their susurration is akin to a gentle sea.

You raise your fist and strike it against the door. Once. Twice. Thrice.

On the third knock, the white marble shifts, opening with terrible slowness. Behind it, a many-limbed figure stands.

Your first impression is that of a pale, moon face. Waxen, masklike, serene. A second glance reveals long, segmented limbs, folded into a torso that is more like a thorax. You dare not chance a third look.

When it speaks, it is with a pleasant, fluting voice.

"You have come for the mirror, have you not?"

It <em>is</em> a pleasant voice. It is a voice that invites trust.

You answer that indeed <em>yes</em>, you <em>have</em> come for the mirror. That you need access to the mausoleum to reach the clocktower. That you must get back home.

The creature tuts in sympathy. Of course, it says. It must be so difficult for you here, in this strange new world. Why don't you tell it more about your home?

You have a nagging feeling from deep within your brain that tells you that this would be a bad idea.""",
        "options": [
            {
                "text": """Poison the well with lies.""",
                "stat": "shadowy",
                "difficulty": 4,
                "success_text": """It wishes to nourish itself on your words? Feed it hemlock, arsenic, atropine. It will drink deep of you, and wish it had not tasted the spring.

As you speak, the creature unspools a long, butterfly proboscis, tasting the air. Two minutes later, it is spasming at your feet. You step over it and towards a stairway framed by glow-worm lanterns.""",
                "failure_text": """The words are drawn from you like pulled teeth. They rise, unbidden, from your throat as if extracted by forceps, your vocal chords contorting around the sounds. You tell it of your home, the Sun, the scent of the sea, and of the flowers in bloom. The salt sting of tears, the warmth of another's embrace. The cleansing rain and bitter heat of summer…

You awaken on the cold stone floor of the mausoleum. The creature is nowhere to be seen. glow-worms writhe in the lanterns above a set of stairs, leading down.""",
                "next_state_success": 150,
                "next_state_failure": 150,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 20
            },
            {
                "text": """Wrap your story in half-truths.""",
                "stat": "persuasive",
                "difficulty": 4,
                "success_text": """You honey your words until there is nothing of substance left. They are sickly, insubstantial. An insufficience. You befuddle and contradict, you mix metaphors with gleeful abandon, you obfuscate.

As you speak, the creature unspools a long, butterfly proboscis, tasting the air. Two minutes later, the tongue recedes into its mouth and it moves away, retreating into the shadows of the ceiling far above. You step towards a stairway framed by glow-worm lanterns.""",
                "failure_text": """The words are drawn from you like pulled teeth. They rise, unbidden, from your throat as if extracted by forceps, your vocal chords contorting around the sounds. You tell it of your home, the Sun, the scent of the sea, and of the flowers in bloom. The salt sting of tears, the warmth of another's embrace. The cleansing rain and bitter heat of summer…

You awaken on the cold stone floor of the mausoleum. The creature is nowhere to be seen. glow-worms writhe in the lanterns above a set of stairs, leading down.""",
                "next_state_success": 150,
                "next_state_failure": 150,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 20
            }
        ]
    },

 # Ghoulwatch story_state 150-199
        {
        "story_state": 150,
        "text": """You move down the greenish stair. There is an earthen passage at the bottom, the scent of the soil rich and cloying. A few paces along, you realise that you must be walking under the sea of glow-worms. You can <em>hear</em> them. Individual worms dot the tunnel at irregular intervals. A few must have made their way through the loamy earth above.

You close your mind to the noise: the unsettling, pervasive rustle of a million tiny bodies writhing in concert. One foot in front of the other. That's the way.

After a few minutes, the passageway slopes upwards in a gentle incline. You scramble the last few steps, emerging into a vast chamber, each wall dominated by the inverse side of a clock face. At the centre, three great gear trains, each traced by verdigris, stand motionless. Casting your eye upwards, you see nine bells, hanging silent in the belfry far above.

That creature had known you were looking for a mirror. Was it merely taunting you?

But then you see it. Nestled behind the middle train, half-hidden underneath the bevel gears: tarnished silver and a rusted pane.

The escapement. Of course. You allow yourself a wry smile.

It is now a question of how to extract it. The answer comes to you slowly, an unwelcome thought that slides into your mind unbidden.

<em>Pray</em>.

But you have encountered many different iconographies in this place. The clock is the most obvious answer. Does that make it the right one? You have seen the serpent, the swine-head, the pyramid. You have seen more.""",
        "options": [
            {
                "text": """The clock. Occam's razor.""",
                "stat": "watchful",
                "difficulty": 6,
                "success_text": """Two names come to you, drawn from the ether; from the damp, dark soil beneath you.

Morbazar - <em>Tick</em>

Baraphal - <em>Tock</em>

You kneel in supplication, asking for him-and-her to unbend, to allow you through the mirror. To allow you home.

Above you, the bells toll, resonant in the tower. Startled, you look up. When your gaze falls downwards again, the mirror is lying in the gravedirt in front of you.""",
                "failure_text": """Two names come to you, drawn from the ether; from the damp, dark soil beneath you.

Morbazar <emTick</em>

Baraphal <em>Tock</em>

You kneel in supplication, asking for him-and-her to unbend, to allow you through the mirror. To allow you home.

But something is terribly wrong.""",
                "next_state_success": 195,
                "next_state_failure": 160,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 30
            },
            {
                "text": """The serpent: Ouraboros; Jörmungandr; the Edenic tempter of the Original Sin.""",
                "stat": "shadowy",
                "difficulty": 6,
                "success_text": """<em>Nahash</em>

The name slithers into your mind, appropriately enough. Your vision is filled with a great coil, a gordian knot of serpents. It is ancient. It <em>hungers</em>. You are observed by a thousand ophidian eyes.

How would you feed such a creature? You make an offering of secrets of your world. The esoteric, the obscure, the anodyne, the mundane: it devours them all with equal relish.

When you finally finish your account, when your vision unclouds, the mirror lies in the gravedirt in front of you.""",
                "failure_text": """<em>Nahash</em>

The name slithers into your mind, appropriately enough. Your vision is filled with a great coil, a gordian knot of serpents. It is ancient. It <em>hungers</em>. You are observed by a thousand ophidian eyes.

How would you feed such a creature? You make an offering of secrets of your world. The esoteric, the obscure, the anodyne, the mundane: it devours them all with equal relish.

But it is not satisfied. It wishes to impart it's knowledge to <em>you</em>, too.""",
                "next_state_success": 195,
                "next_state_failure": 170,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 30
            },
            {
                "text": """The swine-head: The Erymanthian Boar. Ask it to lend you its strength.""",
                "stat": "dangerous",
                "difficulty": 6,
                "success_text": """<em>Graveddon</em>

The name comes to you with the force of a blow, and you reel as if struck. Dull, porcine eyes, glimmering with low cunning, swim in your vision.

You would kneel before the Iron Swine? Very well, it shall accept you as devotant.

There is a great wrenching noise: somewhere between the scream of tortured metal and the squeal of countless boars. When you regain your sight, the gears have been torn from their housing, and the mirror lies discarded in the gravedirt in front of you.""",
                "failure_text": """<em>Graveddon</em>

The name comes to you with the force of a blow, and you reel as if struck. Dull, porcine eyes, glimmering with low cunning, swim in your vision.

You would kneel before the Iron Swine? You are <em>unworthy</em>""",
                "next_state_success": 195,
                "next_state_failure": 180,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 30
            },
            {
                "text": """The pyramid: The Eye of Providence. There were wild theories about the nature of time in the Great Pyramids, once.""",
                "stat": "persuasive",
                "difficulty": 6,
                "success_text": """Your nostrils are immediately filled with the sweet scent of decay. You can taste it in the air: blood, metallic on the tongue.

Your vision clouds, and you close your eyes against the acrid spray of ichor. You open them again. A mountainous scab in the shape of a pyramid stands before you, one xanthous eye fixing you in its gaze.

<em>Scorthidion</em>.

The name catches in your throat. The Coagulant God.

What can you offer such a being? Your heartbeat quickens in response, your pulse jumping at your wrist and throat.

No, not blood. That is too easy, and this god clearly has an abundance of it. Knowledge shall be its medicine, and medicine its offering. You talk of the surgical advances in your world. Of a reality where the letting of blood is no longer commonplace.

The mountain observes you for a long moment. There is a noise approaching derision, and you turn as a gout of blood from a seeping wound sprays out. But when you turn back, the mirror lies in the gravedirt in front of you. You check your clothes - they are not reddened, nor stained.""",
                "failure_text": """Your nostrils are filled with the sweet scent of decay. You can taste it in the air: blood, metallic on the tongue.

Your vision clouds, and you close your eyes against the acrid spray of ichor. You open them again. A mountainous scab in the shape of a pyramid stands before you, one xanthous eye fixing you in its gaze.

<em>Scorthidion</em>.

The name catches in your throat. The Coagulant God.

What can you offer such a being? Your heartbeat quickens in response, your pulse jumping at your wrist.

No, not blood. That is too easy, and this god clearly has an abundance of it. What, then? Knowledge? A poultice or binding for its wounds?

The mountain darkens, the eye narrows. You presume to treat and label malady?""",
                "next_state_success": 195,
                "next_state_failure": 190,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 30            
}
        ]
    },

    {
        "story_state": 160,
        "text": """You are gripped by a sudden, wracking pain in your arms. You stare in horror as your veins begin to darken, green shoots emerging from under your fingernails, buds blooming into yellow. Your vision is filled with it, the colour both behind and beyond.

<em>How dare you entreaty the traitor? Cause of sorrow. Bane of wilting joy</em>.

You stumble forward, your body withering as the sunflowers take root.""",
       "options": [
            {
                "text": """Hurl yourself through the mirror, gears be damned!""",
                "stat": "dangerous",
                "difficulty": 5,
                "success_text": """You squeeze yourself through the gears, ignoring the searing pain as the flowers are ripped from your body. With a final shout, you punch through the glass, tumbling into the Mirrorwise. As soon as you enter, the yellow in your vision recedes: the flowers are gone.""",
                "failure_text": """It's no use. You urge your body to move, but you cannot. The flowers twist and twine about your head, a crown of thorns.""",
                "next_state_success": 200,
                "next_state_failure": 200,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 170,
        "text": """Forked tongues crowd your ears, a sibilant chorus of secrets you would rather not have known.

A daisy chain of hushed conversations, whispered promises, dark tales confided. Veiled threats and guileless indiscretion. Confessions: thunderous, tentative, of treason; faith; love.

They should be meaningless to you, but still they clamour and clang about your head, building in an awful crescendo.

Before you - there! The mirror hangs suspended in the coils.""",
       "options": [
            {
                "text": """Focus your mind. There is only the mirror.""",
                "stat": "persuasive",
                "difficulty": 5,
                "success_text": """The hissing voices abate, just for a moment, and you dive for the glass. As soon as you are through, the snakes fall away.""",
                "failure_text": """You reach out, and the mirror is tugged away. You fall to your knees, ears filled with the lexicographic venom. Your eyes roll back.""",
                "next_state_success": 200,
                "next_state_failure": 200,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 180,
        "text": """You dare prostrate yourself before the War Pig?

<em>Weak</em>.

You are given an education in every pain imaginable. You are beaten. You are sliced. You are crushed beneath iron boots. Bloody knives rise again, and again, and again.

Beneath a film of blood, you stagger to your feet for one final attempt at escape.""",
       "options": [
            {
                "text": """Use Graveddon's fury as a hammer. Direct him to the gears.""",
                "stat": "shadowy",
                "difficulty": 5,
                "success_text": """The Iron Swine fights with ferocity, but he has underestimated your cunning.

You spot your opening, duck under his wild onslaught, and allow his blows to fall heavy upon the mechanism. The gears tumble from their casings, the gap just wide enough for you to dart past, throwing yourself bodily through the mirror. You leave his shrieks of fury behind you.""",
                "failure_text": """You cannot outmaneuver a god of war. You feint, you dodge, but he reads your every move. His knife rises, one final time.""",
                "next_state_success": 200,
                "next_state_failure": 200,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 190,
        "text": """Scorthidion is displeased.

Your body is wracked with sudden pain. Childhood scars reopen and weep, bruises bloom anew, bones shatter and warp. Forgotten wounds return to haunt you.

You stagger towards the mirror, falling to a crawl.""",
       "options": [
            {
                "text": """Willpower, now, is all that drives you.""",
                "stat": "dangerous",
                "difficulty": 5,
                "success_text": """You pull yourself through the gears, leaving the cogs slick with blood from your passage. You finally arrive at the escapement and, with one final supreme effort, pull the mirror down on top of you. The pain is immediately gone as you disappear into the Mirrorwise.""",
                "failure_text": """You crawl, slug-like across the floor, your lungs filling with blood. There is no escape.""",
                "next_state_success": 200,
                "next_state_failure": 200,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 10,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 195,
        "text": """You stoop to grasp the mirror, girding yourself for your coming journey.

You take a deep breath and a slow exhale.

Now, you are ready. You are ready now.""",
       "options": [
            {
                "text": """Enter the Mirrorwise""",
                "stat": "dangerous",
                "difficulty": 3,
                "success_text": """You pitch forward with a diver's grace, breaking the glass cleanly.""",
                "failure_text": """Your mind is unwilling to leave the clocktower, no matter the threat. Your body must insist.

The break is not clean.""",
                "next_state_success": 200,
                "next_state_failure": 200,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 20
            },
        ]
    },

# Mirrorwise Transition 2 story_state 200
    {
        "story_state": 200,
        "text": """Even braced against it, your mind rebels against the assault on your senses that is the Mirrorwise. You tumble and plunge through an ocean of oddity, again glimpsing ephemeral flashes of scenes framed in silver, gold, and tin: A capering titan, shackled to a spire of glass and bone. More colossi, lying long as terraced rows, bleeding from a thousand wounds. A great gate, a mile high and festooned with gibbets.

Your own reflection, magnified and duplicated a thousand times, fleeing through a mirror in the distance. <em>That</em> mirror, there!""",
        "options": [
            {
                "text": """Your reflections each leave a trail of bloody footprints. Track them.""",
                "stat": "watchful",
                "difficulty": 6,
                "success_text": """So many yous, so much blood. All converging to a single point. A perfect spiral inscribed upon your senses leading to a silvered pane of thick-cut glass, now stained crimson. You throw yourself through.""",
                "failure_text": """The other versions of yourself have muddied the spoor. They all converge, yes, but it is maddening to follow. Your footsteps pound to the rhythm of your heartbeat, cantering onwards through the kaleidoscope until you reach the center: a silvered pane of thick-cut glass, stained crimson. You fall through, exhausted.""",
                "next_state_success": 201,
                "next_state_failure": 201,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
            {
                "text": """Ignore the reflections. This is misdirection. Where do they naturally lead?""",
                "stat": "shadowy",
                "difficulty": 6,
                "success_text": """It is legerdemain, and clumsy at that. With a pang of embarrassment, you recognise your own work at play. If you were you (which you are), which way would you go now?
You turn from your reflection's trail and kick through a silvered pane of thick-cut glass, traced with crimson.""",
                "failure_text": """Misdirection? Perhaps, but it drew your attention effectively enough. Swivelling away from the prescribed route, you almost see too late your true destination: a silvered pane of thick-cut glass, stained crimson at the edges, drifting below you. Your hand catches painfully on the edge as you lever your way through.""",
                "next_state_success": 201,
                "next_state_failure": 201,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
            {
                "text": """Follow your reflection at pace, step for step.""",
                "stat": "dangerous",
                "difficulty": 6,
                "success_text": """More images flash before you as you push off from each mirror in a madcap chase: Saws the size of buildings, slicing through a tentacled leviathan. A black, twisting spire above a mirror-like black lake. A child in a peaked cap, playing with a clown puppet by the fire. You power through them, not brooking any distraction from your goal, and eventually break through a silvered pane of thick-cut glass, lined with crimson.""",
                "failure_text": """More images flash before you as you push off from each mirror in a madcap chase: Saws the size of buildings, slicing through a tentacled leviathan. A black, twisting spire above a mirror-like black lake. A child in a peaked cap, playing with a clown puppet by the fire. The scent too, is overwhelming. Decay: sweet, sickly, horrific. You gather your senses for one final moment of lucidity, and throw yourself through a silvered pane of thick-cut glass, stained crimson.""",
                "next_state_success": 201,
                "next_state_failure": 201,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            },
            {
                "text": """Call out to your reflection to wait.""",
                "stat": "persuasive",
                "difficulty": 6,
                "success_text": """Your reflection pauses, turning, one foot already through a silvered pane of thick-cut glass, laced with crimson lines. They extend a hand, pulling you through with them.""",
                "failure_text": """Your reflection turns, revealing a red-rimmed smile, blood dripping from their lips. A thousand iterations of yourself start towards you, grasping hands clawing at your frame. You feel your clothes rip as you push past, through a silvered pane of thick-cut glass, stained crimson.""",
                "next_state_success": 201,
                "next_state_failure": 201,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            }
        ]
    },

  # Empire of Thread story_state 201-250
    {
        "story_state": 201,
        "text": """You lurch through the mirror and immediately fall to your knees. Kaleidoscopic brilliance still blooms behind your eyes. You grope out blindly, meeting with a solid barrier, and for a wild moment you fear that you have been entombed once again.

But, little-by-little, you regain control of your senses. First, your touch: beneath your hands is cold stone and colder glass, crossed by thick cord-like vines. Your returning vision confirms this, with one caveat: they are not vines, but thread. A mass of it, the black juxtaposing grey stone and thick, cracked glass, pale with some interior luminescence.

You raise your head and inhale. The powerful scent of blood catches in your throat and you pitch forward, retching. It permeates the air. You remain immobile for a moment, curled into the fetal position, before you wrest control once more and rise unsteadily to your feet.

Sucking in short, shallow breaths, you take a quick damage assessment of your battered body, feeling with some surprise the music box still pressing against your chest. You remove it from your pocket and take a closer look by the pale light.

It is small and unadorned. It does not appear to open, although a crank on the side turns easily enough. You pocket it again and gaze about you, your head pounding.

You stand in a cavernous chamber, intersected by black thread, twined and looped in a serpentine sprawl. There are no exits apparent where the distant walls rise.""",
        "options": [
            {
                "text": """Follow the twisting thread. Where does it come from?""",
                "stat": "watchful",
                "difficulty": 7,
                "success_text": """There is something here. A tangle that obfuscates a greater design. Here, they weave together to snake across the glass. There, they interlace in sympathy with the cold stone.

They are not merely concordant with the vast floor. They stretch up the walls and to the distant ceiling too. There is mechanical purpose in their configuration. They are wires. They are veins; arteries; capillaries.

You trace the line to one common destination, or source. An opening in the stone. A darkened well, down which the thread plunges.""",
                "failure_text": """Is there a pattern to it? None that you can decipher.

It is an invitation to madness. An impenetrable coil of ink-black confusion. You wander the room in desperation, and almost see the opening in the stone below your feet too late.
You teeter on the edge of a darkened well. Threads converge here, of course. You wonder how you didn't see it before. You feel a buzzing pain behind your eyes.""",
                "next_state_success": 210,
                "next_state_failure": 210,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 20
            },
            {
                "text": """If in doubt, follow your nose. You have no shortage of olfactory stimulation.""",
                "stat": "shadowy",
                "difficulty": 7,
                "success_text": """Reluctant though you are to inhale more of the stomach-turning stench, you bend low and suck in a deep breath, swallowing down the bile that rises in response. The scent, as far as you can tell, is strongest wherever the thread converges. You chose one particularly large tangle and follow it, your nose confirming your suspicions.

You soon come across an opening in the stone: a darkened well, down which the thread plunges.""",
                "failure_text": """Bloodhound, you are not.

Your head is soon spinning with the heady stench of the gore, but it is some time before you can pinpoint the location, so omnipresent is the scent.

Eventually, you track the source to an opening in the stone: a darkened well, down which the thread plunges.""",
                "next_state_success": 210,
                "next_state_failure": 210,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 20
            }
        ]
    },

    {
        "story_state": 210,
        "text": """You stand before the well, casting one last hopeful look around the chamber for alternative points of egress.

But there are none. You must go down.""",
        "options": [
            {
                "text": """Pick your footholds carefully.""",
                "stat": "dangerous",
                "difficulty": 7,
                "success_text": """You wrap a length of thread around your arm and begin the descent, inching down with precision.

You are not sure how long you climb. Long enough for your legs and arms to scream in protest.

Long enough that you can no longer see the circle of pale light that marked the top of the well.

Long enough that when you finally reach the bottom, you are almost relieved to feel your feet sink into the viscera coating the floor.""",
                "failure_text": """You wrap a length of thread around your arm and begin the descent, inching down with precision.

You are not sure how long you climb. You see the circle of pale light that marked the top of the well wink out, and you press on through darkness.

And as you climb, uncomfortable comparisons come to you. You are a fish on the line, a hanged man unspooling his noose. Wouldn't it look pretty around your neck?

It is a relief to feel your feet sink into the viscera coating the floor.""",
                "next_state_success": 220,
                "next_state_failure": 220,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 2,
                "menace_change_success": 10,
                "menace_change_failure": 20
            },        ]
    },

    {
        "story_state": 220,
        "text": """Ignoring the awful stench and the cold blood seeping into your socks, you feel for the thread again. They continue: you trace their path along distressingly sticky walls, emerging into another chamber, almost as large as the one you exited above. This chamber, too, is bathed in a pale luminescence. Veins of glass wind through granite, their light reflecting off the mica within.

Against the far wall, a titanic corpse is slumped, threads winding over and under his body: roots enveloping a forgotten object. It was a man, you think. A king, judging by his crown. A god, judging by his size. His regal countenance is drawn, his head bowed. His blood is cold. It flows freely from the corpse, carving a route through the thick dust of the floor. It spiders out, a copper-scented delta of effluvia.

His eyes flicker open when you approach.

You pause. He does not move, nor make any indication that he has seen you.""",
        "options": [
            {
                "text": """He cannot move. Drink of Godblood. <em>(This is a bad idea)</em>""",
                "stat": "dangerous",
                "difficulty": 12,
                "success_text": """You dip your head to the river and drink deep.

Your body is wracked by sudden, exquisite pain. Your limbs begin to lengthen, bones cracking and popping free of their joints, then fusing again with a surge of warmth. Your throat contorts and a beautiful, inhuman scream escapes you in three-part harmony.

You are left panting on the floor, your clothes washed crimson by the flow of blood.

The corpse regards you impassively.""",
                "failure_text": """You dip your head to the river and drink deep.

Your body is wracked by sudden, unimaginable pain. Your eyes roll back into your head and stare into a blank skull. Your mind is filled with images. An old man, hammering a bejeweled crown on the anvil of a throne. A hunched, birdlike figure, bent over a tome bound in crimson leather. A woman in a straw hat, tending a garden of wrought-iron flowers.

You come to, slumped in the river, your clothes washed crimson by the flow of blood.

The corpse regards you impassively.""",
                "next_state_success": 230,
                "next_state_failure": 230,
                "apprehension_change_success": 5,
                "apprehension_change_failure": 2,
                "menace_change_success": 30,
                "menace_change_failure": 50
            },
            {
                "text": """He is a king? Bow. Ask of him a boon. Escape.""",
                "stat": "persuasive",
                "difficulty": 8,
                "success_text": """The corpse shifts his melancholic gaze to you.

"I am sorry, child" he says, sorrow etching his features. "My power has waned. You must descend."

One long finger extends. Where he points, a doorway blooms in the granite wall.

You bow low. You might even chance touching your forelock.

It is best to be thorough when thanking a god.""",
                "failure_text": """The corpse shifts his gaze to you.

Tears begin to flow down his cheeks, great golden droplets mingling with the deep incarnadine of his blood.

You feel your face crumpling in sympathy. You are caught by wracking sobs, weeping freely into the river.

Minutes pass. Eventually, you realise that he has ceased his tears. When you look up again, his eyes are closed, his face slack. To your left, a darkened doorway stands in the granite wall.""",
                "next_state_success": 240,
                "next_state_failure": 240,
                "apprehension_change_success": 2,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 10
            }
        ]
    },

    {
        "story_state": 230,
        "text": """You stand, dripping red and black.""",
        "options": [
            {
                "text": """Drink again. <em>This is, if possible, an even worse idea</em>""",
                "stat": "dangerous",
                "difficulty": 100,
                "success_text": """Well done, this should not be possible. Unfortunately, it truly <em>was</em> a bad idea.

Sorry.""",
                "failure_text": """Again, you stoop to drink.

As soon as the blood meets your lips, your vision begins to fade. You fancy that you see the corpse’s lips twitch upwards.""",
                "next_state_success": 230,
                "next_state_failure": 230,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 100,
                "menace_change_failure": 100
            },
            {
                "text": """Power courses through you. It must be directed.""",
                "stat": "persuasive",
                "difficulty": 8,
                "success_text": """Following some keen new instinct, you close your eyes. Golden light blooms behind your eyelids, the flare bright enough to imprint upon your vision. You feel the rush of power leaving you. Only a pleasant warmth remains.

When you reopen your eyes, blinking away the radiance, you see a doorway in the granite to your left.""",
                "failure_text": """Following some keen new instinct, you close your eyes. Golden light blooms behind your eyelids, the flare bright enough to imprint upon your vision. You feel the rush of power leaving you. You are a conduit, but you burn out like a cheap filament.

When you reopen your eyes, your hands are burned, and you feel a stinging pain at your temples that suggests the damage may be more widespread. But your effort bore fruit.

To your left, a doorway stands in the granite where there was none before.""",
                "next_state_success": 240,
                "next_state_failure": 240,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 20
            }
        ]
    },

    {
        "story_state": 240,
        "text": """You must go onwards.

And so you stumble through the doorway and down the passage. The floor is thick with thread. There is no light here: you grope blindly for the walls as you lumber onwards.

Your heartbeat is heavy in your ears. No. Not your heartbeat. <em>A</em> heartbeat.

It draws you onwards, tugging on you like… well, a <em>thread</em>.

Your legs are tiring, but you must go onwards.

You must go onwards.

Eventually, there is light ahead. You throw yourself forwards in a final effort, your leaden feet snagging on the fibrous floor to send you sprawling out into another chamber, this one larger than the previous two combined. Endless spools of thread weave across the stone. Star-like nodes of glass twinkle in a distant roof. Here, the scent of blood is lesser, left behind with the corpse of the god-king.

Upon the wall at the far end of the cavernous room, a giant, charcoal-grey heart is affixed. You watch as it pulses with a slow rhythm.""",
        "options": [
            {
                "text": """Address the heart. It is the right thing to do.""",
                "stat": "persuasive",
                "difficulty": 5,
                "success_text": """You call to the heart. You call your name. You call for freedom.

The heart beats.""",
                "failure_text": """You call to the heart. You call your name. You call for freedom.

The heart beats.""",
                "next_state_success": 250,
                "next_state_failure": 250,
                "apprehension_change_success": 1,
                "apprehension_change_failure": 1,
                "menace_change_success": 0,
                "menace_change_failure": 0
            },
        ]
    },

   # The End story_state 275-300
    {
        "story_state": 250,
        "text": """You approach to where the heart hangs, suspended on the wall by a webbed lattice of thread. Now that you are closer, it is clear: the heart is origin and terminus. Thread loops and twines through the atria and ventricles, sprouts like blossoming branches from the aorta and vena cava. It beats with a sluggish, ponderous cadence.

"THOU HAST COME FOR THE MIRROR."

The voice slips into your mind without troubling your ears. It is the thunder of rushing blood.

Your reply is simple: yes, you have.

The heart asks, in its heavy, millstone voice, whether you are certain. Have you not seen the memories, it asks. The memories in your little box?

You extract the music box from your pocket. Can it mean this?

Yes, the heart says. It means that. Place the side opposite to the crank over the base of your ear, it says, and turn the handle.

Perhaps you will, but you are not fool enough to do so without first taking some precautions.""",
        "options": [
            {
                "text": """If you cannot trust your body, ward your mind.""",
                "stat": "watchful",
                "difficulty": 10,
                "success_text": """You take a moment to breathe, flexing your fingers. You ground yourself against the errant lightning of distraction, and move the box up to your ear.

You turn the crank, and immediately your vision darkens. You are no longer in the dim chamber, stood in front of the great, grey heart. A rush of images comes to you: A glittering city of cut gemstones, almost painful in its gaudy brilliance. An impossible Tower of Babel spire, reaching out of sight. A bright stained glass cathedral, bristling with artillery, resting on mile-long caterpillar tracks. Grinning men in cracked greasepaint kicking a figure in the mud. An island-sized raft of sugar-spun bodies, fused together in caramel and floating in a treacle sea. The captain - it takes you a second to recognise her without her hat - smiling, laughing, her arm around the shoulder of a crewmate. The captain again, kneeling in front of a tree laden with golden fruit.

The visions fade, and you are standing just as you were before. The heart beats.""",
                "failure_text": """You take a moment to breathe, flexing your fingers. You ground yourself against errant lightning thoughts, and move the box up to your ear.

You turn the crank, and immediately your vision darkens. You are no longer in the dim chamber, stood in front of the great, grey heart. A rush of images comes to you: A glittering city of cut gemstones, almost painful in its gaudy brilliance. An impossible Tower of Babel spire, reaching out of sight. A bright stained glass cathedral, bristling with artillery, resting on mile-long caterpillar tracks. Grinning men in cracked greasepaint kicking a figure in the mud. An island-sized raft of sugar-spun bodies, fused together in caramel and floating in a treacle sea. The captain - it takes you a second to recognise her without her hat - smiling, laughing, her arm around the shoulder of a crewmate. The captain again, kneeling in front of a tree laden with golden fruit.

The visions fade. You are knelt before the heart, both hands clutching fistfuls of thread. They twitch and stray towards your eyes. You start to your feet with a yell. The heart beats.""",
                "next_state_success": 275,
                "next_state_failure": 275,
                "apprehension_change_success": 5,
                "apprehension_change_failure": 2,
                "menace_change_success": 0,
                "menace_change_failure": 20
            },
            {
                "text": """Lash yourself to the floor. You will fall prey to no siren.""",
                "stat": "dangerous",
                "difficulty": 10,
                "success_text": """Fortunately, you have rope in abundance. You grab a handful of thread and tie firm knots around your boots, affixing you to the stone below. Then, you raise the music box to your ear.

You turn the crank, and immediately your vision darkens. You are no longer in the dim chamber, stood in front of the great, grey heart. A rush of images comes to you: A glittering city of cut gemstones, almost painful in its gaudy brilliance. An impossible Tower of Babel spire, reaching out of sight. A bright stained glass cathedral, bristling with artillery, resting on mile-long caterpillar tracks. Grinning men in cracked greasepaint kicking a figure in the mud. An island-sized raft of sugar-spun bodies, fused together in caramel and floating in a treacle sea. The captain - it takes you a second to recognise her without her hat - smiling, laughing, her arm around the shoulder of a crewmate. The captain again, kneeling in front of a tree laden with golden fruit.

The visions fade. You remain rooted to the floor, and bend to untie yourself. The heart beats.""",
                "failure_text": """Fortunately, you have rope in abundance. You grab a handful of thread and tie firm knots around your boots, affixing you to the stone below. Then, you raise the music box to your ear.

You turn the crank, and immediately your vision darkens. You are no longer in the dim chamber, stood in front of the great, grey heart. A rush of images comes to you: A glittering city of cut gemstones, almost painful in its gaudy brilliance. An impossible Tower of Babel spire, reaching out of sight. A bright stained glass cathedral, bristling with artillery, resting on mile-long caterpillar tracks. Grinning men in cracked greasepaint kicking a figure in the mud. An island-sized raft of sugar-spun bodies, fused together in caramel and floating in a treacle sea. The captain - it takes you a second to recognise her without her hat - smiling, laughing, her arm around the shoulder of a crewmate. The captain again, kneeling in front of a tree laden with golden fruit.

The visions fade. When you come to, you are suspended by your feet, halfway in the air in front of the heart. You yell and kick out. The thread relinquishes its grip, allowing you to fall heavily to the floor. The heart beats.""",
                "next_state_success": 275,
                "next_state_failure": 275,
                "apprehension_change_success": 5,
                "apprehension_change_failure": 2,
                "menace_change_success": 0,
                "menace_change_failure": 20
            }
        ]
    },

    {
        "story_state": 275,
        "text": """Above you, the heart unspools a length of thread. An ornate mirror hangs suspended in the tangle.

"THERE" the heart intones.

"THOU HAST SEEN WHAT IS POSSIBLE IN THE HOUSE.

THERE ARE JOYS AND WONDERS, YES, BUT THERE ARE HORRORS TOO.

STAY WITH ME. I SHALL OFFER THEE GREAT WORKS. WE SHALL HAVE SUCH DESIGNS.

THOU SHALT NOT WANT."

There is a pause. Two heartbeats long.
 
"DO NOT LEAVE ME."

You look up at the heart, hanging in its web of thread.

You have made your decision.""",
        "options": [
            {
                "text": """O Heart, show me freedom.""",
                "stat": "persuasive",
                "difficulty": 5,
                "success_text": """There is a long silence.

You count seven pulses of the great, grey heart, before finally, it lowers the mirror level with you.

You thank the heart. It remains silent. You take one final breath, then plunge through.

The Mirrorwise is familiar now, but it has never been this ordered. Frames slot into place, setting in patterns ahead of you like rail lines. A thread - invisible, though insistent - pulls you onwards, guiding you towards a distant mirror through which gaslight blooms. Ever faster are you urged forward, until you tumble unceremoniously though the mirror into a bathtub, mercifully unoccupied.""",
                "failure_text": """There is a long silence.

You wait for perhaps a minute before the heart finally answers.

"NO."

The mirror retreats into the folds of the heart. You stand before it. Utterly alone.""",
                "next_state_success": 300,
                "next_state_failure": 300,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 100
            },
            {
                "text": """O Heart, permit me stay.""",
                "stat": "persuasive",
                "difficulty": 5,
                "success_text": """Does the pulse quicken, just for a moment?

The heart is silent for a long time.

Then, finally:

"THANK YOU."

You smile.""",
                "failure_text": """There is a long silence.

You wait for perhaps a minute before the heart finally answers.

"YOU LIE."

The mirror retreats into the folds of the heart. You stand before it. Utterly alone.""",
                "next_state_success": 290,
                "next_state_failure": 290,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 100
            },
        ]
    },

    {
        "story_state": 290,
        "text": """It is comfortable in the twilight glimmer of the glass-node stars. The heart has summoned entire worlds for you. You have tasted manifold delights that you once could only have dreamt of. Every day is a cavalcade of pleasures, every night brings more still.

"DO NOT LEAVE ME", it had asked.

And so you hadn't.""",
        "options": [
            {
                "text": """Accept your ending""",
                "stat": "persuasive",
                "difficulty": 1,
                "success_text": """Be at peace.""",
                "failure_text": """Be at peace.""",
                "next_state_success": 301,
                "next_state_failure": 301,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 0
            },
        ]
    },

    {
        "story_state": 300,
        "text": """You scramble out of the bathtub and onto the wood-panelled floor. You lie there a moment, soaking in the warmth of the room.

A gentle breeze on your face. You turn your head: there is an open window, light and life outside. You can hear the bustle of crowds, the strident call of street-vendors, the excited babble of children.

You fish the music box from your coat. Does it seem lighter, now?

A bright orchard flashes behind your eyes.

You smile.""",
        "options": [
            {
                "text": """Accept your ending""",
                "stat": "persuasive",
                "difficulty": 1,
                "success_text": """Be at peace.""",
                "failure_text": """Be at peace.""",
                "next_state_success": 301,
                "next_state_failure": 301,
                "apprehension_change_success": 0,
                "apprehension_change_failure": 0,
                "menace_change_success": 0,
                "menace_change_failure": 0
            },
        ]
    },
]