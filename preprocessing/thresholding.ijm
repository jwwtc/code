run("8-bit");
setAutoThreshold("Default dark no-reset");
//run("Threshold...");
call("ij.plugin.frame.ThresholdAdjuster.setMode", "B&W");
//setThreshold(29, 120);
setOption("BlackBackground", false);
run("Convert to Mask");