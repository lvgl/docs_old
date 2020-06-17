```eval_rst
.. include:: /header.rst 
:github_url: |github_link_base|/contribution/index.md
```

# Contributing


## Introduction

Join LVGL's community and leave your footprint in library!

There are lot of ways to contribute to LVGL even if your are new to library or even new to programming. 

It might be scary to make the first step but you have nothing to afraid of. 
A friendly and helpful community is waiting to know like minded people and make something great together.

So let's find which contribution option fits you the best and join the development of LVGL!

Before getting started here are some guidelines to make contribution smoother:
- Be kind and friendly. 
- Be sure to read the relevant part of the documentation before posting a question.
- Ask questions in [Forum](https://forum.lvgl.io/) and use [GitHub]((https://github.com/lvgl/) for development-related discussions.
- Fill the post or issue templates in the Forum or GitHub. It makes much easier to understand your case and you will get a useful answer faster. 
- If possible send an absolute minimal but build-able code example in order to reproduce the issue. Be sure it contains all required the variable declarations, constants and assets (images, fonts).
- Use [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to format your posts. You can learn it in 10 minutes.
- Speak about one thing in one issue or topic.
- Give feedback and close the issue or mark the topic as solved if your question is answered. 
- For non-trivial fixes and features it's better open an issue first to discuss the details instead of sending a pull request directly.
- Please read and follow the [Coding style](https://github.com/lvgl/lvgl/blob/master/docs/CODING_STYLE.md) guide.


### DCO

### Pull request


Merging new code into lvgl, documentation, blog, examples and other repositories happens via *Pull requests* (PR for short).
A PR is a notification like "Hey, I made some updates to your project. Here are the changes, you can added them if you want.*
To do this you need a copy (called fork) of the original project under your account, make some changes there, and notify the original repository about your updates. 
You can see how it looks like on GitHub for lvgl here: https://github.com/lvgl/lvgl/pulls

To add your changes you can edit files online on GitHub and send a new Pull request from there (recommended for small changes) or
 add the updates in your favorite editor/IDE and use git to publish the changes (recommended for more complex updates).

#### From GitHub
1. Navigate to the file you want to edit.
2. Click the Edit button in the top right-hand corner.
3. Add your changes to the file
4. Add a commit message on the bottom of the page
5. Click the *Propose changes* button

#### From command line

It's about the `lvgl` repository but it works the same way for other repositories too.
1. Fork the [lvgl repository](https://github.com/lvgl/lvgl). To do this click the "Fork" button in the top right corner. 
It will "copy" the `lvgl` repository to your GitHub account (`https://github.com/<YOUR_NAME>?tab=repositories`)
2. Clone  your forked repository.
3. Add your changes. You can create a *feature branch* from *master* for the updates: `git checkout -b the-new-feature` 
4. Commit and push you changed to the forked `lvgl` repository.
5. Create a PR on GitHub from the page of your `lvgl` repository (`https://github.com/<YOUR_NAME>/lvgl`) by clicking the *"New pull request"* button. Don't forget to select the branch where you added your changes.
7. Set the base branch. It means where you want to merge your update. In the `lvgl` repo fixes go to `master`, new features to `dev` branch. 
8. Describe what is in the update. An example code is welcome if applicable.
9. Update** your `lvgl` repo with new commits. They will automatically appear in the PR too.



## When you got started with LVGL

Even if you're just got started with LVGL there plenty of ways to make your feet wet. Most of these options even doesn't required to know a single line of code of LVGL. 

### Give LVGL a Star

Show that you like LVGL by giving it star on GitHub!
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/lvgl/lvgl" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star lvgl/lvgl on GitHub">Star</a>

This simple click makes LVGL more visible on GitHub and makes it more attractive to other people. 
So with this you already helped a lot! 

### Tell what you have achieved

Have you already started LVGL in a [Simulator](/get-started/pc-simulator), a development board or you custom hardware? 
Was it easy or where there some obstacles? Are you happy with the result?

If so why don't you tell it to your friends? You can post it on Twitter, Facebook, LinkedIn or create a YouTube video.

Any of these helps a lot to spread the word of LVGL and familiarize it with new developers.

Only thing: don't forget to add a link to https://lvg.io or https://github.com/lvgl and #lvgl. Thank you! :) 

### Write examples
As you learn LVGL probably you will play with the features of widgets. But why don't you publish your experiments?

Every widgets' documentation contains some examples. For example here are the examples of the [Drop-down list](/widgets/dropdown.html#example). 
The examples are directly loaded from the [lv_examples](https://github.com/lvgl/lv_examples/tree/master/src/lv_ex_widgets) repository. 

So all you need to do is sending a [Pull request](/contributing/index.html#pull-request) to the [lv_examples](https://github.com/lvgl/lv_examples/tree/master/src/lv_ex_widgets) repository and follow some conventions:
- Name the examples like `lv_ex_<widget_name>_<id>`
- Make the example as short and simple as possible
- Add comments to explain what the example does
- Use 320x240 resolution
- Create a screenshot about the example 
- Update `index.rst` in the example's folder with your new example. See how the other example are added.


### Improve the docs

As you read the documentation you might see some typos or unclear sentences. 
For typos and straightforward fixes you can simply edit the file on GitHub. There is an `Edit on Github` link on the top right-hand corner of all page.
Click it to see the file on GitHub, hit the Edit button and add you fixes as described in [Pull request - From GitHub](/contributing/index.html#from-github) section.

Note that, the documentation is also formatted in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). 

### Translate the docs

If you have more free time you can even translate the documentation. If your chosen language is still not added, please write a post 


- Get started section
- Overview : Objects, Events, Styles
- Porting: System overview, Set-up a project, Display interface, Input device Interface, Tick interface
- 5 widgets of your choice

### Write a blog post


## When you already use LVGL

### Give feedback

### Report bugs

### Send fixes

### Add features

### Join the conversations in the Forum



## When you are confident with LVGL

### Become a maintainer

### Garden your repo under LVGL organization

## Summary

Looking forward to see your first Pull request or post! :) 

