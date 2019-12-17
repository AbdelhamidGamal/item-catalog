# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base,  Category,  Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def CreateCategory(n):
    c = Category(name=n,  user_id=1)
    session.add(c)
    session.commit()


def CreateItem(t, d, c):
    i = Item(title=t, description=d, cat_id=c, user_id=1)
    session.add(i)
    session.commit()


CreateCategory("Soccer")                # 1
CreateCategory("Basketball")            # 2
CreateCategory("Baseball")              # 3
CreateCategory("Frisbe")                # 4
CreateCategory("Snowboarding")          # 5
CreateCategory("Rock Climbing")         # 6
CreateCategory("Foosball")              # 7
CreateCategory("Skating")               # 8
CreateCategory("Hockey")                # 9

uniform_disc = ("Most youth soccer leagues require a standard uniform for all "
                " players. This might range from a simple Tshirt to a complete"
                " soccer uniform with matching jersey,  shorts and socks. Some"
                " leagues issue the uniform to players,  while others require "
                " you to order the uniform yourself.")

Practice_clothes = ("Uniforms are typically reserved for wear in games only, "
                    " so your little kicker needs comfortable athletic clothes"
                    " for soccer practice. Choose clothes that allow a full "
                    " range of motion. Sweatwicking material keeps your child "
                    " cool and dry during sweaty warmweather practices")

Soccer_cleats = ("When your child plays in an organized league,  you likely "
                 " need soccerspecific cleats. These shoes are designed for "
                 " the sport to give your soccer player the support and "
                 " traction necessary in the game.")

Shin_guards = ("Protective shin guards are another requirement in "
               " most leagues. They rest at the front of the shin to protect "
               " from errant kicks and fastmoving balls.")

Soccer_socks = ("Just like your child needs special shoes,  she also needs "
                " special socks designed for soccer. The long socks go up "
                " and over the shin guards.")

Ball_disc = ("Your childs coach may provide balls during practice,  "
             " but its always a good idea to have a quality soccer ball "
             " of your own so you can practice at home. Invest "
             " in a highquality ball instead of a cheap foam ball that "
             " doesnt give your player a real feel for soccer play.")

Goalkeeper_gloves = ("If your child is interested in playing goalkeeper,  "
                     " consider investing in a pair of goalkeeper gloves. "
                     " These special gloves are designed to support the "
                     " wrists while allowing freedom of movement in the "
                     " fingers. If your child is young,  the league may not "
                     " play with goalies just yet,  so hold off on the gloves "
                     " until you know if your child will actually play "
                     " the goalkeeper role.")

Water_bottle = ("Soccer players spend a lot of time running up and "
                " down the field. The soccer season often falls during "
                " warm weather. Hydration is important,  so outfit your "
                " child with her own water bottle. Write her name on "
                " the bottle to avoid mixups on the bench.")

Gear_bag = ("A backpack or tote bag designed for soccer makes it easy "
            " to carry all that gear to practices and games. These "
            " specialty bags typically include a spot for a soccer "
            " ball and all the other gear your child needs.")

CreateItem("Uniform", uniform_disc, 1)
CreateItem("Practice clothes", Practice_clothes, 1)
CreateItem("Soccer cleats", Soccer_cleats, 1)
CreateItem("Shin guards", Shin_guards, 1)
CreateItem("Soccer socks", Soccer_socks, 1)
CreateItem("Ball", Ball_disc, 1)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 1)
CreateItem("Water bottle", Water_bottle, 1)
CreateItem("Gear bag", Gear_bag, 1)

CreateItem("Uniform", uniform_disc, 2)
CreateItem("Practice clothes", Practice_clothes, 2)
CreateItem("Soccer cleats", Soccer_cleats, 2)
CreateItem("Shin guards", Shin_guards, 2)
CreateItem("Soccer socks", Soccer_socks, 2)
CreateItem("Ball", Ball_disc, 2)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 2)
CreateItem("Water bottle", Water_bottle, 2)
CreateItem("Gear bag", Gear_bag, 2)

CreateItem("Uniform", uniform_disc, 3)
CreateItem("Practice clothes", Practice_clothes, 3)
CreateItem("Soccer cleats", Soccer_cleats, 3)
CreateItem("Shin guards", Shin_guards, 3)
CreateItem("Soccer socks", Soccer_socks, 3)
CreateItem("Ball", Ball_disc, 3)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 3)
CreateItem("Water bottle", Water_bottle, 3)
CreateItem("Gear bag", Gear_bag, 3)

CreateItem("Uniform", uniform_disc, 4)
CreateItem("Practice clothes", Practice_clothes, 4)
CreateItem("Soccer cleats", Soccer_cleats, 4)
CreateItem("Shin guards", Shin_guards, 4)
CreateItem("Soccer socks", Soccer_socks, 4)
CreateItem("Ball", Ball_disc, 4)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 4)
CreateItem("Water bottle", Water_bottle, 4)
CreateItem("Gear bag", Gear_bag, 4)

CreateItem("Uniform", uniform_disc, 5)
CreateItem("Practice clothes", Practice_clothes, 5)
CreateItem("Soccer cleats", Soccer_cleats, 5)
CreateItem("Shin guards", Shin_guards, 5)
CreateItem("Soccer socks", Soccer_socks, 5)
CreateItem("Ball", Ball_disc, 5)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 5)
CreateItem("Water bottle", Water_bottle, 5)
CreateItem("Gear bag", Gear_bag, 5)

CreateItem("Uniform", uniform_disc, 6)
CreateItem("Practice clothes", Practice_clothes, 6)
CreateItem("Soccer cleats", Soccer_cleats, 6)
CreateItem("Shin guards", Shin_guards, 6)
CreateItem("Soccer socks", Soccer_socks, 6)
CreateItem("Ball", Ball_disc, 6)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 6)
CreateItem("Water bottle", Water_bottle, 6)
CreateItem("Gear bag", Gear_bag, 6)

CreateItem("Uniform", uniform_disc, 7)
CreateItem("Practice clothes", Practice_clothes, 7)
CreateItem("Soccer cleats", Soccer_cleats, 7)
CreateItem("Shin guards", Shin_guards, 7)
CreateItem("Soccer socks", Soccer_socks, 7)
CreateItem("Ball", Ball_disc, 7)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 7)
CreateItem("Water bottle", Water_bottle, 7)
CreateItem("Gear bag", Gear_bag, 7)

CreateItem("Uniform", uniform_disc, 8)
CreateItem("Practice clothes", Practice_clothes, 8)
CreateItem("Soccer cleats", Soccer_cleats, 8)
CreateItem("Shin guards", Shin_guards, 8)
CreateItem("Soccer socks", Soccer_socks, 8)
CreateItem("Ball", Ball_disc, 8)
CreateItem("Goalkeeper gloves", Goalkeeper_gloves, 8)
CreateItem("Water bottle", Water_bottle, 8)
CreateItem("Gear bag", Gear_bag, 8)

print("items add to db!")
