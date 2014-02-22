Mechanical Turk Image Style Classification
==========================================

This project is bulid on top of [flask_heroku][], with some modifications.

[flask_heroku]:   http://github.com/zachwill/flask_heroku

The instructions assume you have the following installed and configured:

- [Anaconda][]
- [Homebrew][]
- [Heroku toolbelt][]

[Anaconda]: http://continuum.io/downloads
[Homebrew]: http://brew.sh
[Heroku toolbelt]: https://toolbelt.heroku.com/   

Perform the basic setup instructions found in the following sections of that project's `README.md` before proceeding below:

Setup Instructions
------------------

First, you'll need to clone the repo.

    $ git clone git@github.com:matttrent/mturk-image-style.git
    $ cd mturk-image-style

Second, install some ruby gems

  $ sudo gem install foreman heroku

Since we're doing science-y stuff, we'll to the [Anaconda][] and use `conda` to configure our virtual environment

    $ conda create -n mturk-image-style pip
    $ source activate mturk-image-style

Remaning Setup Instructions
---------------------------

Follow the following portions of [flask_heroku][]'s `README.md`

- Installing Packages
- Running Your Application

You'll also need to follow the steps in Deploying to get the app onto heroku.
