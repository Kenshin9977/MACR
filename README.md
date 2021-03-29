# Marmoset AutoMAT CoD Renamer (MACR)

The purpose of this program is to allow the use of [AutoMAT](https://gumroad.com/l/AutoMAT), a Marmoset's plug-in. 
## Features

This plug-in auto-assigns textures to their corresponding material but to work, textures need to have a naming convention. Because Treyarch hash the name of their files since Black Ops 4, you can't really do that and have to refer to the mtl.  This program rename the relevant textures of a material to by the name of the material plus a suffix that will allow AutoMAT to work. 
It uses the mtl files
## Downloads

Binaries for Windows are available in the [releases](https://github.com/Kenshin9977/MACR/releases) section.
## Usage

Launch the MACR.exe anywhere you want and give it the full path of the folder where you have the mtl files. It will rename the files pretty fast. Within AutoMAT you need to put the following suffix :
* Color: c
* AO: o
* Normal: n
* Roughness: g
* Spec: s
* Emissive: e