// https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot

Discord=require("discord.js");
fs=require("fs");
bot=new Discord.Client();
console.log("Booting Senko bot")
bot.on("ready",()=>{
	data={
		"owner":bot.users.get("335554170222542851"),
		"nsb":bot.users.get("439205512425504771"),
		"SST":bot.guilds.get("691881732101636097"),
		"colors":[
			"#E74C3C",
			"#E67E22",
			"#F1C40F",
			"#2ECC71",
			"#3498DB",
			"#9B59B6"
		],
		"serverRoles":{
			/*"691819406325579848":[ // ANCAP GANG
				"#010101",
				"#FFFF00"
			],/**/
			"691881732101636097":{
				"698669002330996828":[
					"#FFFF00",
					"#0000FF",
					"#FFFFFF",
					"#007F00",
					"#010101"  // Not black but black turns into transparent so :/
				]
			}
		},
		"serverRolePeriod":1,
		"serverRoleIndex":0,
		"reacts":{
			"335554170222542851":"NotFunny", // Me
			"359484915735068672":"NotFunny", // Botstotmer
			"215075528070266890":"badMen",   // Enzo
			"311583840202391552":"goku",     // Goku
			"614218298841759746":"NotFunny", // Cerina's little shit brother
			"225339003270987776":"Furry",    // Teffy
			"481647372523536384":"NotFunny"  // The Goon/Cat/Sam
		},
		"lastNotFunny":0,
		"ci":0,
		"pornCommands":[".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"],
		"deleteChannels":[],
		"exts":[".png", ".gif", ".jpg", ".jpeg", ".mp4", ".mov", ".bmp", ".webm"],
		"memeChannels":[
			"691883108915609600", // SST
			"333628523795447808"  // Teffy
		]
	};
	data.serverRolePeriod=deltaNotationArray(lcm, [].concat(...Object.values(data.serverRoles).map(Object.values)).map(x=>x.length));//Object.values(data.daiyaRoles).map(x=>x.length));
	console.log("Senko bot booted")
	//console.log(data)
	doRoles()
	setInterval(doRoles, 1000*60*60);
	bot.on("message", onMessage);
});

function lcm(a,b){
	var i=1, j=1;
	if ((a<0)!=(b<0) || (a==0)!=(b==0)){return 0;} // You got a better answer?
	while (a*i!=b*j){
		if (a*i>b*j){j++;}
		if (a*i<b*j){i++;}
	}
	return a*i;
}
function deltaNotationArray(f, a){
	if (a.length==1){
		return a[0];
	} else if (a.length==2){
		return f(a[0], a[1]);
	} else {
		return deltaNotationArray(f, [f(a[0], a[1])].concat(a.splice(2)));
	}
}

function onMessage(m){
	if (m.author.id==bot.user.id){return;}
	var member, 
		// isSSTMod, 
		rname,
		rfiles;
	member=m.guild.members.get(m.author.id);
	
	if (m.guild==data.SST && m.author==data.owner && m.content!="" && ["691884413558194186", "692926620822143028", "713295801203425322", "712514087480983574", "712395282935185419"].indexOf(m.channel.id)==-1){
		m.delete();
		data.owner.send("Bitch");
		return;
	}

	if (data.pornCommands.indexOf(m.content.toLowerCase().split(" ")[0])!=-1 && /[+%&#]/.test(m.content)){
		data.deleteChannels.push(m.channel.id);
		m.channel.send("Your command was deleted for using URL escape characters```"+m.content.replace(/`/g, "`\u200b")+"```There is a chance I deleted the wrong response by NSB, in which case I'm sorry");
		m.delete();
	} else if (m.author.id==data.nsb.id && data.deleteChannels.indexOf(m.channel.id)!=-1){
		setTimeout(function(){
			// Deleting it immediately sometimes makes mobile discord keep showing it
			m.delete();
			data.deleteChannels.splice(data.deleteChannels.indexOf(m.channel.id), 1);
		}, 1000);
	} else if (data.pornCommands.indexOf(m.content.toLowerCase().split(" ")[0])!=-1 && m.content.toLowerCase().indexOf("senko")!=-1){
		data.deleteChannels.push(m.channel.id);
		m.channel.send("Not fucking impressed, buddy");
		m.delete();
	} else if (new Date().getTime()-data.lastNotFunny>1000*60*5 && data.memeChannels.indexOf(m.channel.id)!=-1 && (m.attachments.array().length!=0 || /\.(pnga?|jpe?g|gif|mp[34]|webm)$/.test(m.content.toLowerCase()))){
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
				role.setColor(data.colors[data.ci]);
			} catch (e) {console.log("Failed setting senko role color for ", guild.name)}
		}
		if (guild.id in data.serverRoles){
			for (roleId in data.serverRoles[guild.id]){
				role=guild.roles.find(x=>x.id==roleId);
				//console.log(role)
				if (role!=null){
					try {
						role.setColor(data.serverRoles[guild.id][roleId][data.serverRoleIndex%data.serverRoles[guild.id][roleId].length])
					} catch (e) {console.log("Failed setting role "+role.name+" color for "+guild.name)}
				}
			}
		}
	}
	data.serverRoleIndex=(data.serverRoleIndex+1)%data.serverRolePeriod;
	data.ci=(data.ci+1)%data.colors.length;
}
bot.login(process.env.senkobottoken);