#===========================================================================================================================                                                                                                                          
#   SSSSSSSSSSSSSSS PPPPPPPPPPPPPPPPP        AAA               DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE   SSSSSSSSSSSSSSS  
# SS:::::::::::::::SP::::::::::::::::P      A:::A              D::::::::::::DDD   E::::::::::::::::::::E SS:::::::::::::::S
#S:::::SSSSSS::::::SP::::::PPPPPP:::::P    A:::::A             D:::::::::::::::DD E::::::::::::::::::::ES:::::SSSSSS::::::S
#S:::::S     SSSSSSSPP:::::P     P:::::P  A:::::::A            DDD:::::DDDDD:::::DEE::::::EEEEEEEEE::::ES:::::S     SSSSSSS
#S:::::S              P::::P     P:::::P A:::::::::A             D:::::D    D:::::D E:::::E       EEEEEES:::::S            
#S:::::S              P::::P     P:::::PA:::::A:::::A            D:::::D     D:::::DE:::::E             S:::::S            
# S::::SSSS           P::::PPPPPP:::::PA:::::A A:::::A           D:::::D     D:::::DE::::::EEEEEEEEEE    S::::SSSS         
#  SS::::::SSSSS      P:::::::::::::PPA:::::A   A:::::A          D:::::D     D:::::DE:::::::::::::::E     SS::::::SSSSS    
#    SSS::::::::SS    P::::PPPPPPPPP A:::::A     A:::::A         D:::::D     D:::::DE:::::::::::::::E       SSS::::::::SS  
#       SSSSSS::::S   P::::P        A:::::AAAAAAAAA:::::A        D:::::D     D:::::DE::::::EEEEEEEEEE          SSSSSS::::S 
#            S:::::S  P::::P       A:::::::::::::::::::::A       D:::::D     D:::::DE:::::E                         S:::::S
#            S:::::S  P::::P      A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D E:::::E       EEEEEE            S:::::S
#SSSSSSS     S:::::SPP::::::PP   A:::::A             A:::::A   DDD:::::DDDDD:::::DEE::::::EEEEEEEE:::::ESSSSSSS     S:::::S
#S::::::SSSSSS:::::SP::::::::P  A:::::A               A:::::A  D:::::::::::::::DD E::::::::::::::::::::ES::::::SSSSSS:::::S
#S:::::::::::::::SS P::::::::P A:::::A                 A:::::A D::::::::::::DDD   E::::::::::::::::::::ES:::::::::::::::SS 
# SSSSSSSSSSSSSSS   PPPPPPPPPPAAAAAAA                   AAAAAAADDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSSSSS   
#==========================================================================================================================                                                                                                                         

#import requirements                                                                                                                          
import os
import random
import discord
import datetime
import json
from discord.ext.commands import Bot
from discord import Game, Embed, Color, Status, ChannelType
		
#setup bots prefix and tokens
prefix = "./"
Client = discord.Client(pass_context=True)
client = Bot(command_prefix=prefix)
commands = """```diff
-Admin Commands-
-==============-
-./add role-
-./remove role-
-./remove all roles-
-./Destroy the server-
-./Change nickname-
-./change all nicknames-
-./server info-
-./user info-
-./purge-

-Fun Commands-
-============-
-./rr = russian roulette-
-./8ball = magic 8 ball-

-EXTRAS-
-======-
-./proxy = gives random no log proxy sites-
-./namegen = generates 1st and last name-
-./shutdown = kill the bot-
```
"""
token = input("Enter discord token")

@client.event
async def on_ready():
	print ("\033[0;31m")
	print ("""
                	_.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   \                            `*TP*     d$$P*******$   
    \                                    :$$P'      /    
     \                                  :dP'       /     
      `.                               d$P       .'      
        `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'
============================================================
<CREDITS> CODED BY SPADES[...]
<TO> MR.PROXY[...]
<FROM> SPADES[...]
<COMMENT> ENJOY THE BOT!!![...]
============================================================
""")
	print ("\033[0;32m")
	print ('Logged in as')
	print ("\033[0;36m")
	print (client.user.name)
	print (client.user.id)
	
@client.command(pass_context=True)
async def commands(ctx,*args):
	await client.say("""```diff
-Self Commands-
-=============-
-./purge-
-./status-
-./guild-
	
-Admin Commands-
-==============-
-./add role-
-./remove role-
-./remove all roles-
-./Destroy the server-
-./Change nickname-
-./change all nicknames-
-./kick user-
-./ban user-
-./server info-
-./user info-

-Fun Commands-
-============-
-./rr = russian roulette-
-./8ball = magic 8 ball-

-EXTRAS-
-======-
-./proxy = gives random no log proxy sites-
-./namegen = generates 1st and last name-
-./shutdown = kill the bot-
```
""")

@client.command(pass_context=True)
async def rr(ctx,*args):
	croll = ("```diff -you pick up the revolver and spin the chamber-```")
	roll = ('```css you shot yourself and died','you live for now and pass the gun```')
	await client.say(croll)
	await client.say(random.choice(roll))

@client.command(pass_context=True)	
async def purge(message, parameters, recursion=0):
    if parameters == '':
        await reply(message, commands['purge'][1].format(PREFIX))
        return
    if not parameters.isdigit():
        await reply(message, "Number of messages to purge must be a positive integer.")
        return
    async for msg in client.logs_from(message.channel, limit=int(parameters) + 1):
        try:
            await client.delete_message(msg)
        except:
            pass
    success_msg = await client.send_message(message.channel, "Successfully purged **" + parameters + "** messages! :thumbsup:")
    await asyncio.sleep(2)
    await client.delete_message(success_msg)

client.command(pass_context=True)
async def serverinfo(message, parameters, recursion=0):
    server = message.server
    text = 0
    voice = 0
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            text += 1
        elif channel.type == discord.ChannelType.voice:
            voice += 1
    msg = "```autohotkey\n"
    msg += '                id: {server.id}\n'
    msg += '       server name: {server.name}\n'
    try:
        msg += '             owner: {server.owner.name}#{server.owner.discriminator} ({server.owner.id})\n'
    except:
        msg += '             owner: <error - could not get information on owner>\n'
    msg += '        created at: {server.created_at} ({} ago)\n'.format(strfdelta(datetime.datetime.utcnow() - server.created_at), server=server)
    msg += '            region: {server.region}\n'
    msg += '           members: {server.member_count}\n'
    msg += 'verification level: {server.verification_level}\n'
    msg += '          channels: {} channels ({} text, {} voice)\n'.format(text + voice, text, voice)
    if len(server.roles) > 50:
        msg += '             roles: {} roles, showing top 50\n{}\n'.format(len(server.roles), ', '.join([x.name for x in server.role_hierarchy][0:50]))
    else:
        msg += '             roles: {} roles\n{}\n'.format(len(server.role_hierarchy), ', '.join(map(lambda x: x.name, server.role_hierarchy)))
    msg += '            emojis: {}\n'.format(len(server.emojis))
    msg += '              icon:```{server.icon_url}'
    await reply(message, msg.format(server=server))


client.run(token,bot = False)