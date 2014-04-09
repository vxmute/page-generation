#!/usr/bin/env python
import json
import os
from string import Template

#read config
f = json.loads(open("conf.json","r").read())
t = Template(open(f["template"],"r").read())

# top link list
links = ""
lh = Template("<a href=\"$link\">$name</a>")
for i in range(0,len(f["links"])):
	links += lh.substitute(\
			link=f["links"][i]["link"],\
			name=f["links"][i]["name"])
	if i < len(f["links"])-1:
		links += " - "

# sidebar list
sidebar_l = ""
for i in range(0,len(f["articles"])):
	sidebar_l += lh.substitute(\
			link=f["articles"][i]["new_path"],\
			name=f["articles"][i]["title"])
	if i < len(f["articles"])-1:
		sidebar_l += "</br>"

# generate and write files
c = f["articles"]
for i in range(0,len(c)):
	a = (open(c[i]["location"]).read())
	a = a.replace("<","&lt;").replace(">","&gt;")
	o = t.substitute(\
			stylesheet=f["style"],\
			title=c[i]["title"],\
			header=f["header"],\
			subheader=f["subheader"],\
			links=links,\
			sidebar=sidebar_l,\
			article=a,\
			date=f["date"],\
			generatedby=f["generated_by"])
	out = open(f["outdir"]+c[i]["new_path"],"w")
	out.write(o)
	out.close()

