# By @NOOB_GUY_OP for Dark CObra
# If you steal this without credits You will be the geyest gey ever in the world that you will suck cat's dick.
import asyncio

from .. import ALIVE_NAME, CMD_HELP
from ..utils import lightning_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@borg.on(lightning_cmd(pattern="birthday$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**Hello!๐**",
        "**How Are You?**",
        f"**{DEFAULTUSER}Happy Birthday**"
        "[Happy Birthday](http://2.bp.blogspot.com/-WGLaIVbpK6U/WT4sr0LG2TI/AAAAAAAAVX0/1t0F3gECRh4okN6zJzq6fMwQ7dA4Qw8AwCLcB/s1600/happy-birthday-to-you.png)",
        "**Wishing you ๐ a ๐ day ๐ filled ๐ with ๐ happiness and ๐ a ๐ year ๐ filled ๐ with ๐ joy ๐.**",
        "**Sending you ๐ smiles ๐ for  every ๐ moment ๐ of your special ๐ฒ day ๐*",
        "**Have ๐ a ๐ wonderful ๐ time ๐ and a very ๐ happy ๐ birthday ๐!**",
        "**Count your ๐ life ๐ค by ๐ smiles, ๐ not ๐ซ tears. ๐ญ Count your ๐ age ๐ต by ๐ friends, ๐ซ not ๐ซ years. ๐ Happy ๐ birthday ๐!**",
        "**I hope ๐ all ๐ฏ your ๐ birthday ๐ wishes and ๐ dreams ๐ come true. ๐ฏ**",
        "**Another ๐ adventure filled ๐ year ๐ awaits you. ๐ Welcome it ๐ฏ by ๐ celebrating ๐ซ your ๐ birthday ๐ with ๐ pomp and ๐ splendor. Wishing you ๐ a ๐ very ๐ happy ๐ and ๐ fun-filled birthday ๐!**",
        "**Happy ๐ birthday ๐ to someone ๐ค who ๐ is smart, ๐ฉ gorgeous, ๐ funny ๐ and ๐ reminds me ๐ญ a ๐ lot of ๐ฆ myselfโฆ from ๐ one ๐ค fabulous chick ๐ฃ to another !**",
        "[For You](http://www.handletheheat.com/wp-content/uploads/2015/03/Best-Birthday-Cake-with-milk-chocolate-buttercream-SQUARE.jpg)",
        "[For You](http://i.pinimg.com/originals/49/d2/e3/49d2e318a2705cbd300e21023392ff6f.jpg)",
        "Here is also ๐Gifts๐ from me๐จ.",
        "[For You](http://5.imimg.com/data5/KE/IK/MY-15644577/antique-gold-gift-box-luxury-rigid-box02-250x250.jpg)",
        "[For You](http://i.pinimg.com/originals/10/b8/fb/10b8fb15270d8db1f6ff967e7026d2de.gif)",
        "[For You](http://www.lovethispic.com/uploaded_images/367867-Starry-Happy-Birthday-Gif.gif)",
    ]
    for i in animation_ttl:  # By @NOOB_GUY_OP for Dark CObra

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        )  # By @NOOB_GUY_OP for Dark CObra


CMD_HELP.update(
    {
     "HBD": "`.hbty`\
     \n**USAGE**: For Wishing Happy Birthday"
     
    }
)
