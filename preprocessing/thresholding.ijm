run("8-bit");
setAutoThreshold("Default no-reset");
setThreshold(55, 120, "raw");
//setThreshold(55, 120);
setOption("BlackBackground", false);
run("Convert to Mask");