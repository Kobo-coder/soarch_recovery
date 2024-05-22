# Tools found during research

pylint (pyreverse) - If i try to remove the test folders, information is lost. I haven't found any good way to make it so I can safely remove test files wihout loss of information. Example is `topics.py` imports `TopicFilter` yet there is no connection in the output between `topics.py` and `TopicFilter`
py2puml - Doesn't work. Couldn't make it work without having the domain files as they show in their own example. Since zeegu doesn't have this it doesn't seem to work. Found old examples of someone using it from code, but still it seems that you need the domain file for py2puml to work.
pyviz - Looks like a collection of different visualization frameworks
bokeh - part of pyviz as far as i can tell
codemap - Unfortunately it seems that codemap only allows up to 100 functions for free otherwise you have to pay. (https://codemap.app)
py-call-graph - Doesn't seem well suited for large code bases as it measures calls for single file scripts, and doesn't seem to work well inbetween several files/classes
understand (scitools) - didn't use
archlens - Used in report. Has its flaws.
git truck - used in report
radon - looks like codeclimate uses this which could make it comparable to modu?
modu - own bachelor tool and used in report

