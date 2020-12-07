// https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot

Discord=require("discord.js");
fs=require("fs");
bot=new Discord.Client();
console.log("Booting Senko bot")
bot.on("ready",()=>{
	data={
		"owner":bot.users.get("335554170222542851"),
		"nsb":bot.users.get("439205512425504771"),
		//"SST":bot.guilds.get("691881732101636097"),
		"colors":[
			"#E74C3C",
			"#E67E22",
			"#F1C40F",
			"#2ECC71",
			"#3498DB",
			"#9B59B6"
		],
		"reacts":{
			"335554170222542851":"NotFunny", // Me
			"225339003270987776":"Furry"     // Teffy
		},
		"lastNotFunny":0,
		"senkoColorIndex":0,
		"deleteChannels":[],
		"exts":[".png", ".gif", ".jpg", ".jpeg", ".mp4", ".mov", ".bmp", ".webm"],
		"memeChannels":[
			//"691883108915609600", // SST
			"333628523795447808"  // Teffy
		]
	};
	console.log("Senko bot booted")
	//console.log(data)
	doRoles()
	setInterval(doRoles, 1000*60*60);
	bot.on("message", onMessage);
});

function onMessage(m){
	if (m.author.id==bot.user.id){return;}
	var member,
		rname,
		rfiles;
	member=m.guild.members.get(m.author.id);

	if (new Date().getTime()-data.lastNotFunny>1000*60*5 && data.memeChannels.indexOf(m.channel.id)!=-1 && (m.attachments.array().length!=0 || /\.(pnga?|jpe?g|gif|mp[34]|webm)$/.test(m.content.toLowerCase()))){
		if (m.author.id in data.reacts){
			rname=data.reacts[m.author.id];
			rfiles=fs.readdirSync("imageSets/"+rname).map(x=>"imageSets/"+rname+"/"+x);
			m.channel.send("Where's the funny?", {"files":[rfiles[Math.floor(Math.random()*rfiles.length)]]});
			data.lastNotFunny=new Date().getTime();
		}
	}
}

function doRoles(){
	var role, roleId;
	for (guild of bot.guilds.array()){
		role=guild.roles.find(x=>x.name=="Certified Senko");
		if (role!=null){
			try {
				role.setColor(data.colors[data.senkoColorIndex]);
			} catch (e) {console.log("Failed setting senko role color for ", guild.name)}
		}
	}
	data.senkoColorIndex=(data.senkoColorIndex+1)%data.colors.length;
}
bot.login(process.env.senkobottoken);