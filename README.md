##![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  SEA-DAT2 course repository
###General Assembly Data Science course
**Location:** Seattle, WA
<br><b>Class times:</b> Classes: 6:30pm - 9:30pm</br>
<b/>Instructor:</b> <a href="https://www.linkedin.com/profile/view?id=ADEAAAEai9UBI1CGmAPFMYpURJeL9zvxWX6xBqI">Jim Byers</a>

**Note:** Prior to the first day of class complete the 10-15 hours of pre-work in order to be properly prepared for class [(prework)](https://gist.github.com/kevinmcalear/9e5625d5eac58fe35de8#account)

Tuesday | Thursday
--- | ---
**Research Design and Exploratory data analysis**|
3/15: [L01 Introduction to Data Science](#class-1) | 3/17: [L02 Research design and Pandas](#research-design)
3/22: [L03 Statistics fundamentals](#stat_fund) | 3/24: [L04 Command Line and Version Control](#command-line)
3/29: [L05 Fetching Data](#fetching-data), **Project Discussion Deadline** |
**Foundations of data modeling**|
 | 3/31: [L06 Intro to Regression](#intro-to-regression), **Project Question and Dataset Due**
4/5: [L07 Intro to Classification - K nearest neighbor](#knn) | 4/7: [L08 Evaluating Model Fit](#evaluating-fit)
4/12: [L09 Classifying with Logistic Regression](#logistic-regression) | 4/14: [L10 Advanced model evaluation](#advanced_model)
4/19: [L11 Regularization and Clustering](#class-11-regularization-and-clustering)| 4/21: L12: **First Project Presentations** + bonus topics
**Data science in the real world**|
4/26: [L13 Natural Language Processing](#nlp) | 4/28: L14 Dimensionality reduction, **Draft Paper Due**
5/3: [L15 Decision Trees](#decision) | 5/5: [L16 Ensembling, Bagging and Random Forests](#ensemble)
5/10: L17 Modeling with Time Series Data I, **Peer Review Due** | 5/12 L18 Modeling with Time Series Data II
5/17: L19 Where to go next + bonus topics | 5/19: **Final Project Presentations**

## Submission Forms

#### [      Exit ticket form](https://docs.google.com/forms/d/1ccyiiym4XpQB65SbuZX7MYgI-WZKBPIPJNbRI-2SsPY/viewform)
<!--
(https://docs.google.com/a/generalassemb.ly/forms/d/10L0tgB2X70bIHAzb1d0_4guWmCEqxavhQAHM1t1I4-Y/viewform)
-->
####   [Homework and project submissions form] (https://docs.google.com/forms/d/1vKgdubWdc-AzMTYS6f6uTFwQDop3M9uUNbilcuziTQA/viewform?usp=send_form)
<!--
(https://docs.google.com/forms/d/1S82LIibhiG2olZQb2C7iboqN5rb8wB6mQLFBg992eh4/viewform?usp=send_form)
-->
* [Homework Evaluation Criteria](https://docs.google.com/spreadsheets/d/19XaVllCETEWyROSMHIShVWgUqK-kbZkvSeCzjK7yezI/edit?usp=sharing)
 &nbsp;

-----

## Other resources

#### [Office hours](other/office_hours.md)

#### [Machine learning estimator selection - a diagram](http://3.bp.blogspot.com/-dofu6J0sZ8o/UrctKb69QdI/AAAAAAAADfg/79ewPecn5XU/s1600/scikit-learn-flow-chart.jpg)

<!-- #### [Office hrs](/other/office_hours)
#### [Machine learning model comparison](/other/model_comparison.md) -->

 &nbsp;

-----

<a name="class-1"></a>
### Class 1: Lets get rolling! - Intro to Data Science

**Student Prework**
Before this lesson you should already be able to:
* Define basic data types used in object-oriented programming
* Recall the Python syntax for lists, dictionaries, and functions
* Create files and navigate directories using the command line interface (for your specific environment)

**After this lesson, you will be able to:**
* Describe the roles and components of a successful learning environment
* Define data science and the data science workflow
* Apply the data science workflow to meet your classmates
* Setup your development environment and review python basics

**Topics/Highlights**
* Welcome from General Assembly!
* Course overview ([slides](slides/01_course_overview.pdf))
* What is data science ([slides](slides/01_data_science_intro.pdf))
	* Data Science Quiz
* Data Science workflow ([slides](slides/01_data_science_intro.pdf))
	* [Exercise (Apply the workflow)](other/workflow_exercise.md)
* Hands-on with the Data Science Dev Environment (Anaconda, Spyder IDE, iPython notebooks)
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md)
	* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
	* [GA's student gallery of projects](https://gallery.generalassemb.ly)
		* Our very own Kevin McAlear's [Hater News DAT project](http://haternews.co/?network=twitter) on the GA gallery

**Homework:**
* Due Mar 17
	* Read through the information about the course project information to familiarize yourself with the [requirements](project/README.md) and [example projects](/project/project_examples/README.md).  Start thinking about what question you would like to answer in your project.
		* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
* Due Tuesday March 22
	* Review each concept and each line of code in these files of python code: [00_python_beginner_workshop.py](code/00_python_beginner_workshop.py) and [00_python_intermediate_workshop.py](code/00_python_intermediate_workshop.py). Complete the coding exercises in the files: If you don't feel comfortable with any of the content (excluding the "requests" and "APIs" sections), you should spend some time before Mar 22nd practicing Python.  Use your resources such as documentation, searches, the class Slack to get help if you get stuck.  Here are some additional resources:
	    * [Introduction to Python](http://introtopython.org/) does a great job explaining Python essentials and includes tons of example code.
	    * If you like learning from a book, [Python for Informatics](http://www.pythonlearn.com/html-270/) has useful chapters on strings, lists, and dictionaries.
	    * If you prefer interactive exercises, try these lessons from [Codecademy](http://www.codecademy.com/en/tracks/python): "Python Lists and Dictionaries" and "A Day at the Supermarket".
	    * If you have more time, try missions 2 and 3 from [DataQuest's Learning Python](https://www.dataquest.io/course/learning-python) course.
	    * If you've already mastered these topics and want more of a challenge, try solving [Python Challenge](http://www.pythonchallenge.com/) number 1 (decoding a message)

**Resources:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* Quora has a [data science topic FAQ](https://www.quora.com/Data-Science) with lots of interesting Q&A.

-----

<a name="research-design"></a>
### Class 2: Research Design and Pandas
**Student pre-work**
Before this lesson, you should already be able to:
* Have completed the python pre-work in the class pre-work described [here](https://gist.github.com/kevinmcalear/9e5625d5eac58fe35de8#account)

<!-- * Create, open, create and shutdown an IPython Notebook-->

**After this lesson, you will be able to:**
* Define a problem and types of data
* Identify data set types
* Define the data science workflow
* Apply the data science workflow in the pandas context
* Write an IPython Notebook to import, format and clean data using the Pandas Library

**Topics/Highlights**
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md)
* The why's and how's of a good question ([slides](slides/02-experimental-design-and-pandas.pdf))
* Types of datasets ([slides](slides/02-experimental-design-and-pandas.pdf))
* Write a research question with raw data (exercise)
* Data science workflow steps 2. Acquire and 3. Understand the data
* Acquire and Understand data with Pandas 
	* Pandas concepts ([slides](slides/02-experimental-design-and-pandas.pdf))
	* Pandas codealong ([notebook](notebooks/02_numpy_and_pandas.ipynb))
	* Independent Practice ([notebook](notebooks/02_starter_code.ipynb))
 
**Homework:**
* Due Tuesday March 22
	* To turn in homework,  attach files to a personal message in Slack to Jim Byers and Kevin Mcalear 
	* Review each concept and each line of code in these files of python code: [00_python_beginner_workshop.py](code/00_python_beginner_workshop.py) and [00_python_intermediate_workshop.py](code/00_python_intermediate_workshop.py). Complete the coding exercises in the files: If you don't feel comfortable with any of the content (excluding the "requests" and "APIs" sections), you should spend some time before Mar 22nd practicing Python.  Use your resources such as documentation, searches, the class Slack to get help if you get stuck.  Here are some additional resources:
	    * [Introduction to Python](http://introtopython.org/) does a great job explaining Python essentials and includes tons of example code.
	    * If you like learning from a book, [Python for Informatics](http://www.pythonlearn.com/html-270/) has useful chapters on strings, lists, and dictionaries.
	    * If you prefer interactive exercises, try these lessons from [Codecademy](http://www.codecademy.com/en/tracks/python): "Python Lists and Dictionaries" and "A Day at the Supermarket".
	    * If you have more time, try missions 2 and 3 from [DataQuest's Learning Python](https://www.dataquest.io/course/learning-python) course.
	    * If you've already mastered these topics and want more of a challenge, try solving [Python Challenge](http://www.pythonchallenge.com/) number 1 (decoding a message)
	

**Resources:**

Python resources

* [Want to understand Python's comprehensions? Think in Excel or SQL](http://blog.lerner.co.il/want-to-understand-pythons-comprehensions-think-like-an-accountant/) may be helpful if you are still confused by list comprehensions.
* [My code isn't working](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/624506_orig.png) is a great flowchart explaining how to debug Python errors.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) is Python's "classic" style guide, and is worth a read if you want to write readable code that is consistent with the rest of the Python community.
* If you want to understand Python at a deeper level, Ned Batchelder's [Loop Like A Native](http://nedbatchelder.com/text/iter.html) and [Python Names and Values](http://nedbatchelder.com/text/names1.html) are excellent presentations.

Pandas resources

Name | Description
--- | ---
[Official Pandas Tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html) | Wes & Company's selection of tutorials and lectures
[Julia Evans Pandas Cookbook](https://github.com/jvns/pandas-cookbook) | Great resource with eamples from weather, bikes and 311 calls
[Learn Pandas Tutorials](https://bitbucket.org/hrojas/learn-pandas) | A great series of Pandas tutorials from Dave Rojas
[Research Computing Python Data PYNBs](https://github.com/ResearchComputing/Meetup-Fall-2013/tree/master/python) | A super awesome set of python notebooks from a meetup-based course exclusively devoted to pandas

-----

<a name="stat_fund"></a>
### Class 3: Statistics fundamentals
**By the end of this lesson you will be able to:**
* Use NumPy and Pandas libraries to analyze datasets using basic summary statistics: mean, median, mode, max, min, quartile, inter-quartile range, variance, standard deviation, and correlation
* Create data visualizations - including: line graphs, box plots, and histograms- to discern characteristics and trends in a dataset
* Identify a normal distribution within a dataset using summary statistics and visualization

**Topics/Highlights**
* Review Homework
	* [00_python_beginner_workshop.py](code/00_python_beginner_workshop.py)
	* [00_python_intermediate_workshop.py](code/00_python_intermediate_workshop.py)
	* Independent Practice [(02_starter_code.ipynb)](notebooks/02_starter_code.ipynb)
* Statistics refresher
	* Basic Statistics with Pandas
		* Statistics Fundamentals [(slides)](slides/03_statistics_fundamentals.pdf)
		* Code-along [(notebook)](notebooks/03_basic_stats.ipynb)
		* Stats demo [(notebook)](notebooks/03_statistics_demo.ipynb)
	* Correlation
		* What is correlation? [(slides)](https://github.com/JamesByers/GA-SEA-DAT2/blob/master/slides/03_correlation.pdf)
			* Correlation is not causation (fun with a commom misconception!)
		* Visualization with Pandas [(notebook)](notebooks/03_correlation_exercise_ice_cream_and_car_data.ipynb)

**Homework:**
* Due Tuesday March 24
	* *Windows users*, install [Git Bash](http://git-scm.com/download/win) prior to starting the command line pre-class exercise*** as you will need the "bash" type command window on your Windows laptop in order to do the exercise and later to use git
		* We recommend Git Bash instead of Git Shell (which uses Powershell).
		* For Mac users, you will probably be using Terminal, or another command line application of your choice.  It already is a bash type command line interpreter.  No need to load anything.  Git is part of the MAC OS so is already installed and ready to use.
	* Complete GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows)
	* Complete the command line pre-class exercise ([code](code/04_command_line_basics.md)).  You do not need to turn in this homework
	* Find one link to a resource about statistics that you find especially useful and send it in a slack message to Jim and Kevin.  Note this will not be graded against the [homework evaluation criteria](https://docs.google.com/spreadsheets/d/19XaVllCETEWyROSMHIShVWgUqK-kbZkvSeCzjK7yezI/edit?usp=sharing).  Jim will share these links back out on our repo so all can benefit.

**Statistics Resources:**
* [Descriptions of Statistics terms in a straight forward way](http://stattrek.com/statistics/dictionary.aspx?definition=Probability_density_function) including density plot

**Pandas Resources:**
* To learn more Pandas, read this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/), or review these two excellent (but extremely long) notebooks on Pandas: [introduction](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb) and [data wrangling](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb).
* If you want to go really deep into Pandas (and NumPy), read the book [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do), written by the creator of Pandas.

<!-- * This notebook demonstrates the different types of [joins in Pandas](notebooks/05_pandas_merge.ipynb), for when you need to figure out how to merge two DataFrames. -->
* This is a nice, short tutorial on [pivot tables](https://beta.oreilly.com/learning/pivot-tables) in Pandas.
* For working with geospatial data in Python, [GeoPandas](http://geopandas.org/index.html) looks promising. This [tutorial](http://michelleful.github.io/code-blog/2015/04/24/sgmap/) uses GeoPandas (and scikit-learn) to build a "linguistic street map" of Singapore.

**Visualization Resources:**
* Watch [Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk) (18 minutes) for an excellent example of why visualization is useful for understanding your data.
* For more on Pandas plotting, read this [notebook](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_7-Plotting-with-Pandas.ipynb) or the [visualization page](http://pandas.pydata.org/pandas-docs/stable/visualization.html) from the official Pandas documentation.
* To learn how to customize your plots further, browse through this [notebook on matplotlib](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_4-Matplotlib.ipynb) or this [similar notebook](https://github.com/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb).
* Read [Overview of Python Visualization Tools](http://pbpython.com/visualization-tools-1.html) for a useful comparison of Matplotlib, Pandas, Seaborn, ggplot, Bokeh, Pygal, and Plotly.
* To explore different types of visualizations and when to use them, [Choosing a Good Chart](http://extremepresentation.typepad.com/files/choosing-a-good-chart-09.pdf) and [The Graphic Continuum](http://www.coolinfographics.com/storage/post-images/The-Graphic-Continuum-POSTER.jpg) are nice one-page references, and the interactive [R Graph Catalog](http://shiny.stat.ubc.ca/r-graph-catalog/) has handy filtering capabilities.
* This [PowerPoint presentation](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic2-EDAViz.ppt) from Columbia's Data Mining class contains lots of good advice for properly using different types of visualizations.
* [Harvard's Data Science course](http://cs109.github.io/2014/) includes an excellent lecture on [Visualization Goals, Data Types, and Statistical Graphs](http://cm.dce.harvard.edu/2015/01/14328/L03/screen_H264LargeTalkingHead-16x9.shtml) (83 minutes), for which the [slides](https://docs.google.com/file/d/0B7IVstmtIvlHLTdTbXdEVENoRzQ/edit) are also available.

-----

<a name="command-line"></a>
### Class 4: Command Line and Version Control

**By the end of this lesson you will be able to:**
* clone a Githib repository to your laptop
* synch your local files with your GitHub repository using git add, commit, push and pull
* use more advanced command line commands such as Grep and |

**Topics/Highlights**
* Review the command line pre-class exercise ([code](code/04_command_line_basics.md))
* Git and GitHub ([slides](slides/04_git_github.pdf))
* Intermediate command line [(commands)](code/04_command_line_with_intermediate_advanced.md)

**Homework:**
* Complete the [command line homework assignment](homework/04_command_line_chipotle.md) with the Chipotle data.
* **Optional:** Browse through some more [example student projects](/project/project_examples/README.md), which may help to inspire your own project!

**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/book/en/v2) is an excellent book for learning Git. Read the first two chapters to gain a deeper understanding of version control and basic commands.
* If you want to practice a lot of Git (and learn many more commands), [Git Immersion](http://gitimmersion.com/) looks promising.
* If you want to understand how to contribute on GitHub, you first have to understand [forks and pull requests](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/).
* [GitRef](http://gitref.org/) is my favorite reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* [Cracking the Code to GitHub's Growth](https://growthhackers.com/growth-studies/github) explains why GitHub is so popular among developers.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a simpler and more attractive guide, but is less comprehensive.

**Command Line Resources:**
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://shop.oreilly.com/product/0636920032823.do) is a great book. The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" (a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.
* If you want to do more at the command line with CSV files, try out [csvkit](http://csvkit.readthedocs.org/), which can be installed via `pip`.

-----

<a name="fetching-data"></a>
### Class 5: Fetching Data

**After this lesson you will be able to:**
* Articulate what JSON, APIs and Web scraping are and how they help us fetch data
* Retrieve data from a website using the site’s APIs
* Scrape a web page to extract data

**Topics/Highlights:**
* Chipotle command line homework due [(code)](homework/04_command_line_chipotle.md)
* Fetching data through APIs
    * APIs - key concepts [(slides)](slides/05_APIs_and_web_scraping.pdf)
    * Example of API documentation: [The OMDb API - omdbapi.com](http://www.omdbapi.com/)
    * Code along - Access APIs on omdbapi.com [(code)](code/05_api.py)
    * Exercise - Retrieve US Census language stats though APIs [(code)](code/05_api_census.py)
     * [Census.gov language statistics page with API description](http://www.census.gov/data/developers/data-sets/language-stats.html)
* Grabbing data using Web scraping ([code](code/05_web_scraping.py))
    * [APIs - key concepts (slides)](slides/05_APIs_and_web_scraping.pdf)
    * [IMDb: robots.txt](http://www.imdb.com/robots.txt)
    * [Example web page](data/example.html)
    * [IMDb: The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)


**Homework:**
* If you're using Anaconda, install Seaborn by running `conda install seaborn` at the command line. (Note that some students in past courses have had problems with Anaconda after installing Seaborn.) If you're not using Anaconda, [install Seaborn](http://stanford.edu/~mwaskom/software/seaborn/installing.html) using `pip`. 
* **Optional:** Complete the homework exercise listed in the [web scraping code](code/05_web_scraping.py). It will take the place of any one homework you miss, past or future! This is due on Tuesday (April 5th).

**API Resources:**
* This Python script to [query the U.S. Census API](https://github.com/laurakurup/census-api) was created by a former DAT student. It's a bit more complicated than the example we used in class, it's very well commented, and it may provide a useful framework for writing your own code to query APIs.
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.
* The [Data Science Toolkit](http://www.datasciencetoolkit.org/) is a collection of location-based and text-related APIs.
* [API Integration in Python](https://realpython.com/blog/python/api-integration-in-python/) provides a very readable introduction to REST APIs.
* Microsoft's [Face Detection API](https://www.projectoxford.ai/demo/face#detection), which powers [How-Old.net](http://how-old.net/), is a great example of how a machine learning API can be leveraged to produce a compelling web application.

**Web Scraping Resources:**
* The [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is incredibly thorough, but is hard to use as a reference guide. However, the section on [specifying a parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) may be helpful if Beautiful Soup appears to be parsing a page incorrectly.
* For more Beautiful Soup examples and tutorials, see [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/), a former DAT student's well-commented notebook on [scraping Craigslist](https://github.com/Alexjmsherman/DataScience_GeneralAssembly/blob/master/Final_Project/1.%20Final_Project_Data%20Scraping.ipynb), this [notebook](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) from Stanford's Text As Data course, and this [notebook](https://github.com/cs109/2014/blob/master/lectures/2014_09_23-lecture/data_scraping_transcript.ipynb) and associated [video](http://cm.dce.harvard.edu/2015/01/14328/L07/screen_H264LargeTalkingHead-16x9.shtml) from Harvard's Data Science course.
* For a much longer web scraping tutorial covering Beautiful Soup, lxml, XPath, and Selenium, watch [Web Scraping with Python](https://www.youtube.com/watch?v=p1iX0uxM1w8) (3 hours 23 minutes) from PyCon 2014. The [slides](https://docs.google.com/presentation/d/1uHM_esB13VuSf7O1ScGueisnrtu-6usGFD3fs4z5YCE/edit#slide=id.p) and [code](https://github.com/kjam/python-web-scraping-tutorial) are also available.
* For more complex web scraping projects, [Scrapy](http://scrapy.org/) is a popular application framework that works with Python. It has excellent [documentation](http://doc.scrapy.org/en/1.0/index.html), and here's a [tutorial](https://github.com/rdempsey/ddl-data-wrangling) with detailed slides and code.
* [robotstxt.org](http://www.robotstxt.org/robotstxt.html) has a concise explanation of how to write (and read) the `robots.txt` file.
* [import.io](https://import.io/) and [Kimono](https://www.kimonolabs.com/) claim to allow you to scrape websites without writing any code.
* [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) and [How Netflix Reverse Engineered Hollywood](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) are two fun examples of how web scraping has been used to build interesting datasets.

-----

<a name="intro-to-regression"></a>
### Class 6: Intro to regression

**After this lesson you will be able to:**
* Indentify the kinds of problems that Linear Regression can solve
* Create a linear regression predictive model
* Evaluate the error of the model's fit to the training data

**Topics/Highlights:**
* Linear regression ([notebook](notebooks/06_linear_regression.ipynb))
    * [Capital Bikeshare dataset](data/bikeshare.csv) used in a Kaggle competition
    * [Data dictionary](https://www.kaggle.com/c/bike-sharing-demand/data)
* Why we should examine data well before building a model: Anscombes_Quartet [(notebook)](notebooks/06_Anscombes_Quartet.ipynb)

<!--* An additional feature engineering example is available here: [Predicting User Engagement in Corporate Collaboration Network](https://github.com/mikeyea/DAT7_project/blob/master/final%20project/Class_Presention_MYea.ipynb) -->

**Homework:**
* Complete the [homework assignment](homework/06_yelp_votes_homework.ipynb) with the [Yelp data](data/yelp.csv). This is due on Thursday (4/7).

**Linear Regression Resources:**
* To go much more in-depth on linear regression, read Chapter 3 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). Alternatively, watch the [related videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) or read Kevin Markhams [quick reference guide](http://www.dataschool.io/applying-and-interpreting-linear-regression/) to the key points in that chapter.
* This [introduction to linear regression](http://people.duke.edu/~rnau/regintro.htm) is more detailed and mathematically thorough, and includes lots of good advice.
* This is a relatively quick post on the [assumptions of linear regression](http://pareonline.net/getvn.asp?n=2&v=8).
* Setosa has an [interactive visualization](http://setosa.io/ev/ordinary-least-squares-regression/) of linear regression.

<!--* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md) -->

-----

<a name="knn"></a>
### Class 7: K-Nearest Neighbors

**After this lesson you will be able to:**
* Indentify the steps to build a predictive model in scikit-learn
* Create a k nearest neighbors (knn) predictive model
* Describe the difference between a supervised and unsupervised model

**Topics/Highlights:**
* K-nearest neighbors (KNN) and scikit-learn ([notebook](notebooks/07_knn_sklearn.ipynb))
* Exercise with NBA player data ([notebook](notebooks/07_nba_knn.ipynb), [data](/data/NBA_players_2015.csv), [data dictionary](/slides/07_nba_paper.pdf))
* Machine learning types and terms [(slides)](slides/07_machine_learning.pdf) 

**Homework:**
* The [homework assignment](homework/06_yelp_votes_homework.ipynb) with the [Yelp data](data/yelp.csv) is due on Thursday (4/7).
* Reading assignment on the [bias-variance tradeoff](homework/09_bias_variance.md)
* Read Kevin Markhams's [introduction to reproducibility](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), read Jeff Leek's [guide to creating a reproducible analysis](https://github.com/jtleek/datasharing), and watch this related [Colbert Report video](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error) (8 minutes).
* Optional: Quick Pandas exercise ([notebook](notebooks/08_pandas_review.ipynb)).  Complete this exercise to sharpen your understanding of dataframes.
* Work on your project... your first project presentation is in less than three weeks!

**KNN Resources:**
* [(notebook)](notebooks/07_human_learning_iris.ipynb) An example of the steps one would go through using "human learning" to come up with a rule to classify new iris observations based on the Iris data set.  Contains a refresher on many Pandas techniques such as groupby and visulaization.
* For a recap of the key points about KNN and scikit-learn, watch [Getting started in scikit-learn with the famous iris dataset](https://www.youtube.com/watch?v=hd1W4CyPX58) (15 minutes) and [Training a machine learning model with scikit-learn](https://www.youtube.com/watch?v=RlQuVL6-qe8) (20 minutes).
* KNN supports [distance metrics](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html) other than Euclidean distance, such as [Mahalanobis distance](http://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance), which [takes the scale of the data into account](http://blogs.sas.com/content/iml/2012/02/15/what-is-mahalanobis-distance.html).
* [A Detailed Introduction to KNN](https://saravananthirumuruganathan.wordpress.com/2010/05/17/a-detailed-introduction-to-k-nearest-neighbor-knn-algorithm/) is a bit dense, but provides a more thorough introduction to KNN and its applications.
* This lecture on [Image Classification](http://cs231n.github.io/classification/) shows how KNN could be used for detecting similar images, and also touches on topics we will cover in future classes (hyperparameter tuning and cross-validation).
* Some applications for which KNN is well-suited are [object recognition](http://vlm1.uta.edu/~athitsos/nearest_neighbors/), [satellite image enhancement](http://land.umn.edu/documents/FS6.pdf), [document categorization](http://www.ceng.metu.edu.tr/~e120321/paper.pdf), and [gene expression analysis](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.208.993).

**Seaborn Resources:**
* The official Seaborn website has a series of [detailed tutorials](http://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html) and an [example gallery](http://web.stanford.edu/~mwaskom/software/seaborn/examples/index.html).
* [Data visualization with Seaborn](https://beta.oreilly.com/learning/data-visualization-with-seaborn) is a quick tour of some of the popular types of Seaborn plots.
* [Visualizing Google Forms Data with Seaborn](http://pbpython.com/pandas-google-forms-part2.html) and [How to Create NBA Shot Charts in Python](http://savvastjortjoglou.com/nba-shot-sharts.html) are both good examples of Seaborn usage on real-world data.

-----

<a name="evaluating-fit"></a>
### Class 8: Basic Model Evaluation
* Reproducibility
    * Discuss assigned readings: [introduction](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), [Colbert Report video](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error), [cabs article](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2), [Tweet](https://twitter.com/jakevdp/status/519563939177197571), [creating a reproducible analysis](https://github.com/jtleek/datasharing)
    * Examples: [Classic rock](https://github.com/fivethirtyeight/data/tree/master/classic-rock), [student project 1](https://github.com/jwknobloch/DAT4_final_project), [student project 2](https://github.com/justmarkham/DAT4-students/tree/master/Jonathan_Bryan/Project_Files)
* Discuss the reading assignment on the [bias-variance tradeoff](homework/09_bias_variance.md)
* Exploring the bias-variance tradeoff ([notebook](notebooks/08_bias_variance.ipynb)) 
* Model evaluation using train/test split ([notebook](notebooks/08_model_evaluation.ipynb))
* Exploring the scikit-learn documentation: [module reference](http://scikit-learn.org/stable/modules/classes.html), [user guide](http://scikit-learn.org/stable/user_guide.html), class and function documentation

<!--
**Homework:**
* Watch [Data science in Python](https://www.youtube.com/watch?v=3ZWuPVWq7p4) (35 minutes) for an introduction to linear regression (and a review of other course content), or at the very least, read through the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/06_linear_regression.ipynb).
* **Optional:** For another introduction to linear regression, watch [The Easiest Introduction to Regression Analysis](https://www.youtube.com/watch?v=k_OB1tWX9PM) (14 minutes).
-->

**Model Evaluation Resources:**
* For a recap of some of the key points from today's lesson, watch [Comparing machine learning models in scikit-learn](https://www.youtube.com/watch?v=0pP4EwWJgIU) (27 minutes).
* For another explanation of training error versus testing error, the bias-variance tradeoff, and train/test split (also known as the "validation set approach"), watch Hastie and Tibshirani's video on [estimating prediction error](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34).
* Caltech's Learning From Data course includes a fantastic video on [visualizing bias and variance](http://work.caltech.edu/library/081.html) (15 minutes).
* [Random Test/Train Split is Not Always Enough](http://www.win-vector.com/blog/2015/01/random-testtrain-split-is-not-always-enough/) explains why random train/test split may not be a suitable model evaluation procedure if your data has a significant time element.

**Reproducibility Resources:**
* [What We've Learned About Sharing Our Data Analysis](https://source.opennews.org/en-US/articles/what-weve-learned-about-sharing-our-data-analysis/) includes tips from BuzzFeed News about how to publish a reproducible analysis.
* [Software development skills for data scientists](http://treycausey.com/software_dev_skills.html) discusses the importance of writing functions and proper code comments (among other skills), which are highly useful for creating a reproducible analysis.
* [Data science done well looks easy - and that is a big problem for data scientists](http://simplystatistics.org/2015/03/17/data-science-done-well-looks-easy-and-that-is-a-big-problem-for-data-scientists/) explains how a reproducible analysis demonstrates all of the work that goes into proper data science.

-----

<a name="logistic-regression"></a>
### Class 9: Logistic Regression
* Yelp votes homework due ([notebook](homework/10_yelp_votes_homework.ipynb))
* Logistic regression ([notebook](notebooks/12_logistic_regression.ipynb))
    * [Glass identification dataset](https://archive.ics.uci.edu/ml/datasets/Glass+Identification)
* Exercise with Titanic data ([notebook](notebooks/12_titanic_confusion.ipynb), [data](data/titanic.csv), [data dictionary](https://www.kaggle.com/c/titanic/data))
* Confusion matrix ([slides](slides/12_confusion_matrix.pdf), [notebook](notebooks/12_titanic_confusion.ipynb))

**Homework:**
* If you aren't yet comfortable with all of the confusion matrix terminology, watch Rahul Patwari's videos on [Intuitive sensitivity and specificity](https://www.youtube.com/watch?v=U4_3fditnWg) (9 minutes) and [The tradeoff between sensitivity and specificity](https://www.youtube.com/watch?v=vtYDyGGeQyo) (13 minutes).
* Video/reading assignment on [ROC curves and AUC](homework/13_roc_auc.md)
* Video/reading assignment on [cross-validation](homework/13_cross_validation.md)

**Logistic Regression Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), or watch the [first three videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) (30 minutes) from that chapter.
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of four classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes) and one classifier we do not cover (Support Vector Machines).

**Confusion Matrix Resources:**
* Kevin Markham's [simple guide to confusion matrix terminology](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) may be useful to you as a reference.
* This blog post about [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/amazon-machine-learning-make-data-driven-decisions-at-scale/) contains a neat [graphic](https://media.amazonwebservices.com/blog/2015/ml_adjust_model_1.png) showing how classification threshold affects different evaluation metrics.
* This notebook (from another DAT course) explains [how to calculate "expected value"](https://github.com/podopie/DAT18NYC/blob/master/classes/13-expected_value_cost_benefit_analysis.ipynb) from a confusion matrix by treating it as a cost-benefit matrix.

-----

<a name="advanced-model></a>
### Class 10: Advanced Model Evaluation
* Data preparation ([notebook](notebooks/13_advanced_model_evaluation.ipynb))
    * Handling missing values
    * Handling categorical features (review)
* ROC curves and AUC
    * Discuss the [video/reading assignment](homework/13_roc_auc.md)
    * Exercise: drawing an ROC curve ([slides](slides/13_drawing_roc.pdf))
    * Return to the main notebook
* Cross-validation
    * Discuss the [video/reading assignment](homework/13_cross_validation.md) and associated [notebook](notebooks/13_cross_validation.ipynb)
    * Return to the main notebook
* Exercise with bank marketing data ([notebook](notebooks/13_bank_exercise.ipynb), [data](data/bank-additional.csv), [data dictionary](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing))

**Homework:**
* Reading assignment on [spam filtering](homework/14_spam_filtering.md)
* Read these [Introduction to Probability](https://docs.google.com/presentation/d/1cM2dVbJgTWMkHoVNmYlB9df6P2H8BrjaqAcZTaLe9dA/edit#slide=id.gfc3caad2_00) slides, or skim section 2.1 of the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php?stat_book=os) (12 pages). Pay specific attention to the following terms: probability, mutually exclusive, sample space, independent.
* **Optional:** Try to gain an understanding of conditional probability from this [visualization](http://setosa.io/conditional/).
* **Optional:** For an intuitive introduction to Bayes' theorem, read these posts on [wealth and happiness](http://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule/answer/Michael-Hochster), [ducks](https://planspacedotorg.wordpress.com/2014/02/23/bayes-rule-for-ducks/), or [legos](http://www.countbayesie.com/blog/2015/2/18/bayes-theorem-with-lego).

**ROC Resources:**
* Rahul Patwari has a great video on [ROC Curves](https://www.youtube.com/watch?v=21Igj5Pr6u4) (12 minutes).
* [An introduction to ROC analysis](http://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) is a very readable paper on the topic.
* ROC curves can be used across a wide variety of applications, such as [comparing different feature sets](http://research.microsoft.com/pubs/205472/aisec10-leontjeva.pdf) for detecting fraudulent Skype users, and [comparing different classifiers](http://www.cse.ust.hk/nevinZhangGroup/readings/yi/Bradley_PR97.pdf) on a number of popular datasets.

**Cross-Validation Resources:**
* For more on cross-validation, read section 5.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (11 pages) or watch the related videos: [K-fold and leave-one-out cross-validation](https://www.youtube.com/watch?v=nZAM5OXrktY) (14 minutes), [cross-validation the right and wrong ways](https://www.youtube.com/watch?v=S06JpVoNaA0) (10 minutes).
* If you want to understand the different variations of cross-validation, this [paper](http://www.jcheminf.com/content/pdf/1758-2946-6-10.pdf) examines and compares them in detail.
* To learn how to use [GridSearchCV and RandomizedSearchCV](http://scikit-learn.org/stable/modules/grid_search.html) for parameter tuning, watch [How to find the best model parameters in scikit-learn](https://www.youtube.com/watch?v=Gol_qOgRqfA) (28 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb).

**Other Resources:**
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html).
* [Counterfactual evaluation of machine learning models](https://www.youtube.com/watch?v=QWCSxAKR-h0) (45 minutes) is an excellent talk about the sophisticated way in which Stripe evaluates its fraud detection model. (These are the associated [slides](http://www.slideshare.net/MichaelManapat/counterfactual-evaluation-of-machine-learning-models).)
* [Visualizing Machine Learning Thresholds to Make Better Business Decisions](http://blog.insightdatalabs.com/visualizing-classifier-thresholds/) demonstrates how visualizing precision, recall, and "queue rate" at different thresholds can help you to maximize the business value of your classifier.

-----

### Class 11: Regularization and Clustering
**By the end of this lesson you will be able to:**

* Standardize features
* Cluster using K-means and DBSCAN
* Compare "how good" the clustering models are

**Topics/Highlights**

* Advanced scikit-learn ([notebook](notebooks/19_advanced_sklearn.ipynb))
    * [StandardScaler](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html): standardizing features
    * [Pipeline](http://scikit-learn.org/stable/modules/pipeline.html): chaining steps
* Clustering ([slides](slides/19_clustering.pdf), [notebook](notebooks/19_clustering.ipynb))
    * K-means: [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html), [visualization 1](http://tech.nitoyon.com/en/blog/2013/11/07/k-means/), [visualization 2](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
    	* [My clustering of colors in an image.  Used a loop to generate clusters of 1 to 256 clusters. Made into an animated gif out of them.  Fun!](https://github.com/JamesByers/Cluster-analysis-of-image-RGB-colors/blob/master/Output%20Newport_seafood%20image%20and%20Animated%20GIF/Newport_seafood_k_means%2B%2B_cluster_animated.gif)
    * DBSCAN: [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html), [visualization](http://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)

**Homework:**
* Reread [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html). (The "answers" to the [guiding questions](homework/solutions/09_bias_variance.md) have been posted and may be helpful to you.)
* **Optional:** Watch these two excellent (and related) videos from Caltech's Learning From Data course: [bias-variance tradeoff](http://work.caltech.edu/library/081.html) (15 minutes) and [regularization](http://work.caltech.edu/library/121.html) (8 minutes).

**scikit-learn Resources:**
* This is a longer example of [feature scaling](https://github.com/rasbt/pattern_classification/blob/master/preprocessing/about_standardization_normalization.ipynb) in scikit-learn, with additional discussion of the types of scaling you can use.
* [Practical Data Science in Python](http://radimrehurek.com/data_science_python/) is a long and well-written notebook that uses a few advanced scikit-learn features: pipelining, plotting a learning curve, and pickling a model.
* To learn how to use [GridSearchCV and RandomizedSearchCV](http://scikit-learn.org/stable/modules/grid_search.html) for parameter tuning, watch [How to find the best model parameters in scikit-learn](https://www.youtube.com/watch?v=Gol_qOgRqfA) (28 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb).
* Sebastian Raschka has a number of excellent resources for scikit-learn users, including a repository of [tutorials and examples](https://github.com/rasbt/pattern_classification), a library of machine learning [tools and extensions](http://rasbt.github.io/mlxtend/), a new [book](https://github.com/rasbt/python-machine-learning-book), and a semi-active [blog](http://sebastianraschka.com/blog/).
* scikit-learn has an incredibly active [mailing list](https://www.mail-archive.com/scikit-learn-general@lists.sourceforge.net/index.html) that is often much more useful than Stack Overflow for researching functions and asking questions.
* If you forget how to use a particular scikit-learn function that we have used in class, don't forget that this repository is fully searchable!

**Clustering Resources:**
* For a very thorough introduction to clustering, read chapter 8 (69 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php) (available as a free download), or browse through the chapter 8 slides.
* scikit-learn's user guide compares many different [types of clustering](http://scikit-learn.org/stable/modules/clustering.html).
* This [PowerPoint presentation](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic6-Clustering.ppt) from Columbia's Data Mining class provides a good introduction to clustering, including hierarchical clustering and alternative distance metrics.
* An Introduction to Statistical Learning has useful videos on [K-means clustering](https://www.youtube.com/watch?v=aIybuNt9ps4&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (17 minutes) and [hierarchical clustering](https://www.youtube.com/watch?v=Tuuc9Y06tAc&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (15 minutes).
* This is an excellent interactive visualization of [hierarchical clustering](https://joyofdata.shinyapps.io/hclust-shiny/).
* This is a nice animated explanation of [mean shift clustering](http://spin.atomicobject.com/2015/05/26/mean-shift-clustering/).
* The [K-modes algorithm](http://www.cs.ust.hk/~qyang/Teaching/537/Papers/huang98extensions.pdf) can be used for clustering datasets of categorical features without converting them to numerical values. Here is a [Python implementation](https://github.com/nicodv/kmodes).
* Here are some fun examples of clustering: [A Statistical Analysis of the Work of Bob Ross](http://fivethirtyeight.com/features/a-statistical-analysis-of-the-work-of-bob-ross/) (with [data and Python code](https://github.com/fivethirtyeight/data/tree/master/bob-ross)), [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/), and [characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/).

-----

<a name="nlp"></a>
### Class 13: Natural Language Processing
* Natural language processing ([notebook](notebooks/13_natural_language_processing.ipynb))
 * Vectorization/Tokenization
 * Stopword Removal
 * Other CountVectorizer options
 * Intro to [TextBlob](https://textblob.readthedocs.org/en/dev/)
  * Stemming and Lemmatization
  * Term Frequency-Inverse Document Frequency (TF-IDF)
  *  Using TF-IDF to Summarize a Yelp Review
  *  Sentiment Analysis

**Homework:**
* **Your draft paper is due on Thursday (12/22)!** Please submit a link to your project repository (with paper, code, data, and visualizations) before class
* The [homework assignment](homework/14_yelp_review_text_homework.ipynb) with the [Yelp data](data/yelp.csv) is due on Tuesday (12/22)

**NLP Resources:**
* If you want to learn a lot more NLP, check out the excellent [video lectures](https://class.coursera.org/nlp/lecture) and [slides](http://web.stanford.edu/~jurafsky/NLPCourseraSlides.html) from this [Coursera course](https://www.coursera.org/course/nlp) (which is no longer being offered).
* This slide deck defines many of the [key NLP terms](https://github.com/ga-students/DAT_SF_9/blob/master/16_Text_Mining/DAT9_lec16_Text_Mining.pdf).
* [Natural Language Processing with Python](http://www.nltk.org/book/) is the most popular book for going in-depth with the [Natural Language Toolkit](http://www.nltk.org/) (NLTK).
* [A Smattering of NLP in Python](https://github.com/charlieg/A-Smattering-of-NLP-in-Python/blob/master/A%20Smattering%20of%20NLP%20in%20Python.ipynb) provides a nice overview of NLTK
* [spaCy](http://spacy.io/) is a newer Python library for text processing that is focused on performance (unlike NLTK).
* If you want to get serious about NLP, [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml) is a suite of tools (written in Java) that is highly regarded.
* When working with a large text corpus in scikit-learn, [HashingVectorizer](http://scikit-learn.org/stable/modules/feature_extraction.html#vectorizing-a-large-text-corpus-with-the-hashing-trick) is a useful alternative to CountVectorizer.
* [Automatically Categorizing Yelp Businesses](http://engineeringblog.yelp.com/2015/09/automatically-categorizing-yelp-businesses.html) discusses how Yelp uses NLP and scikit-learn to solve the problem of uncategorized businesses.
* [Modern Methods for Sentiment Analysis](http://districtdatalabs.silvrback.com/modern-methods-for-sentiment-analysis) shows how "word vectors" can be used for more accurate sentiment analysis.
* [Identifying Humorous Cartoon Captions](http://www.cs.huji.ac.il/~dshahaf/pHumor.pdf) is a readable paper about identifying funny captions submitted to the New Yorker Caption Contest.

-----

<a name="decision></a>
### Class 15: Decision Trees
**By the end of this lesson you will be able to:**

* Create a Regression tree
* Graph and interpret the decision tree

**Topics/Highlights**

* Decision trees ([notebook](notebooks/15_decision_trees.ipynb))
* 	Part 1: Regression trees
* Exercise with Capital Bikeshare data ([notebook](notebooks/5_bikeshare_exercise.ipynb), [data](data/bikeshare.csv), [data dictionary](https://www.kaggle.com/c/bike-sharing-demand/data))

**Homework:**
* Read the "Wisdom of the crowds" section from MLWave's post on [Human Ensemble Learning](http://mlwave.com/human-ensemble-learning/).
* **Optional:** Read the abstract from [Do We Need Hundreds of Classifiers to Solve Real World Classification Problems?](http://jmlr.csail.mit.edu/papers/volume15/delgado14a/delgado14a.pdf), as well as Kaggle CTO Ben Hamner's [comment](https://news.ycombinator.com/item?id=8719723) about the paper, paying attention to the mentions of "Random Forests".

**Resources:**
* scikit-learn's documentation on [decision trees](http://scikit-learn.org/stable/modules/tree.html) includes a nice overview of trees as well as tips for proper usage.
* For a more thorough introduction to decision trees, read section 4.3 (23 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php). (Chapter 4 is available as a free download.)
* If you want to go deep into the different decision tree algorithms, this slide deck contains [A Brief History of Classification and Regression Trees](https://drive.google.com/file/d/0B-BKohKl-jUYQ3RpMEF0OGRUU3RHVGpHY203NFd3Z19Nc1ZF/view).
* [The Science of Singing Along](http://www.doc.gold.ac.uk/~mas03dm/papers/PawleyMullensiefen_Singalong_2012.pdf) contains a neat regression tree (page 136) for predicting the percentage of an audience at a music venue that will sing along to a pop song.
* Decision trees are common in the medical field for differential diagnosis, such as this classification tree for [identifying psychosis](http://www.psychcongress.com/sites/naccme.com/files/images/pcn/saundras/psychosis_decision_tree.pdf).

-----

<a name="ensemble></a>
### Class 16: Ensembling, Bagging and Random Forests

* Finish decision trees lesson ([notebook](notebooks/15_decision_trees.ipynb))
* Ensembling, Bagging and Random Forests ([notebook](notebooks/16_ensembling.ipynb))
    * [Major League Baseball player data](data/hitters.csv) from 1986-87
    * [Data dictionary](https://cran.r-project.org/web/packages/ISLR/ISLR.pdf) (see page 7)

**Resources:**
* scikit-learn's documentation on [ensemble methods](http://scikit-learn.org/stable/modules/ensemble.html) covers both "averaging methods" (such as bagging and Random Forests) as well as "boosting methods" (such as AdaBoost and Gradient Tree Boosting).
* MLWave's [Kaggle Ensembling Guide](http://mlwave.com/kaggle-ensembling-guide/) is very thorough and shows the many different ways that ensembling can take place.
* Browse the excellent [solution paper](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/ChenglongChen/Kaggle_CrowdFlower/master/Doc/Kaggle_CrowdFlower_ChenglongChen.pdf) from the winner of Kaggle's [CrowdFlower competition](https://www.kaggle.com/c/crowdflower-search-relevance) for an example of the work and insight required to win a Kaggle competition.
* [Interpretable vs Powerful Predictive Models: Why We Need Them Both](https://medium.com/@chris_bour/interpretable-vs-powerful-predictive-models-why-we-need-them-both-990340074979) is a short post on how the tactics useful in a Kaggle competition are not always useful in the real world.
* [Not Even the People Who Write Algorithms Really Know How They Work](http://www.theatlantic.com/technology/archive/2015/09/not-even-the-people-who-write-algorithms-really-know-how-they-work/406099/) argues that the decreased interpretability of state-of-the-art machine learning models has a negative impact on society.
* For an intuitive explanation of Random Forests, read Edwin Chen's answer to [How do random forests work in layman's terms?](http://www.quora.com/Random-Forests/How-do-random-forests-work-in-laymans-terms/answer/Edwin-Chen-1)
* [Large Scale Decision Forests: Lessons Learned](http://blog.siftscience.com/blog/2015/large-scale-decision-forests-lessons-learned) is an excellent post from Sift Science about their custom implementation of Random Forests.
* [Unboxing the Random Forest Classifier](http://nerds.airbnb.com/unboxing-the-random-forest-classifier/) describes a way to interpret the inner workings of Random Forests beyond just feature importances.
* [Understanding Random Forests: From Theory to Practice](http://arxiv.org/pdf/1407.7502v3.pdf) is an in-depth academic analysis of Random Forests, including details of its implementation in scikit-learn.

-----











<!--* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md)
### Class 1  older: Introduction to Data Science

**By the end of this lesson you will be able to:**
* Describe what data science is and the types of problems it can solve
* Name at least three types of data
* Describe at least two of the elements of the Final project requirements

**Topics/Highlights**
* Welcome from General Assembly staff
* Course overview ([slides](slides/01_course_overview.pdf))
* Data Science Intro ([slides](slides/01_data_science_intro.pdf))
* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md)

**Homework:**
* Complete GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows).
* Read through this [command line reference](code/02_command_line_basics.md), and complete the pre-class exercise at the bottom. (There's nothing you need to submit once you're done.)
* Watch videos 1 through 8 (21 minutes) of [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD), or read sections 1.1 through 2.2 of [Pro Git](http://git-scm.com/book/en/v2).
* If your laptop has any setup issues, please work with us to resolve them by Thursday. If your laptop has not yet been checked, you should come early on Thursday, or just walk through the [setup checklist](other/setup_checklist.md) yourself (and let us know you have done so).

**Resources:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* Quora has a [data science topic FAQ](https://www.quora.com/Data-Science) with lots of interesting Q&A.

<!--
-----

### Class 2: Command Line and Version Control

**By the end of this lesson you will be able to:**
* clone a Githib repository to your laptop
* synch your local files with your GitHub repository using git add, commit, push and pull
* use more advanced command line commands such as Grep and |

**Topics/Highlights**
* Slack tour
* Review the command line pre-class exercise ([code](code/02_command_line_basics.md))
* Git and GitHub ([slides](slides/02_git_github.pdf))
* Intermediate command line

**Homework:**
* Complete the [command line homework assignment](homework/02_command_line_chipotle.md) with the Chipotle data.
* Review the code from a [beginner](code/00_python_beginner_workshop.py) and an [intermediate](code/00_python_intermediate_workshop.py) Python workshop. If you don't feel comfortable with any of the content (excluding the "requests" and "APIs" sections), you should spend some time this weekend practicing Python:
    * [Introduction to Python](http://introtopython.org/) does a great job explaining Python essentials and includes tons of example code.
    * If you like learning from a book, [Python for Informatics](http://www.pythonlearn.com/html-270/) has useful chapters on strings, lists, and dictionaries.
    * If you prefer interactive exercises, try these lessons from [Codecademy](http://www.codecademy.com/en/tracks/python): "Python Lists and Dictionaries" and "A Day at the Supermarket".
    * If you have more time, try missions 2 and 3 from [DataQuest's Learning Python](https://www.dataquest.io/course/learning-python) course.
    * If you've already mastered these topics and want more of a challenge, try solving [Python Challenge](http://www.pythonchallenge.com/) number 1 (decoding a message) and send me your code in Slack.
* To give you a framework for thinking about your project, watch [What is machine learning, and how does it work?](https://www.youtube.com/watch?v=elojMnjn4kk) (10 minutes). (This is the [IPython notebook](other/scikit-learn_videos/01_machine_learning_intro.ipynb) shown in the video.) Alternatively, read [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/), which focuses on a specific machine learning model called decision trees.
* **Optional:** Browse through some more [example student projects](/project/project_examples/README.md), which may help to inspire your own project!

**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/book/en/v2) is an excellent book for learning Git. Read the first two chapters to gain a deeper understanding of version control and basic commands.
* If you want to practice a lot of Git (and learn many more commands), [Git Immersion](http://gitimmersion.com/) looks promising.
* If you want to understand how to contribute on GitHub, you first have to understand [forks and pull requests](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/).
* [GitRef](http://gitref.org/) is my favorite reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* [Cracking the Code to GitHub's Growth](https://growthhackers.com/growth-studies/github) explains why GitHub is so popular among developers.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a simpler and more attractive guide, but is less comprehensive.

**Command Line Resources:**
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://shop.oreilly.com/product/0636920032823.do) is a great book. The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" (a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.
* If you want to do more at the command line with CSV files, try out [csvkit](http://csvkit.readthedocs.org/), which can be installed via `pip`.

-----

### Class 3: Reading and Preparing Data

**By the end of this lesson you will be able to:**
 * State use case where you would chose a python dictionary over a list and one case where you would choose a list over a dictionary
 * Use Python to read text file data into a program
 * Use Python to convert the data into a nested list (list of lists)

**Topics/Highlights**
* Review command line homework ([solution](homework/02_command_line_chipotle.md))
* Git and GitHub assorted tips ([slides](slides/02_git_github.pdf))
* Python:
    * Spyder interface
    * Looping exercise
    * File reading with airline safety data, code-along  ([article](http://fivethirtyeight.com/features/should-travelers-avoid-flying-airlines-that-have-had-crashes-in-the-past/), [data](data/airlines.csv), [code](code/03_file_reading.py))
    * Data preparation exercise
    * Walkthrough of Python Chipotle homework assignment ([article](http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html), [data](data/chipotle.tsv), [code](homework/03_python_homework_chipotle.py))

**Homework:**
* Complete the [Python homework assignment](homework/03_python_homework_chipotle.py) with the Chipotle data, add a commented Python script to your GitHub repo, and submit a link using the homework submission form. *You have until Tuesday (11/10) to complete this assignment.* (**Note:** Pandas, which is covered in class 4, should not be used for this assignment.)

**Resources:**
* [Want to understand Python's comprehensions? Think in Excel or SQL](http://blog.lerner.co.il/want-to-understand-pythons-comprehensions-think-like-an-accountant/) may be helpful if you are still confused by list comprehensions.
* [My code isn't working](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/624506_orig.png) is a great flowchart explaining how to debug Python errors.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) is Python's "classic" style guide, and is worth a read if you want to write readable code that is consistent with the rest of the Python community.
* If you want to understand Python at a deeper level, Ned Batchelder's [Loop Like A Native](http://nedbatchelder.com/text/iter.html) and [Python Names and Values](http://nedbatchelder.com/text/names1.html) are excellent presentations.

-----

### Class 4: Exploratory Data Analysis
* Pandas ([code](code/04_pandas.py)):
    * MovieLens 100k movie ratings ([data](data/u.user), [data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt), [website](http://grouplens.org/datasets/movielens/))
    * Alcohol consumption by country ([data](data/drinks.csv), [article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/))
    * Reports of UFO sightings ([data](data/ufo.csv), [website](http://www.nuforc.org/webreports.html))




**Homework:**
* The deadline for discussing your project ideas with an instructor is Tuesday (11/10), and your project question write-up is due Thursday (11/12).
* [Python Chipolte homework assignment](homework/03_python_homework_chipotle.py) is due next Tues before class (11/10). ([article](http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html), [data](data/chipotle.tsv), [code](homework/03_python_homework_chipotle.py)).  Add a commented Python script to your GitHub repo, and submit a link using the homework submission form. (**Note:** Pandas, which is covered in class 4, should not be used for this assignment.)
* Read [How Software in Half of NYC Cabs Generates $5.2 Million a Year in Extra Tips](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2) for an excellent example of exploratory data analysis.
* Read [Anscombe's Quartet, and Why Summary Statistics Don't Tell the Whole Story](http://data.heapanalytics.com/anscombes-quartet-and-why-summary-statistics-dont-tell-the-whole-story/) for a classic example of why visualization is useful.

**Resources:**
* Browsing or searching the Pandas [API Reference](http://pandas.pydata.org/pandas-docs/stable/api.html) is an excellent way to locate a function even if you don't know its exact name.
* [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/) is a fun (yet enlightening) look at the process of exploratory data analysis.

-----

### Class 5: Visualization
* Python homework with the Chipotle data due
* Part 2 of Exploratory Data Analysis with Pandas
 * Merging dataframes [(code)](code/05_pandas_merge_nb.py)
  * Exercise: merging Seattle Pronto Cycle Share Data Challenge tables
* Visualization with Pandas and Matplotlib [(code)](code/05_pandas_visualization_nb.py)

**Homework:**
* Your project question write-up is due on Thursday.
* Complete the [Pandas homework assignment](/homework/05_pandas_homework_imbd.py) with the [IMDb data](data/imdb_1000.csv). You have until Tuesday (11/17) to complete this assignment.
* If you're not using Anaconda, install the [Jupyter Notebook](http://jupyter.readthedocs.org/en/latest/install.html) (formerly known as the IPython Notebook) using `pip`. (The Jupyter or IPython Notebook is included with Anaconda.)

**Pandas Resources:**
* To learn more Pandas, read this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/), or review these two excellent (but extremely long) notebooks on Pandas: [introduction](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb) and [data wrangling](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb).
* If you want to go really deep into Pandas (and NumPy), read the book [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do), written by the creator of Pandas.

<!-- * This notebook demonstrates the different types of [joins in Pandas](notebooks/05_pandas_merge.ipynb), for when you need to figure out how to merge two DataFrames. 
* This is a nice, short tutorial on [pivot tables](https://beta.oreilly.com/learning/pivot-tables) in Pandas.
* For working with geospatial data in Python, [GeoPandas](http://geopandas.org/index.html) looks promising. This [tutorial](http://michelleful.github.io/code-blog/2015/04/24/sgmap/) uses GeoPandas (and scikit-learn) to build a "linguistic street map" of Singapore.

**Visualization Resources:**
* Watch [Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk) (18 minutes) for an excellent example of why visualization is useful for understanding your data.
* For more on Pandas plotting, read this [notebook](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_7-Plotting-with-Pandas.ipynb) or the [visualization page](http://pandas.pydata.org/pandas-docs/stable/visualization.html) from the official Pandas documentation.
* To learn how to customize your plots further, browse through this [notebook on matplotlib](https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section2_4-Matplotlib.ipynb) or this [similar notebook](https://github.com/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb).
* Read [Overview of Python Visualization Tools](http://pbpython.com/visualization-tools-1.html) for a useful comparison of Matplotlib, Pandas, Seaborn, ggplot, Bokeh, Pygal, and Plotly.
* To explore different types of visualizations and when to use them, [Choosing a Good Chart](http://extremepresentation.typepad.com/files/choosing-a-good-chart-09.pdf) and [The Graphic Continuum](http://www.coolinfographics.com/storage/post-images/The-Graphic-Continuum-POSTER.jpg) are nice one-page references, and the interactive [R Graph Catalog](http://shiny.stat.ubc.ca/r-graph-catalog/) has handy filtering capabilities.
* This [PowerPoint presentation](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic2-EDAViz.ppt) from Columbia's Data Mining class contains lots of good advice for properly using different types of visualizations.
* [Harvard's Data Science course](http://cs109.github.io/2014/) includes an excellent lecture on [Visualization Goals, Data Types, and Statistical Graphs](http://cm.dce.harvard.edu/2015/01/14328/L03/screen_H264LargeTalkingHead-16x9.shtml) (83 minutes), for which the [slides](https://docs.google.com/file/d/0B7IVstmtIvlHLTdTbXdEVENoRzQ/edit) are also available.

-----

### Class 6: Machine Learning
**Topics/Highlights:**
* Part 2 of Visualization with Pandas and Matplotlib ([notebook](notebooks/05_pandas_visualization.ipynb))
* Brief introduction to the Jupyter/IPython Notebook
* "Human learning" exercise:
    * [ipython notebook](notebooks/06_human_learning_iris.ipynb)
    * [Iris dataset](http://archive.ics.uci.edu/ml/datasets/Iris) hosted by the UCI Machine Learning Repository
    * [Iris photo](http://sebastianraschka.com/Images/2014_python_lda/iris_petal_sepal.png)
* Introduction to machine learning

**Homework:**
* Complete the [Pandas homework assignment]. You have until Tuesday (11/17) to complete this assignment.
* **Optional:** Complete the bonus exercise listed in the [human learning notebook](notebooks/06_human_learning_iris.ipynb). It will take the place of any one homework you miss, past or future! This is due on Tues 11/17.
* If you're not using Anaconda, install [requests](http://www.python-requests.org/en/latest/user/install/) and [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) using `pip`. (Both of these packages are included with Anaconda.)

**Machine Learning Resources:**
* For a very quick summary of the key points about machine learning, watch [What is machine learning, and how does it work?](https://www.youtube.com/watch?v=elojMnjn4kk) (10 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/01_machine_learning_intro.ipynb).
* For a more in-depth introduction to machine learning, read section 2.1 (14 pages) of Hastie and Tibshirani's excellent book, [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). (It's a free PDF download!)
* The [Learning Paradigms](http://work.caltech.edu/library/014.html) video (13 minutes) from [Caltech's Learning From Data course](http://work.caltech.edu/telecourse.html) provides a nice comparison of supervised versus unsupervised learning, as well as an introduction to "reinforcement learning".
* [Real-World Active Learning](https://beta.oreilly.com/ideas/real-world-active-learning) is a readable and thorough introduction to "active learning", a variation of machine learning in which humans label only the most "important" observations.
* For a preview of some of the machine learning content we will cover during the course, read Sebastian Raschka's [overview of the supervised learning process](https://github.com/rasbt/pattern_classification/blob/master/machine_learning/supervised_intro/introduction_to_supervised_machine_learning.md).
* [Data Science, Machine Learning, and Statistics: What is in a Name?](http://www.win-vector.com/blog/2013/04/data-science-machine-learning-and-statistics-what-is-in-a-name/) discusses the differences between these (and other) terms.
* [The Emoji Translation Project](https://www.kickstarter.com/projects/fred/the-emoji-translation-project) is a really fun application of machine learning.
* Look up the [characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/), and then read about the [67 distinct segments](http://doc.arcgis.com/en/esri-demographics/data/tapestry-segmentation.htm) in detail.

**IPython Notebook Resources:**
* For a recap of the IPython Notebook introduction (and a preview of scikit-learn), watch [scikit-learn and the IPython Notebook](https://www.youtube.com/watch?v=IsXXlYVBt1M) (15 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/02_machine_learning_setup.ipynb).
* If you would like to learn the IPython Notebook, the official [Notebook tutorials](https://github.com/jupyter/notebook/blob/master/docs/source/examples/Notebook/Examples%20and%20Tutorials%20Index.ipynb) are useful.
* This [Reddit discussion](https://www.reddit.com/r/Python/comments/3be5z2/do_you_prefer_ipython_notebook_over_ipython/) compares the relative strengths of the IPython Notebook and Spyder.

-----

### Class 7: Fetching Data

**After this lesson you will be able to:**
* Articulate what JSON, APIs and Web scraping are and how they help us fetch data
* Retrieve data from a website using the site’s APIs
* Scrape a web page to extract data

**Topics/Highlights:**
* Pandas homework with the IMDb data due ([code](homework/05_pandas_homework_imbd.py))
* Optional "human learning" exercise with the iris data due ([code](notebooks/06_human_learning_iris.ipynb))
* Fetching data through APIs
    * [APIs - key concepts (slides)](/slides/07_APIs_and_web_scraping.pdf) and [The OMDb API - omdbapi.com](http://www.omdbapi.com/)
    * Code along - Access APIs on omdbapi.com [(code)](code/07_api.py)
     * Exercise - Retrieve US Census language stats though APIs
     * [Census.gov language statistics page with API description](http://www.census.gov/data/developers/data-sets/language-stats.html)
* Grabbing data using Web scraping ([code](code/07_web_scraping.py))
    * [APIs - key concepts (slides)](/slides/07_APIs_and_web_scraping.pdf)
    * [IMDb: robots.txt](http://www.imdb.com/robots.txt)
    * [Example web page](data/example.html)
    * [IMDb: The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)


**Homework:**
* **Optional:** Complete the homework exercise listed in the [web scraping code](code/07_web_scraping.py). It will take the place of any one homework you miss, past or future! This is due on Monday (11/23).
* **Optional:** If you're not using Anaconda, [install Seaborn](http://stanford.edu/~mwaskom/software/seaborn/installing.html) using `pip`. If you're using Anaconda, install Seaborn by running `conda install seaborn` at the command line. (Note that some students in past courses have had problems with Anaconda after installing Seaborn.)

**API Resources:**
* This Python script to [query the U.S. Census API](https://github.com/laurakurup/census-api) was created by a former DAT student. It's a bit more complicated than the example we used in class, it's very well commented, and it may provide a useful framework for writing your own code to query APIs.
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.
* The [Data Science Toolkit](http://www.datasciencetoolkit.org/) is a collection of location-based and text-related APIs.
* [API Integration in Python](https://realpython.com/blog/python/api-integration-in-python/) provides a very readable introduction to REST APIs.
* Microsoft's [Face Detection API](https://www.projectoxford.ai/demo/face#detection), which powers [How-Old.net](http://how-old.net/), is a great example of how a machine learning API can be leveraged to produce a compelling web application.

**Web Scraping Resources:**
* The [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is incredibly thorough, but is hard to use as a reference guide. However, the section on [specifying a parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) may be helpful if Beautiful Soup appears to be parsing a page incorrectly.
* For more Beautiful Soup examples and tutorials, see [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/), a former DAT student's well-commented notebook on [scraping Craigslist](https://github.com/Alexjmsherman/DataScience_GeneralAssembly/blob/master/Final_Project/1.%20Final_Project_Data%20Scraping.ipynb), this [notebook](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) from Stanford's Text As Data course, and this [notebook](https://github.com/cs109/2014/blob/master/lectures/2014_09_23-lecture/data_scraping_transcript.ipynb) and associated [video](http://cm.dce.harvard.edu/2015/01/14328/L07/screen_H264LargeTalkingHead-16x9.shtml) from Harvard's Data Science course.
* For a much longer web scraping tutorial covering Beautiful Soup, lxml, XPath, and Selenium, watch [Web Scraping with Python](https://www.youtube.com/watch?v=p1iX0uxM1w8) (3 hours 23 minutes) from PyCon 2014. The [slides](https://docs.google.com/presentation/d/1uHM_esB13VuSf7O1ScGueisnrtu-6usGFD3fs4z5YCE/edit#slide=id.p) and [code](https://github.com/kjam/python-web-scraping-tutorial) are also available.
* For more complex web scraping projects, [Scrapy](http://scrapy.org/) is a popular application framework that works with Python. It has excellent [documentation](http://doc.scrapy.org/en/1.0/index.html), and here's a [tutorial](https://github.com/rdempsey/ddl-data-wrangling) with detailed slides and code.
* [robotstxt.org](http://www.robotstxt.org/robotstxt.html) has a concise explanation of how to write (and read) the `robots.txt` file.
* [import.io](https://import.io/) and [Kimono](https://www.kimonolabs.com/) claim to allow you to scrape websites without writing any code.
* [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) and [How Netflix Reverse Engineered Hollywood](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) are two fun examples of how web scraping has been used to build interesting datasets.

-----

### Class 8: K-Nearest Neighbors
* Part 2 - Grabbing more data using Web scraping ([code](code/07_web_scraping.py))
    * [Web sraping - key concepts (slides)](/slides/07_APIs_and_web_scraping.pdf)
    * [IMDb: The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)
* K-nearest neighbors (KNN) and scikit-learn ([notebook](notebooks/08_knn_sklearn.ipynb))
* Exercise with NBA player data ([notebook](notebooks/08_nba_knn.ipynb), [data](/data/NBA_players_2015.csv), [data dictionary](/slides/07_nba_paper.pdf))


**Homework:**
* Quick Pandas exercise ([notebook](notebooks/08_pandas_review.ipynb)).  Complete this exercise to sharpen your understanding of dataframes.
* Reading assignment on the [bias-variance tradeoff](homework/09_bias_variance.md)
* Read Kevin's [introduction to reproducibility](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), read Jeff Leek's [guide to creating a reproducible analysis](https://github.com/jtleek/datasharing), and watch this related [Colbert Report video](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error) (8 minutes).
* Work on your project... your first project presentation is in less than two weeks!

**KNN Resources:**
* For a recap of the key points about KNN and scikit-learn, watch [Getting started in scikit-learn with the famous iris dataset](https://www.youtube.com/watch?v=hd1W4CyPX58) (15 minutes) and [Training a machine learning model with scikit-learn](https://www.youtube.com/watch?v=RlQuVL6-qe8) (20 minutes).
* KNN supports [distance metrics](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html) other than Euclidean distance, such as [Mahalanobis distance](http://stats.stackexchange.com/questions/62092/bottom-to-top-explanation-of-the-mahalanobis-distance), which [takes the scale of the data into account](http://blogs.sas.com/content/iml/2012/02/15/what-is-mahalanobis-distance.html).
* [A Detailed Introduction to KNN](https://saravananthirumuruganathan.wordpress.com/2010/05/17/a-detailed-introduction-to-k-nearest-neighbor-knn-algorithm/) is a bit dense, but provides a more thorough introduction to KNN and its applications.
* This lecture on [Image Classification](http://cs231n.github.io/classification/) shows how KNN could be used for detecting similar images, and also touches on topics we will cover in future classes (hyperparameter tuning and cross-validation).
* Some applications for which KNN is well-suited are [object recognition](http://vlm1.uta.edu/~athitsos/nearest_neighbors/), [satellite image enhancement](http://land.umn.edu/documents/FS6.pdf), [document categorization](http://www.ceng.metu.edu.tr/~e120321/paper.pdf), and [gene expression analysis](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.208.993).

**Seaborn Resources:**
* To get started with Seaborn for visualization, the official website has a series of [detailed tutorials](http://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html) and an [example gallery](http://web.stanford.edu/~mwaskom/software/seaborn/examples/index.html).
* [Data visualization with Seaborn](https://beta.oreilly.com/learning/data-visualization-with-seaborn) is a quick tour of some of the popular types of Seaborn plots.
* [Visualizing Google Forms Data with Seaborn](http://pbpython.com/pandas-google-forms-part2.html) and [How to Create NBA Shot Charts in Python](http://savvastjortjoglou.com/nba-shot-sharts.html) are both good examples of Seaborn usage on real-world data.

-----

### Class 9: Basic Model Evaluation
* Optional web scraping homework due ([solution](code/07_web_scraping.py#L136))
* Reproducibility
    * Discuss assigned readings: [introduction](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), [Colbert Report video](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error), [cabs article](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2), [Tweet](https://twitter.com/jakevdp/status/519563939177197571), [creating a reproducible analysis](https://github.com/jtleek/datasharing)
    * Examples: [Classic rock](https://github.com/fivethirtyeight/data/tree/master/classic-rock), [student project 1](https://github.com/jwknobloch/DAT4_final_project), [student project 2](https://github.com/justmarkham/DAT4-students/tree/master/Jonathan_Bryan/Project_Files)
* Discuss the reading assignment on the [bias-variance tradeoff](homework/09_bias_variance.md)
* * Exploring the bias-variance tradeoff ([notebook](notebooks/08_bias_variance.ipynb)) 
* Model evaluation using train/test split ([notebook](notebooks/09_model_evaluation.ipynb))
* Exploring the scikit-learn documentation: [module reference](http://scikit-learn.org/stable/modules/classes.html), [user guide](http://scikit-learn.org/stable/user_guide.html), class and function documentation

**Homework:**
* Watch [Data science in Python](https://www.youtube.com/watch?v=3ZWuPVWq7p4) (35 minutes) for an introduction to linear regression (and a review of other course content), or at the very least, read through the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/06_linear_regression.ipynb).
* **Optional:** For another introduction to linear regression, watch [The Easiest Introduction to Regression Analysis](https://www.youtube.com/watch?v=k_OB1tWX9PM) (14 minutes).

**Model Evaluation Resources:**
* For a recap of some of the key points from today's lesson, watch [Comparing machine learning models in scikit-learn](https://www.youtube.com/watch?v=0pP4EwWJgIU) (27 minutes).
* For another explanation of training error versus testing error, the bias-variance tradeoff, and train/test split (also known as the "validation set approach"), watch Hastie and Tibshirani's video on [estimating prediction error](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34).
* Caltech's Learning From Data course includes a fantastic video on [visualizing bias and variance](http://work.caltech.edu/library/081.html) (15 minutes).
* [Random Test/Train Split is Not Always Enough](http://www.win-vector.com/blog/2015/01/random-testtrain-split-is-not-always-enough/) explains why random train/test split may not be a suitable model evaluation procedure if your data has a significant time element.

**Reproducibility Resources:**
* [What We've Learned About Sharing Our Data Analysis](https://source.opennews.org/en-US/articles/what-weve-learned-about-sharing-our-data-analysis/) includes tips from BuzzFeed News about how to publish a reproducible analysis.
* [Software development skills for data scientists](http://treycausey.com/software_dev_skills.html) discusses the importance of writing functions and proper code comments (among other skills), which are highly useful for creating a reproducible analysis.
* [Data science done well looks easy - and that is a big problem for data scientists](http://simplystatistics.org/2015/03/17/data-science-done-well-looks-easy-and-that-is-a-big-problem-for-data-scientists/) explains how a reproducible analysis demonstrates all of the work that goes into proper data science.

-----

### Class 10: Linear Regression
* Machine learning exercise ([article](http://blog.dominodatalab.com/10-interesting-uses-of-data-science/))
* Linear regression ([notebook](notebooks/10_linear_regression.ipynb))
    * [Capital Bikeshare dataset](data/bikeshare.csv) used in a Kaggle competition
    * [Data dictionary](https://www.kaggle.com/c/bike-sharing-demand/data)
* Why we should examine data well before building a model: Anscombes_Quartet [(notebook)](notebooks/10_Anscombes_Quartet.ipynb)
* Feature engineering example: [Predicting User Engagement in Corporate Collaboration Network](https://github.com/mikeyea/DAT7_project/blob/master/final%20project/Class_Presention_MYea.ipynb)

**Homework:**
* Your first project presentation is on Thursday (12/3)! Please submit a link to your project repository (with slides, code, data, and visualizations) by 6pm on Tuesday.
* Complete the [homework assignment](homework/10_yelp_votes_homework.ipynb) with the [Yelp data](data/yelp.csv). This is due on Tuesday (12/8).

**Linear Regression Resources:**
* To go much more in-depth on linear regression, read Chapter 3 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). Alternatively, watch the [related videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) or read Kevin Markhams [quick reference guide](http://www.dataschool.io/applying-and-interpreting-linear-regression/) to the key points in that chapter.
* This [introduction to linear regression](http://people.duke.edu/~rnau/regintro.htm) is more detailed and mathematically thorough, and includes lots of good advice.
* This is a relatively quick post on the [assumptions of linear regression](http://pareonline.net/getvn.asp?n=2&v=8).
* Setosa has an [interactive visualization](http://setosa.io/ev/ordinary-least-squares-regression/) of linear regression.

<!--
* For a brief introduction to confidence intervals, hypothesis testing, p-values, and R-squared, as well as a comparison between scikit-learn code and [Statsmodels](http://statsmodels.sourceforge.net/) code, read my [DAT7 lesson on linear regression](https://github.com/justmarkham/DAT7/blob/master/notebooks/10_linear_regression.ipynb). 

* Here is a useful explanation of [confidence intervals](http://www.quora.com/What-is-a-confidence-interval-in-laymans-terms/answer/Michael-Hochster) from Quora.
* [Hypothesis Testing: The Basics](http://20bits.com/article/hypothesis-testing-the-basics) provides a nice overview of the topic, and John Rauser's talk on [Statistics Without the Agonizing Pain](https://www.youtube.com/watch?v=5Dnw46eC-0o) (12 minutes) gives a great explanation of how the null hypothesis is rejected.
* Earlier this year, a major scientific journal banned the use of p-values:
    * Scientific American has a nice [summary](http://www.scientificamerican.com/article/scientists-perturbed-by-loss-of-stat-tools-to-sift-research-fudge-from-fact/) of the ban.
    * This [response](http://www.nature.com/news/statistics-p-values-are-just-the-tip-of-the-iceberg-1.17412) to the ban in Nature argues that "decisions that are made earlier in data analysis have a much greater impact on results".
    * Andrew Gelman has a readable [paper](http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf) in which he argues that "it's easy to find a p < .05 comparison even if nothing is going on, if you look hard enough".
    * [Science Isn't Broken](http://fivethirtyeight.com/features/science-isnt-broken/) includes a neat tool that allows you to "p-hack" your way to "statistically significant" results.
* [Accurately Measuring Model Prediction Error](http://scott.fortmann-roe.com/docs/MeasuringError.html) compares adjusted R-squared, AIC and BIC, train/test split, and cross-validation.

**Other Resources:**
* Section 3.3.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (4 pages) has a great explanation of dummy encoding for categorical features.
* Kaggle has some nice [visualizations of the bikeshare data](https://www.kaggle.com/c/bike-sharing-demand/scripts?outputType=Visualization) we used today.

-----


### Class 11: First Project Presentation
* Project presentations!

**Homework:**
* Watch Rahul Patwari's videos on [probability](https://www.youtube.com/watch?v=o4QmoNfW3bI) (5 minutes) and [odds](https://www.youtube.com/watch?v=GxbXQjX7fC0) (8 minutes) if you're not comfortable with either of those terms.
* Read these excellent articles from BetterExplained: [An Intuitive Guide To Exponential Functions & e](http://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) and [Demystifying the Natural Logarithm (ln)](http://betterexplained.com/articles/demystifying-the-natural-logarithm-ln/). Then, review this [brief summary](notebooks/12_e_log_examples.ipynb) of exponential functions and logarithms.

-----

### Class 12: Logistic Regression
* Yelp votes homework due ([notebook](homework/10_yelp_votes_homework.ipynb))
* Logistic regression ([notebook](notebooks/12_logistic_regression.ipynb))
    * [Glass identification dataset](https://archive.ics.uci.edu/ml/datasets/Glass+Identification)
* Exercise with Titanic data ([notebook](notebooks/12_titanic_confusion.ipynb), [data](data/titanic.csv), [data dictionary](https://www.kaggle.com/c/titanic/data))
* Confusion matrix ([slides](slides/12_confusion_matrix.pdf), [notebook](notebooks/12_titanic_confusion.ipynb))

**Homework:**
* If you aren't yet comfortable with all of the confusion matrix terminology, watch Rahul Patwari's videos on [Intuitive sensitivity and specificity](https://www.youtube.com/watch?v=U4_3fditnWg) (9 minutes) and [The tradeoff between sensitivity and specificity](https://www.youtube.com/watch?v=vtYDyGGeQyo) (13 minutes).
* Video/reading assignment on [ROC curves and AUC](homework/13_roc_auc.md)
* Video/reading assignment on [cross-validation](homework/13_cross_validation.md)

**Logistic Regression Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), or watch the [first three videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) (30 minutes) from that chapter.
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of four classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes) and one classifier we do not cover (Support Vector Machines).

**Confusion Matrix Resources:**
* Kevin Markham's [simple guide to confusion matrix terminology](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) may be useful to you as a reference.
* This blog post about [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/amazon-machine-learning-make-data-driven-decisions-at-scale/) contains a neat [graphic](https://media.amazonwebservices.com/blog/2015/ml_adjust_model_1.png) showing how classification threshold affects different evaluation metrics.
* This notebook (from another DAT course) explains [how to calculate "expected value"](https://github.com/podopie/DAT18NYC/blob/master/classes/13-expected_value_cost_benefit_analysis.ipynb) from a confusion matrix by treating it as a cost-benefit matrix.

-----

### Class 13: Advanced Model Evaluation
* Data preparation ([notebook](notebooks/13_advanced_model_evaluation.ipynb))
    * Handling missing values
    * Handling categorical features (review)
* ROC curves and AUC
    * Discuss the [video/reading assignment](homework/13_roc_auc.md)
    * Exercise: drawing an ROC curve ([slides](slides/13_drawing_roc.pdf))
    * Return to the main notebook
* Cross-validation
    * Discuss the [video/reading assignment](homework/13_cross_validation.md) and associated [notebook](notebooks/13_cross_validation.ipynb)
    * Return to the main notebook
* Exercise with bank marketing data ([notebook](notebooks/13_bank_exercise.ipynb), [data](data/bank-additional.csv), [data dictionary](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing))

**Homework:**
* Reading assignment on [spam filtering](homework/14_spam_filtering.md)
* Read these [Introduction to Probability](https://docs.google.com/presentation/d/1cM2dVbJgTWMkHoVNmYlB9df6P2H8BrjaqAcZTaLe9dA/edit#slide=id.gfc3caad2_00) slides, or skim section 2.1 of the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php?stat_book=os) (12 pages). Pay specific attention to the following terms: probability, mutually exclusive, sample space, independent.
* **Optional:** Try to gain an understanding of conditional probability from this [visualization](http://setosa.io/conditional/).
* **Optional:** For an intuitive introduction to Bayes' theorem, read these posts on [wealth and happiness](http://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule/answer/Michael-Hochster), [ducks](https://planspacedotorg.wordpress.com/2014/02/23/bayes-rule-for-ducks/), or [legos](http://www.countbayesie.com/blog/2015/2/18/bayes-theorem-with-lego).

**ROC Resources:**
* Rahul Patwari has a great video on [ROC Curves](https://www.youtube.com/watch?v=21Igj5Pr6u4) (12 minutes).
* [An introduction to ROC analysis](http://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) is a very readable paper on the topic.
* ROC curves can be used across a wide variety of applications, such as [comparing different feature sets](http://research.microsoft.com/pubs/205472/aisec10-leontjeva.pdf) for detecting fraudulent Skype users, and [comparing different classifiers](http://www.cse.ust.hk/nevinZhangGroup/readings/yi/Bradley_PR97.pdf) on a number of popular datasets.

**Cross-Validation Resources:**
* For more on cross-validation, read section 5.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (11 pages) or watch the related videos: [K-fold and leave-one-out cross-validation](https://www.youtube.com/watch?v=nZAM5OXrktY) (14 minutes), [cross-validation the right and wrong ways](https://www.youtube.com/watch?v=S06JpVoNaA0) (10 minutes).
* If you want to understand the different variations of cross-validation, this [paper](http://www.jcheminf.com/content/pdf/1758-2946-6-10.pdf) examines and compares them in detail.
* To learn how to use [GridSearchCV and RandomizedSearchCV](http://scikit-learn.org/stable/modules/grid_search.html) for parameter tuning, watch [How to find the best model parameters in scikit-learn](https://www.youtube.com/watch?v=Gol_qOgRqfA) (28 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb).

**Other Resources:**
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html).
* [Counterfactual evaluation of machine learning models](https://www.youtube.com/watch?v=QWCSxAKR-h0) (45 minutes) is an excellent talk about the sophisticated way in which Stripe evaluates its fraud detection model. (These are the associated [slides](http://www.slideshare.net/MichaelManapat/counterfactual-evaluation-of-machine-learning-models).)
* [Visualizing Machine Learning Thresholds to Make Better Business Decisions](http://blog.insightdatalabs.com/visualizing-classifier-thresholds/) demonstrates how visualizing precision, recall, and "queue rate" at different thresholds can help you to maximize the business value of your classifier.

-----

### Class 14: Naive Bayes and Text Data
* Conditional probability and Bayes' theorem
    * [Slides](slides/14_bayes_theorem.pdf) (adapted from [Visualizing Bayes' theorem](http://oscarbonilla.com/2009/05/visualizing-bayes-theorem/))
    * Applying Bayes' theorem to iris classification ([notebook](notebooks/14_bayes_theorem_iris.ipynb))
* Naive Bayes classification
    * [Slides](slides/14_naive_bayes.pdf)
    * Spam filtering example ([notebook](notebooks/14_naive_bayes_spam.ipynb))
* Applying Naive Bayes to text data in scikit-learn ([notebook](notebooks/14_text_data_sklearn.ipynb))
    * [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) documentation
    * SMS messages: [data](data/sms.tsv), [data dictionary](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

**Homework:**
* Complete this new [homework assignment](homework/14_yelp_review_text.md) with the [Yelp data](data/yelp.csv). This is due on Tuesday (12/22).
* Confirm that you have [TextBlob](https://textblob.readthedocs.org/) installed by running `import textblob` from within your preferred Python environment. If it's not installed, run `pip install textblob` at the command line (not from within Python).

**Resources:**
* Sebastian Raschka's article on [Naive Bayes and Text Classification](http://sebastianraschka.com/Articles/2014_naive_bayes_1.html) covers the conceptual material from today's class in much more detail.
* For more on conditional probability, read these [slides](https://docs.google.com/presentation/d/1psUIyig6OxHQngGEHr3TMkCvhdLInnKnclQoNUr4G4U/edit#slide=id.gfc69f484_00), or read section 2.2 of the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php?stat_book=os) (15 pages).
* For an intuitive explanation of Naive Bayes classification, read this post on [airport security](http://www.quora.com/In-laymans-terms-how-does-Naive-Bayes-work/answer/Konstantin-Tt).
* For more details on Naive Bayes classification, Wikipedia has two excellent articles ([Naive Bayes classifier](http://en.wikipedia.org/wiki/Naive_Bayes_classifier) and [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)), and Cross Validated has a good [Q&A](http://stats.stackexchange.com/questions/21822/understanding-naive-bayes).
* When applying Naive Bayes classification to a dataset with continuous features, it is better to use [GaussianNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) rather than [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html). This [notebook](notebooks/14_types_of_naive_bayes.ipynb) compares their performances on such a dataset. Wikipedia has a short [description](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes) of Gaussian Naive Bayes, as well as an excellent [example](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Sex_classification) of its usage.
* These [slides](http://www.umiacs.umd.edu/~jbg/teaching/DATA_DIGGING/lecture_05.pdf) from the University of Maryland provide more mathematical details on both logistic regression and Naive Bayes, and also explain how Naive Bayes is actually a "special case" of logistic regression.
* Andrew Ng has a [paper](http://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf) comparing the performance of logistic regression and Naive Bayes across a variety of datasets.
* If you enjoyed Paul Graham's article, you can read [his follow-up article](http://www.paulgraham.com/better.html) on how he improved his spam filter and this [related paper](http://www.merl.com/publications/docs/TR2004-091.pdf) about state-of-the-art spam filtering in 2004.
* Yelp has found that Naive Bayes is more effective than Mechanical Turks at [categorizing businesses](http://engineeringblog.yelp.com/2011/02/towards-building-a-high-quality-workforce-with-mechanical-turk.html).

-----

### Class 15: Natural Language Processing
* Natural language processing ([notebook](notebooks/15_natural_language_processing.ipynb))
 * Vectorization/Tokenization
 * Stopword Removal
 * Other CountVectorizer options
 * Intro to [TextBlob](https://textblob.readthedocs.org/en/dev/)
  * Stemming and Lemmatization
  * Term Frequency-Inverse Document Frequency (TF-IDF)
  *  Using TF-IDF to Summarize a Yelp Review
  *  Sentiment Analysis
* Overview of how Kaggle competitions work ([slides](slides/16_kaggle.pdf))

<!--
* Introduction to our [Kaggle competition](https://inclass.kaggle.com/c/dat8-stack-overflow)
    * Create a Kaggle account, join the competition using the invitation link, download the sample submission, and then submit the sample submission (which will require SMS account verification).
    
**Homework:**
* **Your draft paper is due on Thursday (12/22)!** Please submit a link to your project repository (with paper, code, data, and visualizations) before class
* The [homework assignment](homework/14_yelp_review_text_homework.ipynb) with the [Yelp data](data/yelp.csv) is due on Tuesday (12/22)
* Watch [Kaggle: How it Works](https://www.youtube.com/watch?v=PoD84TVdD-4) (4 minutes) for a brief overview of the Kaggle competiton platform

<!--
* Watch [Kaggle: How it Works](https://www.youtube.com/watch?v=PoD84TVdD-4) (4 minutes) for a brief overview of the Kaggle platform.

* Download the competition files, move them to the `DAT8/data` directory, and make sure you can open the CSV files using Pandas. If you have any problems opening the files, you probably need to turn off real-time virus scanning (especially Microsoft Security Essentials).

* **Optional:** Come up with some theories about which features might be relevant to predicting the response, and then explore the data to see if those theories appear to be true.
* **Optional:** Watch Kevin Markum's [project presentation video](https://www.youtube.com/watch?v=HGr1yQV3Um0) (16 minutes) for a tour of the end-to-end machine learning process for a Kaggle competition, including feature engineering.
-->
<!--
(Or, just read through the [slides](https://speakerdeck.com/justmarkham/allstate-purchase-prediction-challenge-on-kaggle).)

**NLP Resources:**
* If you want to learn a lot more NLP, check out the excellent [video lectures](https://class.coursera.org/nlp/lecture) and [slides](http://web.stanford.edu/~jurafsky/NLPCourseraSlides.html) from this [Coursera course](https://www.coursera.org/course/nlp) (which is no longer being offered).
* This slide deck defines many of the [key NLP terms](https://github.com/ga-students/DAT_SF_9/blob/master/16_Text_Mining/DAT9_lec16_Text_Mining.pdf).
* [Natural Language Processing with Python](http://www.nltk.org/book/) is the most popular book for going in-depth with the [Natural Language Toolkit](http://www.nltk.org/) (NLTK).
* [A Smattering of NLP in Python](https://github.com/charlieg/A-Smattering-of-NLP-in-Python/blob/master/A%20Smattering%20of%20NLP%20in%20Python.ipynb) provides a nice overview of NLTK

<!-- , as does this [notebook from DAT5](https://github.com/justmarkham/DAT5/blob/master/notebooks/14_nlp.ipynb).
* [spaCy](http://spacy.io/) is a newer Python library for text processing that is focused on performance (unlike NLTK).
* If you want to get serious about NLP, [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml) is a suite of tools (written in Java) that is highly regarded.
* When working with a large text corpus in scikit-learn, [HashingVectorizer](http://scikit-learn.org/stable/modules/feature_extraction.html#vectorizing-a-large-text-corpus-with-the-hashing-trick) is a useful alternative to CountVectorizer.
* [Automatically Categorizing Yelp Businesses](http://engineeringblog.yelp.com/2015/09/automatically-categorizing-yelp-businesses.html) discusses how Yelp uses NLP and scikit-learn to solve the problem of uncategorized businesses.
* [Modern Methods for Sentiment Analysis](http://districtdatalabs.silvrback.com/modern-methods-for-sentiment-analysis) shows how "word vectors" can be used for more accurate sentiment analysis.
* [Identifying Humorous Cartoon Captions](http://www.cs.huji.ac.il/~dshahaf/pHumor.pdf) is a readable paper about identifying funny captions submitted to the New Yorker Caption Contest.

<!--
* [DC Natural Language Processing](http://www.meetup.com/DC-NLP/) is an active Meetup group in our local area.


-----

### Class 16: Neural Networks and SVC
* Artificial Neural Networks (ANN)
 * [slides](slides/16_nn_svm.pdf)
 * [notebook](notebook/16_nn_svc.ipynb)
* SVC (Support Vector Classifier)
 * [slides](slides/16_nn_svm.pdf)
 * [notebook](notebook/16_nn_svc.ipynb)


**SVC resources**
* For a more in-depth inderstanding of Support Vector Machines and SVC, read Chapter 9 of Hastie and Tibshirani's excellent book, [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). (It's a free PDF download!)
* SVC videos by the authors of An Introduction to Statistical Learning can be found [here](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/).

**ANN resources**
* For a more background of on Artificial Neural Networks view this series.  It describes the logic behind ANN from a low level logic step by step point of view: 
 * Part 1 https://www.youtube.com/watch?v=bxe2T-V8XRs
 * Part 2 https://www.youtube.com/watch?v=UJwK6jAStmg
 * Part 3 https://www.youtube.com/watch?v=5u0jaA3qAGk
 * Part 4 https://www.youtube.com/watch?v=GlcnxUlrtek
 * Part 5 https://www.youtube.com/watch?v=pHMzNW8Agq4
 * Part 6 https://www.youtube.com/watch?v=9KM9Td6RVgQ
 * Part 7 https://www.youtube.com/watch?v=S4ZUwgesjS8

**Kaggle Resources:**
* [Specialist Knowledge Is Useless and Unhelpful](http://www.slate.com/articles/health_and_science/new_scientist/2012/12/kaggle_president_jeremy_howard_amateurs_beat_specialists_in_data_prediction.html) is a brief interview with Jeremy Howard (past president of Kaggle) in which he argues that data science skills are much more important than domain expertise for creating effective predictive models.
* [Getting in Shape for the Sport of Data Science](https://www.youtube.com/watch?v=kwt6XEh7U3g) (74 minutes), also by Jeremy Howard, contains a lot of tips for competitive machine learning.
* [Learning from the best](http://blog.kaggle.com/2014/08/01/learning-from-the-best/) is an excellent blog post covering top tips from Kaggle Masters on how to do well on Kaggle.
* [Feature Engineering Without Domain Expertise](https://www.youtube.com/watch?v=bL4b1sGnILU) (17 minutes), a talk by Kaggle Master Nick Kridler, provides some simple advice about how to iterate quickly and where to spend your time during a Kaggle competition.
* These examples may help you to better understand the process of feature engineering: predicting the number of [passengers at a train station](https://medium.com/@chris_bour/french-largest-data-science-challenge-ever-organized-shows-the-unreasonable-effectiveness-of-open-8399705a20ef), identifying [fraudulent users of an online store](https://docs.google.com/presentation/d/1UdI5NY-mlHyseiRVbpTLyvbrHxY8RciHp5Vc-ZLrwmU/edit#slide=id.p), identifying [bots in an online auction](https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/forums/t/14628/share-your-secret-sauce), predicting who will [subscribe to the next season of an orchestra](http://blog.kaggle.com/2015/01/05/kaggle-inclass-stanfords-getting-a-handel-on-data-science-winners-report/), and evaluating the [quality of e-commerce search engine results](http://blog.kaggle.com/2015/07/22/crowdflower-winners-interview-3rd-place-team-quartet/).
* [Our perfect submission](https://www.kaggle.com/c/restaurant-revenue-prediction/forums/t/13950/our-perfect-submission) is a fun read about how great performance on the [public leaderboard](https://www.kaggle.com/c/restaurant-revenue-prediction/leaderboard/public) does not guarantee that a model will generalize to new data.
* [10 things I wish I knew... about Machine Learning Competitions](http://people.inf.ethz.ch/jaggim/meetup/slides/ML-meetup-9-vonRohr-kaggle.pdf) contains a great set of tips, many of which are good tips for non-competition machine learning model development as well.

-----

### Class 17: Review and refresh
* Data science intro 	
 * [L01 Introduction to Data Science](#class-1-introduction-to-data-science)
 	* **Data Science workflow ([slides](slides/01_data_science_intro.pdf))**
 * [L02 Command Line, Version Control](#class-2-command-line-and-version-control)	
* Acquiring and preparing data	
 * [L03 Reading and preparing data](#class-3-reading-and-preparing-data)	
 * [L07 Fetching Data](#class-7-fetching-data)	
* Evaluating datasets with attributes and methods	
 * [L04 Exploratory Data Analysis](#class-4-exploratory-data-analysis)	
  * **Exercise with dataframe attributes and methods: ([code](code/04_pandas.py))**
	  * MovieLens 100k movie ratings ([data](data/u.user), [data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt), [website](http://grouplens.org/datasets/movielens/))
* Visualization	
 * [L05 Visualization](#class-5-visualization)	
	 * **Visualization with Pandas and Matplotlib ([notebook](notebooks/05_pandas_visualization.ipynb))**
* Machine Learning
	* **Supervised or unsupervised, continuous or categorical ([slides](slides/06_machine_learning.pdf))**
	* [L06 Machine Learning](#class-6-machine-learning)	
* Predictive models
	* **Excercise: Choose appropriate estimators**
	* Supervised - predict continuous values
		* [L10 Linear Regression](#class-10-linear-regression)
	* Supervised Classifiers - predict a label
 		* [L08 K-Nearest Neighbors](#class-8-k-nearest-neighbors)	
 		* [L12 Logistic Regression](#class-12-logistic-regression)
 		* [L14 Naive Bayes and Text Data](#class-14-naive-bayes-and-text-data)
 		* [L15 Natural Language Processing](#class-15-natural-language-processing)
* Model Evaluation	
 * [L09 Basic Model Evaluation](#class-9-basic-model-evaluation)	
 * [L13 Advanced Model Evaluation](#class-13-advanced-model-evaluation)	

-----

### Class 18: Regularization and Clustering
**By the end of this lesson you will be able to:**

* Standardize features
* Cluster using K-means and DBSCAN
* Compare "how good" the clustering models are

**Topics/Highlights**

* Advanced scikit-learn ([notebook](notebooks/19_advanced_sklearn.ipynb))
    * [StandardScaler](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html): standardizing features
    * [Pipeline](http://scikit-learn.org/stable/modules/pipeline.html): chaining steps
* Clustering ([slides](slides/19_clustering.pdf), [notebook](notebooks/19_clustering.ipynb))
    * K-means: [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html), [visualization 1](http://tech.nitoyon.com/en/blog/2013/11/07/k-means/), [visualization 2](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
    	* [My clustering of colors in an image.  Used a loop to generate clusters of 1 to 256 clusters. Made into an animated gif out of them.  Fun!](https://github.com/JamesByers/Cluster-analysis-of-image-RGB-colors/blob/master/Output%20Newport_seafood%20image%20and%20Animated%20GIF/Newport_seafood_k_means%2B%2B_cluster_animated.gif)
    * DBSCAN: [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html), [visualization](http://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)

**Homework:**
* Reread [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html). (The "answers" to the [guiding questions](homework/solutions/09_bias_variance.md) have been posted and may be helpful to you.)
* **Optional:** Watch these two excellent (and related) videos from Caltech's Learning From Data course: [bias-variance tradeoff](http://work.caltech.edu/library/081.html) (15 minutes) and [regularization](http://work.caltech.edu/library/121.html) (8 minutes).

**scikit-learn Resources:**
* This is a longer example of [feature scaling](https://github.com/rasbt/pattern_classification/blob/master/preprocessing/about_standardization_normalization.ipynb) in scikit-learn, with additional discussion of the types of scaling you can use.
* [Practical Data Science in Python](http://radimrehurek.com/data_science_python/) is a long and well-written notebook that uses a few advanced scikit-learn features: pipelining, plotting a learning curve, and pickling a model.
* To learn how to use [GridSearchCV and RandomizedSearchCV](http://scikit-learn.org/stable/modules/grid_search.html) for parameter tuning, watch [How to find the best model parameters in scikit-learn](https://www.youtube.com/watch?v=Gol_qOgRqfA) (28 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb).
* Sebastian Raschka has a number of excellent resources for scikit-learn users, including a repository of [tutorials and examples](https://github.com/rasbt/pattern_classification), a library of machine learning [tools and extensions](http://rasbt.github.io/mlxtend/), a new [book](https://github.com/rasbt/python-machine-learning-book), and a semi-active [blog](http://sebastianraschka.com/blog/).
* scikit-learn has an incredibly active [mailing list](https://www.mail-archive.com/scikit-learn-general@lists.sourceforge.net/index.html) that is often much more useful than Stack Overflow for researching functions and asking questions.
* If you forget how to use a particular scikit-learn function that we have used in class, don't forget that this repository is fully searchable!

**Clustering Resources:**
* For a very thorough introduction to clustering, read chapter 8 (69 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php) (available as a free download), or browse through the chapter 8 slides.
* scikit-learn's user guide compares many different [types of clustering](http://scikit-learn.org/stable/modules/clustering.html).
* This [PowerPoint presentation](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic6-Clustering.ppt) from Columbia's Data Mining class provides a good introduction to clustering, including hierarchical clustering and alternative distance metrics.
* An Introduction to Statistical Learning has useful videos on [K-means clustering](https://www.youtube.com/watch?v=aIybuNt9ps4&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (17 minutes) and [hierarchical clustering](https://www.youtube.com/watch?v=Tuuc9Y06tAc&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (15 minutes).
* This is an excellent interactive visualization of [hierarchical clustering](https://joyofdata.shinyapps.io/hclust-shiny/).
* This is a nice animated explanation of [mean shift clustering](http://spin.atomicobject.com/2015/05/26/mean-shift-clustering/).
* The [K-modes algorithm](http://www.cs.ust.hk/~qyang/Teaching/537/Papers/huang98extensions.pdf) can be used for clustering datasets of categorical features without converting them to numerical values. Here is a [Python implementation](https://github.com/nicodv/kmodes).
* Here are some fun examples of clustering: [A Statistical Analysis of the Work of Bob Ross](http://fivethirtyeight.com/features/a-statistical-analysis-of-the-work-of-bob-ross/) (with [data and Python code](https://github.com/fivethirtyeight/data/tree/master/bob-ross)), [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/), and [characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/).

-----

### Class 19: Decision Trees
**By the end of this lesson you will be able to:**

* Create a Regression tree
* Graph and interpret the decision tree

**Topics/Highlights**

* Finish DBSCAN clustering lesson ([slides](slides/19_clustering.pdf), [notebook](notebooks/19_clustering.ipynb))
* Decision trees ([notebook](notebooks/17_decision_trees.ipynb))
* 	Part 1: Regression trees
* Exercise with Capital Bikeshare data ([notebook](notebooks/17_bikeshare_exercise.ipynb), [data](data/bikeshare.csv), [data dictionary](https://www.kaggle.com/c/bike-sharing-demand/data))

**Homework:**
* Read the "Wisdom of the crowds" section from MLWave's post on [Human Ensemble Learning](http://mlwave.com/human-ensemble-learning/).
* **Optional:** Read the abstract from [Do We Need Hundreds of Classifiers to Solve Real World Classification Problems?](http://jmlr.csail.mit.edu/papers/volume15/delgado14a/delgado14a.pdf), as well as Kaggle CTO Ben Hamner's [comment](https://news.ycombinator.com/item?id=8719723) about the paper, paying attention to the mentions of "Random Forests".

**Resources:**
* scikit-learn's documentation on [decision trees](http://scikit-learn.org/stable/modules/tree.html) includes a nice overview of trees as well as tips for proper usage.
* For a more thorough introduction to decision trees, read section 4.3 (23 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php). (Chapter 4 is available as a free download.)
* If you want to go deep into the different decision tree algorithms, this slide deck contains [A Brief History of Classification and Regression Trees](https://drive.google.com/file/d/0B-BKohKl-jUYQ3RpMEF0OGRUU3RHVGpHY203NFd3Z19Nc1ZF/view).
* [The Science of Singing Along](http://www.doc.gold.ac.uk/~mas03dm/papers/PawleyMullensiefen_Singalong_2012.pdf) contains a neat regression tree (page 136) for predicting the percentage of an audience at a music venue that will sing along to a pop song.
* Decision trees are common in the medical field for differential diagnosis, such as this classification tree for [identifying psychosis](http://www.psychcongress.com/sites/naccme.com/files/images/pcn/saundras/psychosis_decision_tree.pdf).

-----

### Class 20: Ensembling, Bagging and Random Forests

* Finish decision trees lesson ([notebook](notebooks/17_decision_trees.ipynb))
* Ensembling, Bagging and Random Forests ([notebook](notebooks/18_ensembling.ipynb))
    * [Major League Baseball player data](data/hitters.csv) from 1986-87
    * [Data dictionary](https://cran.r-project.org/web/packages/ISLR/ISLR.pdf) (see page 7)

**Resources:**
* scikit-learn's documentation on [ensemble methods](http://scikit-learn.org/stable/modules/ensemble.html) covers both "averaging methods" (such as bagging and Random Forests) as well as "boosting methods" (such as AdaBoost and Gradient Tree Boosting).
* MLWave's [Kaggle Ensembling Guide](http://mlwave.com/kaggle-ensembling-guide/) is very thorough and shows the many different ways that ensembling can take place.
* Browse the excellent [solution paper](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/ChenglongChen/Kaggle_CrowdFlower/master/Doc/Kaggle_CrowdFlower_ChenglongChen.pdf) from the winner of Kaggle's [CrowdFlower competition](https://www.kaggle.com/c/crowdflower-search-relevance) for an example of the work and insight required to win a Kaggle competition.
* [Interpretable vs Powerful Predictive Models: Why We Need Them Both](https://medium.com/@chris_bour/interpretable-vs-powerful-predictive-models-why-we-need-them-both-990340074979) is a short post on how the tactics useful in a Kaggle competition are not always useful in the real world.
* [Not Even the People Who Write Algorithms Really Know How They Work](http://www.theatlantic.com/technology/archive/2015/09/not-even-the-people-who-write-algorithms-really-know-how-they-work/406099/) argues that the decreased interpretability of state-of-the-art machine learning models has a negative impact on society.
* For an intuitive explanation of Random Forests, read Edwin Chen's answer to [How do random forests work in layman's terms?](http://www.quora.com/Random-Forests/How-do-random-forests-work-in-laymans-terms/answer/Edwin-Chen-1)
* [Large Scale Decision Forests: Lessons Learned](http://blog.siftscience.com/blog/2015/large-scale-decision-forests-lessons-learned) is an excellent post from Sift Science about their custom implementation of Random Forests.
* [Unboxing the Random Forest Classifier](http://nerds.airbnb.com/unboxing-the-random-forest-classifier/) describes a way to interpret the inner workings of Random Forests beyond just feature importances.
* [Understanding Random Forests: From Theory to Practice](http://arxiv.org/pdf/1407.7502v3.pdf) is an in-depth academic analysis of Random Forests, including details of its implementation in scikit-learn.

-----

### Class 21: Bonus Topics

**Topics/Highlights**

* Additional models and variants - Exercise
* Trends
	* Data storage, Hadoop and MapReduce
		* SQL databases
		* NoSQL vs. SQL databases ([comparison](http://core0.staticworld.net/images/article/2014/10/sql-nosql-b-100527236-large.idge.gif))
		* Distributed files [(diagram)](https://www.google.com/search?q=hadoop+storage+impala+diagram&source=lnms&tbm=isch)
	* AWS, Azure and Google,  data and data science engine services
		* SQL Databases in the cloud
			* AWS Redshift, Oracle, SQL Server
			* Azure SQL Server
			* Google BigQuery
		* NoSQL Databases
			* AWS Mongo, DynamoDB
			* Azure
		* Data collection for IoT
		* Data science engines - ex. [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/)
* Exercise - top takeaways and top surprises
* Where to go from here data scientists!
	* [Data science skills hierarchy](https://docs.google.com/spreadsheets/d/1RAcC44o3crC2ZeCmtrELibV1VyEB5ecnBHZKXXXZI6M)
* Next steps in your journey
	* [Exercise: your objectives and next steps](https://docs.google.com/spreadsheets/d/13z-eUjMtsSyO6B51iVzoEwmfpO-IhymoYDIVvgTious/edit?usp=sharing)

**Additional models and variants (in blue)**

* Classifiers
	* Naïve Bayes
	* KNN
	* SVC
	* [SDG](http://scikit-learn.org/stable/modules/sgd.html)
	* Decision Trees
	* Neural Networks
* Ensemble methods [(scikit-learn pqge)](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble)
	* Bagging
	* Boosting
		* [sklearn.ensemble.AdaBoostRegressor](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)
		* Beware, even one misclassified label in training data can result in poor prediction
	* Random Forests
* Regression
	* Linear regression
	* [Ridge regression](http://scikit-learn.org/stable/modules/linear_model.html) 
	* [Lasso](http://scikit-learn.org/stable/modules/linear_model.html)
	* [Linear regressor with polynomial preprocessing](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
	* [SVR (choose from several kernels)](http://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html)
	* [SDG regression](http://scikit-learn.org/stable/modules/sgd.html)
	* Ensembling
		* [Random Forest regression](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* Clustering
	* K-means
	* DBSCAN
	* [Hierarchical clustering](https://joyofdata.shinyapps.io/hclust-shiny/)
-->
<!--
### Before the Course Begins
* Install [Git](http://git-scm.com/downloads).
* Create an account on the [GitHub](https://github.com/) website.
    * It is not necessary to download "GitHub for Windows" or "GitHub for Mac"
* Install the [Anaconda distribution](http://continuum.io/downloads) of Python 2.7x.
    * If you choose not to use Anaconda, here is a list of the [Python packages](other/python_packages.md) you will need to install during the course.
* We would like to check the setup of your laptop before the course begins:
    * You can have your laptop checked prior to class on 10/27 from 5:00-5:45PM.
    * Alternatively, you can walk through the [setup checklist](other/setup_checklist.md) yourself.
* Once you receive an email invitation from Slack, join our "SEA-DAT1" Slack group and add your photo.
* Practice Python using the resources below.

### Additional Python Resources
* [Codecademy's Python course](http://www.codecademy.com/en/tracks/python): Good beginner material, including tons of in-browser exercises.
* [Google's Python Class](https://developers.google.com/edu/python/): Slightly more advanced, including hours of useful lecture videos and downloadable exercises (with solutions).
* [Introduction to Python](http://introtopython.org/): A series of IPython notebooks that do a great job explaining core Python concepts and data structures.
* [Python for Informatics](http://www.pythonlearn.com/book.php): A very beginner-oriented book, with associated [slides](https://drive.google.com/folderview?id=0B7X1ycQalUnyal9yeUx3VW81VDg&usp=sharing) and [videos](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ).
* [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182): Read through the Overview section for a very quick introduction to Python.
* [Python Quick Reference Guide](other/python_reference): Kevin Markham's beginner-oriented guide that demonstrates Python concepts through short, well-commented examples.
* [Beginner](code/00_python_beginner_workshop.py) and [intermediate](code/00_python_intermediate_workshop.py) workshop code: Useful for review and reference.
* [Python Tutor](http://pythontutor.com/): Allows you to visualize the execution of Python code.
-->



<!--
### [Comparison of machine learning models](other/model_comparison.md)
-->
 
<!--
### [Comparison of model evaluation procedures and metrics](other/model_evaluation_comparison.md)
# http://3.bp.blogspot.com/-dofu6J0sZ8o/UrctKb69QdI/AAAAAAAADfg/79ewPecn5XU/s1600/scikit-learn-flow-chart.jpg
-->
