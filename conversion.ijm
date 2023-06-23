function conversion(img){
         image=inputDir +img;
         open(image);
         name=getTitle();
         saveName=outputDir + name;
         saveAs("Tiff", saveName);
         close();

}


// choose input folder
inputDir = getDirectory("Choose your input folder");
outputDir= getDirectory("Select your save folder");

// get files list
list=getFileList(inputDir);

// loop through all items in input directory
for (i=0; i<3; i++)
   conversion(list[i]);