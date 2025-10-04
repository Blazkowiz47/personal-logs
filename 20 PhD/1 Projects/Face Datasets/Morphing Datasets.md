
All the morphing datasets are stored in FaceMorphingDatabases directory
NBL-Windows cluster have following face morph databases:
1. [[FRGC]]
2. [[FERET]]
3. [[ABC Database]]
4. [[Post Process]]
5. [[GU Morph]]
6. [[Infant morph]]
7. [[SCFace]] 
8. [[Frill]] 

### Organization of databases: 
	Each dataset will have following structure:
	1. Raw
	2. Aligned
	3. Bonafide
	4. Morph
	    1. morph-type-1
	    2. morph-type-2

All of these folders will have _test_ and _train_ sub-directories which will have all the images in it.
##### Important things: 
	Raw, can have any type of files.
	Aligned will have png files
	Bonafide and Morphs will have jpg files
	