Title: Dotfiles for peace of mind
Date: 2016-02-23 12:18
Author: Cathy Yeh
Category: Programming, Tools
Tags: bash, conda, dotfiles, emacs
Slug: dotfiles
Status: published
Attachments: wp-content/uploads/2016/02/dotfiles_header.png

Reinstalling software and configuring settings on a new computer is a pain. After my latest hard drive failure set the stage for yet another round of download-extract-install and configuration file twiddling, it was time to overhaul my approach. *"Enough is enough!"*

This post walks through

1.  how to back up and automate the installation and configuration process
2.  how to set up a minimal framework for data science

We'll use a [dotfiles repository](https://github.com/EFavDB/dotfiles) on Github to illustrate both points in parallel.

* * * * *

Dotfiles are named after the configuration files that start with a dot in Unix-based systems. These files are hidden from view in your home directory, but visible with a `$ ls -a` command. Some examples are `.bashrc` (for configuring the bash shell), `.gitconfig` (for configuring git), and `.emacs` (for configuring the Emacs text editor).

Let's provide a concrete example of a customization: suppose you have a hard time remembering the syntax to extract a file ("Is it tar -xvf, -jxvf, or -zxvf?"). If you're using a bash shell, you can define a function, `extract()` in your `.bashrc` file that makes life a little easier:

```  
extract() {  
if [ -f "$1" ]; then  
case "$1" in  
*.tar.bz2) tar -jxvf "$1" ;;  
*.tar.gz) tar -zxvf "$1" ;;  
*.bz2) bunzip2 "$1" ;;  
*.dmg) hdiutil mount "$1" ;;  
*.gz) gunzip "$1" ;;  
*.tar) tar -xvf "$1" ;;  
*.tbz2) tar -jxvf "$1" ;;  
*.tgz) tar -zxvf "$1" ;;  
*.zip) unzip "$1" ;;  
*.ZIP) unzip "$1" ;;  
*.pax) cat "$1" | pax -r ;;  
*.pax.Z) uncompress "$1" --stdout | pax -r ;;  
*.Z) uncompress "$1" ;;  
*) echo "'$1' cannot be extracted/mounted via extract()" ;;  
esac  
else  
echo "'$1' is not a valid file to extract"  
fi  
}  
```

So the next time you have to extract a file `some_file.tar.bz2`, just type `extract some_file.tar.bz2` in bash. (This example was found in this [dotfiles repo](https://github.com/webpro/dotfiles/blob/master/system/.function_fs#L23).)

The structure of my dotfiles takes after the [repo](https://github.com/webpro/dotfiles) described by Lars Kappert in the article ["Getting Started With Dotfiles"](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789#.eis4hwbff). However, my repo is pared down significantly, with minor modifications for my Linux Mint system (his is OS X) and a focus on packages for data science.

* * * * *

A framework for data science
----------------------------

This starter environment only has a few parts. We need a text editor -- preferably one that can support multiple languages encountered in data science -- and a way to manage scientific/statistical software packages.

### Components

The setup consists of:

-   [Emacs](https://www.gnu.org/software/emacs/) -- a powerful text editor that can be customized to provide an IDE-like experience for both python and R, while providing syntax highlighting for other languages, e.g. markdown, LaTeX, shell, lisp, and so on. (More on customizing Emacs in a future post.)
-   [Conda](http://conda.pydata.org/docs/) -- both a package manager and environment manager. Advantages:
    -   Packages are easy to install compared to pip, e.g. see a post by the [author of numpy](http://technicaldiscovery.blogspot.com/2013/12/why-i-promote-conda.html).
    -   Conda is language agnostic in terms of both managing packages and environments for different languages (as opposed to pip/virtualenv/venv). This feature is great if you use both python and R.
    -   Standard python scientific computing libraries like numpy, scipy, matplotlib, etc. are available in the conda repository.

I use the system package manager (i.e. `apt-get install ...`) to install a few packages like git, but otherwise rely on Conda to install Python (multiple versions are okay!), R, and their libraries.

I like how clean the conda installation feels. Any packages installed by Conda, as well as different versions of Python itself, are neatly organized under the `miniconda3` directory in my home directory. In contrast, my previous Linux setups were littered with software installations from various package managers, along with sometimes unsuccessful attempts to compile software from source.

### Workflow

My workflow with Conda follows this helpful [post](http://stiglerdiet.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/) by Tim Hopper. Each project gets its own directory and is associated with an environment whose dependencies are specified by an `environment.yml` file.

For example, create a folder for a project, my_proj. Within the project folder, create a bare-bones `environment.yml` file to specify a dependency on python 3 and matplotlib:

    name: my_proj
    dependencies:
    - python=3
    - matplotlib

Then, to create the conda environment named after that directory, run `$ conda env create` inside the my_proj directory. To activate the virtual environment, run `$ source activate my_proj`.

Activating a conda environment can be further automated with [autoenv](https://github.com/kennethreitz/autoenv). Autoenv automatically activates the environment for you when you `$ cd` into a project directory. You just need to create a `.env` file that contains the command to activate your environment, e.g. `source activate my_proj`, under the project directory.

Tim has written a convenient bash function, `conda-env-file` (see [below](#conda-env-file)), for generating a basic `environment.yml` file and `.env` file, which I've incorporated into my own dotfiles, along with autoenv. The order of commands that I type in bash then follows:

1.  `mkdir my_proj` # create project folder
2.  `cd my_proj` # enter project directory
3.  `conda-env-file` # execute homemade function to create environment.yml and .env
4.  `conda env create` # conda creates an environment "my_proj" that is named after the project directory (using environment.yml)
5.  `cd ..`
6.  `cd my_proj` # autoenv automatically activates environment (using the file .env) when you re-enter the directory

* * * * *

The dotfiles layout
-------------------

Below is the layout of the directories and files (generated by the `tree` command) in the [dotfiles repo](https://github.com/EFavDB/dotfiles).

    .
    ├── install
    │   ├── apt-get.sh
    │   ├── conda.sh
    │   ├── git.sh
    │   ├── install-emacs.sh
    │   └── install-miniconda.sh
    ├── install.sh
    ├── runcom
    │   ├── .bash_profile
    │   ├── .bashrc
    │   └── .profile
    └── system
        ├── env
        ├── functions
        └── path

### Configuration

There any number of dotfiles that can be configured (for example, see the collection [here](http://dotfiles.github.io/)), but this repo only provides customizations for the dotfiles `.profile`, `.bash_profile`, and `.bashrc` -- located in the directory, `runcom` (which stands for "run commands") -- that contain commands that are executed at login or during interactive non-login shell sessions. For details about the role of shell initialization dotfiles, see the [end](#aside) of this post.

Instead of putting all our customizations in one long, unwieldy dotfile, it's helpful to divide them into chunks, which we keep in the subfolder, `system`.

The files `env`, `functions`, `path` are sourced in a loop by the dotfiles in `runcom`. For example, `.bashrc` sources `functions` and `env`:

```  
for DOTFILE in "$DOTFILES_DIR"/system/{functions,env}; do  
[ -f "$DOTFILE" ] && . "$DOTFILE"  
done  
```

Let's take a look at the configurations in each of these files:  
 

**env** - enables autoenv for activating virtual environments

    [ -f /opt/autoenv/activate.sh ] && . /opt/autoenv/activate.sh

 

**functions** - defines a custom function, `conda-env-file`, that generates an `environment.yml` that lists the dependencies for a conda virtual environment, and a one-line file `.env` (not to be confused with `env` in the previous bullet point) used by autoenv. (In addition to pip and python, I include the dependencies ipython, jedi, and flake8 needed by my Emacs python IDE setup.)  
  
```  
function conda-env-file {  
# Create conda environment.yml file and autoenv activation file  
# based on directory name.  
autoenvfilename='.env'  
condaenvfilename='environment.yml'  
foldername=$(basename $PWD)

if [ ! -f $condaenvfilename ]; then  
printf "name: $foldername\ndependencies:\n- pip\n- python\n- ipython\n- jedi\n- flake8" > $condaenvfilename  
echo "$condaenvfilename created."  
else  
echo "$condaenvfilename already exists."  
fi

if [ ! -f $autoenvfilename ]; then  
printf "source activate $foldername\n" > $autoenvfilename  
echo "$autoenvfilename created."  
else  
echo "$autoenvfilename already exists."  
fi  
}  
```  
 

**path** - prepends the miniconda3 path to the PATH environment variable. For example, calls to python will default to the Miniconda3 version (3.5.1 in my case) rather than my system version (2.7).

    export PATH="/home/$USER/miniconda3/bin:$PATH"

 

Now, we're done with configuring the dotfiles in this repo (apart from Emacs, which is treated separately). We just have to create symlinks in our home directory to the dotfiles in `runcom`, which is performed by the shell script, `install.sh`:

```  
## ...

ln -sfv "$DOTFILES_DIR/runcom/.bash_profile" ~  
ln -sfv "$DOTFILES_DIR/runcom/.profile" ~  
ln -sfv "$DOTFILES_DIR/runcom/.bashrc" ~

## ...  
```

### Installation

In addition to setting up dotfiles symlinks, `install.sh` automates the installation of all our data science tools via calls to each of the scripts in the `install` subfolder. Each script is named after the mechanism of installation (i.e. `apt-get`, `conda`, `git`) or purpose (to install Miniconda and Emacs).

-   **apt-get.sh** - installs a handful of programs using the system package manager, including `build-essentials`, which is needed to compile programs from source. Also enables source-code repositories (not enabled by default in Linux Mint 17), to be used for compiling emacs from source.
-   **install-emacs.sh** - build Emacs 24.4 from source, which is needed for compatibility with the Magit plug-in (git for Emacs). At the time of writing, only Emacs 24.3 was available on the system repo.
-   **install-miniconda.sh** - [miniconda](http://conda.pydata.org/docs/) includes just conda, conda-build, and python. I prefer this lightweight version to the Anaconda version, which comes with more than 150 scientific packages by default. *A note from the Miniconda downloads page: "There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 based... the choice of which Miniconda is installed only affects the root environment. Regardless of which version of Miniconda you install, you can still install both Python 2.x and Python 3.x environments. The other difference is that the Python 3 version of Miniconda will default to Python 3 when creating new environments and building packages." (I chose Miniconda3.)*
-   **conda.sh** - Use conda to install popular scientific packages for python, R, some popular R packages, and packages for IDE support in Emacs.
-   **git.sh** - Install [autoenv](https://github.com/kennethreitz/autoenv) for working with virtual environment directories. Also clone the configurations from my [Emacs repo](https://github.com/frangipane/emacs).

* * * * *

### Conclusion

The [dotfiles repo](https://github.com/EFavDB/dotfiles) discussed in this post will remain in this minimal state on GitHub so that it can be easily parsed and built upon. It's the most straightforward to adopt if you are on a similar system (Linux Mint or Ubuntu 14.04), as I haven't put in checks for OSX. If you don't like Emacs, feel free to comment out the relevant lines in `install.sh` and `install/git.sh`, and replace with your editor of choice.

Also take a look at other collections of [awesome dotfiles](https://github.com/webpro/awesome-dotfiles) for nuggets (like the `extract()` function) to co-opt. And enjoy the peace of mind that comes with having dotfiles insurance!

* * * * *

### *Notes on shell initialization dotfiles*

The handling of the dotfiles .profile, .bash_profile, and .bashrc is frequently a source of [confusion](http://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile) that we'll try to clear up here.

For example, .profile and .bash_profile are both recommended for setting environment variables, so what's the point of having both?

**.profile**  
.profile is loaded upon login to a Unix system (for most distributions) and is where you should put customizations that apply to your whole session, e.g. environment variable assignments like `PATH` that are not specifically related to bash. .profile holds anything that should be (1) available to graphical applications -- like launching a program from a GUI by clicking on an icon or menu -- or (2) to `sh`, which is run by graphical [display managers](https://wiki.archlinux.org/index.php/display_manager) like GDM/LightDM/MDM when your computer boots up in graphics mode (the most common scenario these days). Note, even though the default login shell is bash in Ubuntu, the default system shell that is used during the bootup process in Ubuntu is [dash, not bash](https://wiki.ubuntu.com/DashAsBinSh), (`readlink -f /bin/sh` outputs `/bin/dash`).

Let's give a concrete example of case (1): the miniconda installer provides a default option to add the miniconda binaries to the search path in .bashrc: `export PATH="/home/$USER/miniconda3/bin:$PATH"`. Assuming you've used `conda` (not `apt-get`) to install python scientific computing libraries and have set the path in .bashrc, if Emacs is launched from an icon on the desktop, then Emacs plugins that depend on those libraries (e.g. `ein`, a plugin that integrates IPython with Emacs) will throw an error; since the graphical invocation only loads .profile, the miniconda binaries would not be in the search path. (On the other hand, there would be no problem launching Emacs from the terminal via `$ emacs`.) For this reason, it's preferable to add the miniconda path in .profile instead of .bashrc.

For changes to .profile to take effect, you have to log out entirely and then log back in.

**.bash_profile**  
Like .profile, .bash_profile should contain environment variable definitions. I haven't yet encountered a situation where a configuration can be set in .bash_profile that can't be set in .profile or .bashrc.

Therefore, my .bash_profile just loads .profile and .bashrc. Some choose to bypass .bash_profile entirely and only have .profile (which bash reads if .bash_profile or .bash_login don't exist) and .bashrc.

**.bashrc**  
Definitions of alias, functions, and other settings you'd want in an interactive command line should be put in .bashrc. .bashrc is sourced by interactive, non-login shells.

**login, non-login, interactive, and non-interactive shells**

-   To check if you're in a login shell, type on the command line `echo $0`. If the output is `-bash`, then you're in a login shell. If the output is `bash`, then it's not a login shell (see `man bash`).
-   Usually, a shell started from a new terminal in a GUI will be an interactive, non-login shell. The notable exception is OSX, whose terminal defaults to starting login shells. Thus, an OSX user may blithely sweep customizations that would ordinarily be placed in .bashrc -- like aliases and functions -- into .bash_profile and not bother with creating a .bashrc at all. However, those settings would not be properly initialized if the terminal default is changed to non-login shells.
-   If you ssh in or login on a text console, then you get an interactive, login shell.
-   More examples in [this StackExchange thread](http://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell/46856#46856).

This discussion might seem pedantic since you can often get away with a less careful setup. In my experience, though, what can go wrong will probably go wrong, so best to be proactive.
