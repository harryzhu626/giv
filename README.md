# GIV, genshin impact (character data) visualizer ver 3.5

to-do functionalities: 
- display character info when hovering mouse over icons
  - data fields: name, element, weapon, etc. 
  - link to wiki page
 - update region icons with names
- download button for chart
- CN option
(- add some analytics, e.g. 4/5 star ratios for each element)
(- optimize for browser on phone?)


## reflections so far
- scalability: the app isn't designed with scalability in mind, nor does it need to worry about scalability. The game will not add new attributes to characters and since at most 2 characters are introduced per version, if the game runs for another 4 years, the character roster will only increase by 70 characters ((52 weeks / 1/6 version/week) x 2 char/version x 4).
- creating the table: I'm sure there are better way to generate table than rewriting html for each filter change. 
