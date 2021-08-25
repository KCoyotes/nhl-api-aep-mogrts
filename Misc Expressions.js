// Warp Settings
thisComp.layer("CONTROLS").effect("Warp Amount")("Slider")
thisComp.layer("CONTROLS").effect("Warp Size")("Slider")
time * Math.floor(thisComp.layer("CONTROLS").effect("Warp SPEED")("Slider").valueAtTime(0))

// Source Text
x = thisComp.layer("CONTROLS").effect("Width")("Slider").valueAtTime(0)
y = thisComp.layer("CONTROLS").effect("Height")("Slider").valueAtTime(0)
if(thisComp.layer("CONTROLS").effect("Space Text")("Checkbox") == 0)
	textField = thisComp.layer("COYOTES").text.sourceText;
else textField = thisComp.layer("COYOTES").text.sourceText + " "

textReady = textField.repeat(x) + "\n"
wideText = textReady.repeat(y)

wideText

// Animators

    // Sets how frequently the RNG runs
posterizeTime(Math.floor(thisComp.layer("CONTROLS").effect("Random Highlight Frequency")("Slider").valueAtTime(0))*2);
    // Imports number of words horizontally and vertically
height = Math.floor(thisComp.layer("CONTROLS").effect("Height")("Slider").valueAtTime(0))
width = Math.floor(thisComp.layer("CONTROLS").effect("Width")("Slider").valueAtTime(0))

numberOfWords = height * width

wordHighlighter = Math.floor(random(numberOfWords))

if(textIndex === wordHighlighter) {
 100;
} else {
 0;
}

a = thisComp.layer("CONTROLS").effect("Text Sliding Amplitude")("Slider");
const {width, height} = sourceRectAtTime()
amp = (width - 1280) / 2
f = (thisComp.layer("CONTROLS").effect("Text Sliding Frequency")("Slider") / 100);
x = Math.sin(time*2*Math.PI*f)*amp;
y = value[1];

[x,y]


// Anchor Points
const {width, height, left, top} = sourceRectAtTime(0);
[left + width / 2, top + height / 2]


// Position
const {width, height} = sourceRectAtTime(0)

singleWordWidth = width / Math.floor(thisComp.layer("CONTROLS").effect("Width")("Slider").valueAtTime(0))
x = (time * 100) % singleWordWidth
y = value[1];

[x,y]

// Jersey Number Auto Scroller
eval("var JSON=" + footage("API_Stats.json").sourceText);

changer = Math.floor(time) + 1;

JSON.teams[changer].primaryNumber;