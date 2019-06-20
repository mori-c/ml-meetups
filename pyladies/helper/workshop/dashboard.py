#! /usr/bin/env python3

# import scripts (placed in same directory)
import headlines2
import pusheen_gif2
import cat_ipsum2

headings, links, topic = headlines2.main()
# changed main function in pusheen script to accept parameter
# passing argument value here for fun
pusheen_gif2.main(3)
breed, insight = cat_ipsum2.main()

# set up your HTML  head and style elements
m1 = """
<html>
<head>
    <title>Scraping Fun!</title>
    <style>
        body {
            margin: 25px;
            font-family: arial;
            font-weight: bold;
        }
        img {
            margin: 10px;
            padding-top:15px;
        }
        h1 { font-size: 20px;}
        h2, a{
            font-size: 16px;
            color:purple;
        }
        div.meow{
            font-size: 30px;
            color: #38A43C;
            text-align: center;
        }
    </style>
</head>
<body>
"""

# add HTML tags to handle the data that is being returned by scripts
m2 = "<h1>Latest News about "+topic.upper()+" </h1>"+\
    "<ul><li>"+str(links[0])+"</li>"+\
    "<li>"+str(links[1])+"</li>"+\
    "<li>"+str(links[2])+"</li></ul>"+\
    "<img src='pusheen_1.gif' width='30%' >"+\
    "<img src='pusheen_2.gif' width='30%' >"+\
    "<img src='pusheen_3.gif' width='30%' >"

m3 = "<h1>"+breed.upper()+"'s words of wisdom:</h1><div class='meow'>"+insight+"</div></body></html>"

# create HTML file
f = open('stuff/dashboard.html','w')
# write to file
f.write(m1+m2+m3)
f.close()
print("Done!")
