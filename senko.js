Discord=require("discord.js");
fs=require("fs");
bot=new Discord.Client();

bot.on("ready",()=>{
	data={
		"owner":bot.users.get("335554170222542851"),
		"nsb":bot.users.get("439205512425504771"),
		"irene":bot.guilds.get("623576218595360778"),
		"colors":[
			"#E74C3C",
			"#E67E22",
			"#F1C40F",
			"#2ECC71",
			"#3498DB",
			"#9B59B6"
		],
		"reacts":{
			"497730525528850444":"NotFunny", // YeeYee
			"342777816498176001":"NotFunny", // Spluphoes mad
			"335554170222542851":"NotFunny", // Me
			"359484915735068672":"NotFunny", // Botstotmer
			"215075528070266890":"badMen", // Enzo
			"311583840202391552":"goku"  // Goku
		},
		"lastNotFunny":0,
		"ci":0,
		"pornCommands":[".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"],
		"deleteChannels":[],
		"exts":[".png", ".gif", ".jpg", ".jpeg", ".mp4", ".mov", ".bmp"],
	};
	data.memeChannel=data.irene.channels.find(x=>x.id=="623584630309650446");
	setInterval(doRoles, 1000*60*60);
	bot.on("message", onMessage);
});
function onMessage(m){
	if (m.author.id==bot.user.id){return;}
	if (data.pornCommands.indexOf(m.content.toLowerCase().split(" ")[0])!=-1 && /[+%&#]/.test(m.content)){
		data.deleteChannels.push(m.channel.id);
		m.channel.send("Your command was deleted for using URL escape characters```"+m.content.replace(/`/g, "`\u200b")+"```There is a chance I deleted the wrong response by NSB, in which case I'm sorry");
		m.delete();
	} else if (m.author.id==data.nsb.id && data.deleteChannels.indexOf(m.channel.id)!=-1){
		setTimeout(function(){
			// Deleting it immediately sometimes makes mobile discord keep showing it
			m.delete();
			data.deleteChannels.splice(data.deleteChannels.indexOf(m.channel.id), 1);
		}, 250);
	} else if (data.pornCommands.indexOf(m.content.toLowerCase().split(" ")[0])!=-1 && m.content.toLowerCase().indexOf("senko")!=-1){
		data.deleteChannels.push(m.channel.id);
		m.channel.send("Not fucking impressed, buddy");
		m.delete();
	} else if (new Date().getTime()-data.lastNotFunny>1000*60*5 && m.channel.id==data.memeChannel.id && (m.attachments.array().length!=0 || /\.(pnga?|jpe?g|gif|mp[34]|webm)$/.test(m.content.toLowerCase()))){
		if (m.author.id in data.reacts){
			var rname=data.reacts[m.author.id],
				rfiles=fs.readdirSync("imageSets/"+rname).map(x=>"imageSets/"+rname+"/"+x),
				msg=(rname=="notFunny"?(Math.random()<0.05?"Delete this if you're a filthy Bosnian":"Where's the funny?"):"");
			m.channel.send(msg, {"files":[rfiles[Math.floor(Math.random()*rfiles.length)]]});
			data.lastNotFunny=new Date().getTime()
		}
	}
}
function doRoles(){
	for (guild of bot.guilds.array()){
		role=guild.roles.find(x=>x.name=="Certified Senko");
		role.setColor(data.colors[data.ci]);
	}
	data.ci=(data.ci+1)%data.colors.length;
}
bot.login(process.env.senkobottoken);