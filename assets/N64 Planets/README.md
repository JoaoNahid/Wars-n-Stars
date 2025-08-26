N64 Planets
===========

Renders of planets in the style of the video game Star Fox 64, also known as Lylat Wars, or the Nintendo 64 more generally.

The planets are rendered in a retro style at a low resolution using deliberately primitive noise that is quite archaic-looking.

Provided are two folders containing renders with and without planetary rings. Each folder contains ten different planet variants. The planet variants are provided as sixty frames of animation of the planet rotating. The frames can be shown in sequence in a sprite in a video game engine.

The planets are given "pre-rendered" as 2D frames and not as 3D models so that a user can pretend that their game engine cannot handle live 3D rendering of a planet and needs to bake the model down to a sprite.

Also provided is the source Blender file, which can be used to create a custom planet, and a low-resolution starfield environment map.

Creating a custom planet
------------------------

To create a custom planet, load the source Blender file, then in the Blender scene, select the main "Planet" object, then go to the Shader Editor.

Edit the color stops of the shader node "Surface colors" to change the colors used.

Edit the properties of the "N64 Planet Noise" shader group to change how the surface noise is generated. "Seed" is the random seed of the noise. "Scale" is the overall scale of the noise. "Vertical scale" is a further vertical scaling of the noise.

To render a ringed planet, make the "Ring" object visible to the renderer and set the current camera to "Ringed camera". Conversely, to render an unringed planet, make the "Ring" object invisible and choose "Unringed camera". The camera can be switched in the Scene tab of the Data Editor.

When done creating a custom planet, on rendering as an animation under Render > Render Animation, sixty frames of rotation will be produced in an "Output" folder within the folder also containing the source file. Alternatively, you can produce a single frame if you don't need to animate the planet.

Enjoy!

Version
-------

1 (2025-3-5)

License
-------

CC0 (Public domain).

Credit as n64guy would be nice but is not necessary.