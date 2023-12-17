# Frequently Asked Questions

#### Can I add any image to the intro or outro?

- As long as you can provide the proper attribution for an image you can use it in your project.

#### I have an older, less powerful, computer, will it handle running this workbench?

- If you open the standard QGIS settings dialog and select the Animation Workbench options
you can follow the advice with regards to lowering the number of threads allowed during
rendering to help you computer cope. Rendering shorter movies or GIFs (i.e. fewer frames)
will also help. Below is an example of running a job with 9000 frames at 60fps and 999
frames per feature

![imagem](https://user-images.githubusercontent.com/178003/159691009-8a8485f0-2bf0-419f-9dd4-a71c207b9117.png)

And the subsequent CPU load during processing:

![cpu](https://user-images.githubusercontent.com/178003/159691200-18dfea74-ac11-4620-9def-803b9c61c98d.png)

After processing:

![imagem](https://user-images.githubusercontent.com/178003/159691416-7cd5c4bf-ad47-4943-9008-bd04b7bf4ef9.png)

And here is the resulting video:

<https://youtu.be/1quc3xPdJsU>

#### I get an error when rendering because of my intro / outro images

Currently your filenames should not contain spaces or special characters (e.g.(, ), [, ], {, }, <, >, /, \, :, *, ?, |, ", &, etc.).

#### Can I use a movie as the intro / outro media?

This is planned but not yet implemented. Tim - check.

#### Can I pay you to add some features?

This is a fun / hobby project, currently we want other contributors who also want to
have a fun experience with building this plugin and contribute in-kind efforts to the
project. Both [Kartoza](https://kartoza.com) and [North-Road](https://north-road.com/)
offer commercial development services but not for this plugin which is a intended to
provide an experimental, no-pressire space for us to work on something fun for QGIS.
