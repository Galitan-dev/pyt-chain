from Chain import ChainLink

link10 = ChainLink(None, "10")
link9 = ChainLink(link10, "9")
link8 = ChainLink(link9, "8")
link7 = ChainLink(link8, "7")
link6 = ChainLink(link7, "6")
link5 = ChainLink(link6, "5")
link4 = ChainLink(link5, "4")
link3 = ChainLink(link4, "3")
link2 = ChainLink(link3, "2")
link1 = ChainLink(link2, "1")

print(link3.length())