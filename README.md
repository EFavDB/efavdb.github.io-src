# Source for generating html pages served by efavdb's github page


## One time setup

### Clone the repo and initialize the submodules

```shell
git clone git@github.com:EFavDB/efavdb.github.io-src.git
cd efavdb.github.io-src/

ls output 
# should show empty, as well as elegant-theme and pelican-plugins

git submodule update --init --recursive
# now those same dirs should no longer be empty
```


Below is optional now that publishing to github happens automatically with PR merge.  
Feel free to skip.
```shell
cd output
git remote -v
# should show
# origin    https://github.com/efavdb/efavdb.github.io.git (fetch)
# origin    https://github.com/efavdb/efavdb.github.io.git (push)

git branch # should show detached

git checkout master  # check out master branch of the submodule
# verify it’s master of the submodule still, not of the efavdb.github.io-src repo
git remote -v
```

### Set up your pelican environment

We need this to build the site
```shell

cd ~/path/to/project-root-of-efavdb.github.io-src

pip install pipenv # if you don’t already have pipenv
pipenv install  # set up the env
pipenv shell # activate the environment

# check env works
make devserver
# see the dev version of the site at http://localhost:8000/
```


## Developing

- The markdown articles are located under `content/`.  Feel free to
  place WIP drafts in `content/articles/drafts` for easy tracking, but
  technically, you can put them anywhere and they won't be published
  unless you specify their status as such (default is `draft`) in the
  article metadata.
- New images should be placed under `content/images/` as opposed to
  `content/wp-content/...`.  The latter made sense to keep as part of
  the migration from WordPress, but we don't need to keep adding to it
  with new articles written outside of WordPress.

### Changes that don't require modifications to elegant theme, e.g. putting up a new article

From the root of the project:
- Activate the environment `pipenv shell`
- Turn on the development server `make devserver`
- Open up the dev website at http://localhost:8000/
- Make your changes to the `content/` dir, where the articles are
  located. Verify your changes are picked up on the dev website.
- Note, Disqus comments won't be visible in dev mode because Disqus
  requires absolute URLs.
- If you want to check the published version of the site (uses
  absolute URLs, which you can see in page source links), run:
  - `make publish`
  - `make serve` -- see site at localhost:8000.
- Open a PR with your content changes.  When you merge the PR, changes
  will automatically be published to github pages.  (Thanks Damien!)



### DEPRECATED steps for manual publishing to github pages

The files in the `output/` subdir should have been automatically
regenerated in development mode.

Push the html changes to github pages.

```shell
cd output

# make sure you're pointing to the github pages repo and on master branch 
git remote -v
git branch

# add changes and push to master on github pages
git add -A
git commit -m "new pages"
git push

# check the new html pages were pushed to master:
# look at https://github.com/EFavDB/efavdb.github.io

# now you need to update the submodule in the efavdb.github.io-src repo
cd ~/path/to/project-root-of-efavdb.github.io-src

git status  # should show output directory is changed
git diff output  # should show change from old sha to the sha of latest commit on efavdb.github.io
git add output
git commit -m "Update output submodule"
```


### Changing CSS for the elegant theme

This is more involved -- you'll need to install additional packages,
so don't bother unless you specifically want to edit the style sheets.

https://elegant.oncrashreboot.com/use-postcss-to-compile-css-style-sheets 


## References

[Pelican docs](http://docs.getpelican.com/en/3.6.3/index.html) -- tells you have to modify config, etc

[Elegant theme](https://elegant.oncrashreboot.com/) -- the theme we're
currently using, includes features we might not have turned on yet


### CAVEATS

The Pelican docs mention ways to modify theme templates and style
sheets without having to actually fork the theme and modify it
directly, e.g. by using `pelicanconfg.py` and setting env vars like
`THEME_TEMPLATES_OVERRIDE`.  I could not get that to work with this
particular elegant theme, so we are **indeed** modifying the fork of
the theme currently, which is not best practices.

In particular, the elegant theme has an extra style sheet compilation
step which is not compatible with the default way of simply overriding
via using a custom.css file in our `content/` folder.
