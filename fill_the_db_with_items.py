# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def CreateCategory(n):
    c = Category(name=n)
    session.add(c)
    session.commit()

def CreateItem(t,d,c):
    i = Item(title=t,description=d,cat_id=c)
    session.add(i)
    session.commit()

CreateCategory("Soccer")                #1
CreateCategory("Basketball")            #2
CreateCategory("Baseball")              #3
CreateCategory("Frisbe")                #4
CreateCategory("Snowboarding")          #5
CreateCategory("Rock Climbing")         #6
CreateCategory("Foosball")              #7
CreateCategory("Skating")               #8
CreateCategory("Hockey")                #9


CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",1)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",1)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",1)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",1)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",1)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",1)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",1)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",1)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",1)

CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",2)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",2)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",2)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",2)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",2)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",2)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",2)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",2)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",2)

CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",3)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",3)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",3)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",3)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",3)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",3)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",3)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",3)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",3)

CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",4)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",4)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",4)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",4)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",4)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",4)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",4)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",4)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",4)

CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",5)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",5)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",5)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",5)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",5)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",5)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",5)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",5)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",5)

CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",6)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",6)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",6)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",6)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",6)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",6)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",6)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",6)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",6)
7
CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",7)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",7)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",7)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",7)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",7)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",7)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",7)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",7)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",7)
8
CreateItem("Uniform","Most youth soccer leagues require a standard uniform for all players. This might range from a simple Tshirt to a complete soccer uniform with matching jersey, shorts and socks. Some leagues issue the uniform to players, while others require you to order the uniform yourself.",8)
CreateItem("Practice clothes","Uniforms are typically reserved for wear in games only, so your little kicker needs comfortable athletic clothes for soccer practice. Choose clothes that allow a full range of motion. Sweatwicking material keeps your child cool and dry during sweaty warmweather practices",8)
CreateItem("Soccer cleats","When your child plays in an organized league, you likely need soccerspecific cleats. These shoes are designed for the sport to give your soccer player the support and traction necessary in the game.",8)
CreateItem("Shin guards","Protective shin guards are another requirement in most leagues. They rest at the front of the shin to protect from errant kicks and fastmoving balls.",8)
CreateItem("Soccer socks","Just like your child needs special shoes, she also needs special socks designed for soccer. The long socks go up and over the shin guards.",8)
CreateItem("Ball","Your childs coach may provide balls during practice, but its always a good idea to have a quality soccer ball of your own so you can practice at home. Invest in a highquality ball instead of a cheap foam ball that doesnt give your player a real feel for soccer play.",8)
CreateItem("Goalkeeper gloves","If your child is interested in playing goalkeeper, consider investing in a pair of goalkeeper gloves. These special gloves are designed to support the wrists while allowing freedom of movement in the fingers. If your child is young, the league may not play with goalies just yet, so hold off on the gloves until you know if your child will actually play the goalkeeper role.",8)
CreateItem("Water bottle","Soccer players spend a lot of time running up and down the field. The soccer season often falls during warm weather. Hydration is important, so outfit your child with her own water bottle. Write her name on the bottle to avoid mixups on the bench.",8)
CreateItem("Gear bag","A backpack or tote bag designed for soccer makes it easy to carry all that gear to practices and games. These specialty bags typically include a spot for a soccer ball and all the other gear your child needs.",8)

print("items add to db!")
