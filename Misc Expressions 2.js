// Previous Expressions used to access data from .csv spreadsheets generated from Sportsipy
footage("Clayton Keller.csv").dataValue([43,thisComp.layer("Clayton Keller.csv")("Effects")("Spreadsheet Row")("Slider")-1])

yearrow = "year " + Math.floor(thisComp.layer("Clayton Keller.csv")("Effects")("Spreadsheet Row")("Slider"));
thisComp.layer("Clayton Keller.csv")("ADBE Data Group")("Outline")("year")(yearrow)

shots_on_goalrow = "shots_on_goal " + (Math.floor(thisComp.layer("Clayton Keller.csv")("Effects")("Spreadsheet Row")("Slider")) - 1);
thisComp.layer("Clayton Keller.csv")("ADBE Data Group")("Outline")("shots_on_goal")(shots_on_goalrow)

shots_on_goalrow = "shots_on_goal " + Math.floor(thisComp.layer("Clayton Keller.csv")("Effects")("Spreadsheet Row")("Slider"));
thisComp.layer("Clayton Keller.csv")("ADBE Data Group")("Outline")("shots_on_goal")(shots_on_goalrow)

pointsrow = "points " + Math.floor(thisComp.layer("Clayton Keller.csv")("Effects")("Spreadsheet Row")("Slider"));
thisComp.layer("Clayton Keller.csv")("ADBE Data Group")("Outline")("points")(pointsrow)

values = [];for(i=0;i<=thisComp.layer("Scoreboard2.csv")("ADBE Data Group")("ADBE DataLayer Num Rows")-1;i++) {     values.push(thisComp.layer("Scoreboard2.csv")("ADBE Data Group")("Outline")("Stat Data 01")("Stat Data 01 " + i).value); } values.join("\n");




a = thisComp.layer("CONTROLS").effect("Text Sliding Amplitude")("Slider");
const {width, height} = sourceRectAtTime()
amp = (width - 1280) / 2
f = (thisComp.layer("CONTROLS").effect("Text Sliding Frequency")("Slider") / 100);
x = Math.sin(time*2*Math.PI*f)*amp;
y = value[1];

[x,y]




{
    playernumber = (thisComp.layer("Player Number").text.sourceText).value

i=0

findrow = thisComp.layer("2020-2021 Arizona Coyotes Player Season Totals - Natural Stat Trick.csv")("Data")("Outline")("Number")("Number " + i)



result = i
text.sourceText = result
}



const {width, height} = sourceRectAtTime(0)

singleWordHeight = height / Math.floor(thisComp.layer("CONTROLS").effect("Height")("Slider").valueAtTime(0))
x = value[0];
y = (time * 100) % singleWordHeight

[x,y]

const {width, height} = sourceRectAtTime(0)

singleWordWidth = width / Math.floor(thisComp.layer("CONTROLS").effect("Width")("Slider").valueAtTime(0))
x = (time * 100) % singleWordWidth
y = value[1];

[x,y]

team[0]['person']['id']