Discord=require("discord.js");
bot=new Discord.Client();
bot.on("ready",()=>{
	data={
		"owner":bot.users.get(335554170222542851),
		"nsb":bot.users.get(439205512425504771),
		"irene":bot.guilds.get(623576218595360778)
	}
	console.log(data);
})
bot.login(process.env.senkobottoken);