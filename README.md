# Week 2

In this week's lectures we discussed the process of trying to understand unfamiliar software systems, and to start to identify potentially problematic aspects of the design or architecture.

For this lab, we'll carry out this range of steps on an unfamiliar software system. In contrast to the lecture-time however, we'll utilise some tools to help us.

## A note on the choice of subject system

This week we'll focus on the CovaSim project we have covered previously. Once you have managed to get it working on this system, try the steps with your own choice of system!

You'll eventually be required to retrace these steps on your group project.

## Setup

1. Clone the repository.
2. Set up and activate a virtual environment.
3. Install the requirements.

In order to install the pydeps requirement, you may need to add the conda-forge repository:

```bash
conda config --add channels conda-forge
```

For the remainder of steps, you can either use PyCharm (see last week's steps). Or you can do the same using the terminal.

```bash
git clone THIS_REPO
cd THIS_REPO
python3 -m venv venv  # or python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## Steps

1. Run the steps to create the word-cloud from the docs within the Jupyter Notebook.
2. For the word-cloud, some of the words included are unhelpful and get in the way. Find out which statement in the Jupyter Notebook you can tweak to add stop-words.
3. In the prep-work and lecture-time we started off a table that mapped concepts to source code classes. Revisit this, and add any additional concepts that appear important within the word-cloud.
4. Run the final part of Jupyter notebook (running PyDeps). This should provide you with an overview of the dependencies between the modules. Write down any conclusions you draw about potential issues around coupling, and where they may arise.
