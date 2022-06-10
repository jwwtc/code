run("8-bit");
setAutoThreshold("Default no-reset");
setThreshold(70, 140, "raw");
//setThreshold(70,140);
setOption("BlackBackground", false);
run("Convert to Mask");